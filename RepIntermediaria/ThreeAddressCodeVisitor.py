from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor

class ThreeAddressCodeVisitor(SimpleLangVisitor):
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []
        self.symbol_table = set()
    
    def new_temp(self):
        self.temp_count += 1
        return f't{self.temp_count}'
    
    def new_label(self):
        self.label_count += 1
        return f'L{self.label_count}'
    
    def emit(self, text):
        self.code.append(text)

    def get_code(self):
        return '\n'.join(self.code)

    def visitProg(self, ctx):
        for child in ctx.children:
            self.visit(child)
        return self.get_code()

    def visitFunction(self, ctx):
        func_name = ctx.ID().getText()
        self.emit(f"{func_name}:")
        self.visit(ctx.block())
        self.emit("")

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitDeclaration(self, ctx):
        var = ctx.ID().getText()
        self.symbol_table.add(var)
        if ctx.expression():
            value = self.visit(ctx.expression())
            self.emit(f"{var} = {value}")
        else:
            self.emit(f"{var} = 0")

    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.expression())
        true_label = self.new_label()
        false_label = self.new_label()
        end_label = self.new_label()
        
        self.emit(f"if {cond} goto {true_label}")
        self.emit(f"goto {false_label}")
        self.emit(f"{true_label}:")
        self.visit(ctx.block(0))
        self.emit(f"goto {end_label}")
        self.emit(f"{false_label}:")
        if ctx.block(1) is not None:
            self.visit(ctx.block(1))
        self.emit(f"{end_label}:")

    def visitWhileStatement(self, ctx):
        start_label = self.new_label()
        cond_label = self.new_label()
        end_label = self.new_label()
        
        self.emit(f"{start_label}:")
        cond = self.visit(ctx.expression())
        self.emit(f"if {cond} goto {cond_label}")
        self.emit(f"goto {end_label}")
        self.emit(f"{cond_label}:")
        self.visit(ctx.block())
        self.emit(f"goto {start_label}")
        self.emit(f"{end_label}:")

    def visitAssignment(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.emit(f"{var} = {value}")
        return var

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expression())
        self.emit(f"return {value}")
        return value

    def visitLogicalOr(self, ctx):
        if len(ctx.logicalAnd()) > 1:
            temp = self.new_temp()
            for i, expr in enumerate(ctx.logicalAnd()):
                value = self.visit(expr)
                if i == 0:
                    self.emit(f"{temp} = {value}")
                else:
                    self.emit(f"{temp} = {temp} || {value}")
            return temp
        return self.visit(ctx.logicalAnd(0))

    def visitLogicalAnd(self, ctx):
        if len(ctx.equality()) > 1:
            temp = self.new_temp()
            for i, expr in enumerate(ctx.equality()):
                value = self.visit(expr)
                if i == 0:
                    self.emit(f"{temp} = {value}")
                else:
                    self.emit(f"{temp} = {temp} && {value}")
            return temp
        return self.visit(ctx.equality(0))

    def visitEquality(self, ctx):
        if len(ctx.relational()) > 1:
            left = self.visit(ctx.relational(0))
            right = self.visit(ctx.relational(1))
            op = ctx.getChild(1).getText()
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp
        return self.visit(ctx.relational(0))

    def visitRelational(self, ctx):
        if len(ctx.additive()) > 1:
            left = self.visit(ctx.additive(0))
            right = self.visit(ctx.additive(1))
            op = ctx.getChild(1).getText()
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp
        return self.visit(ctx.additive(0))

    def visitAdditive(self, ctx):
        if len(ctx.multiplicative()) > 1:
            left = self.visit(ctx.multiplicative(0))
            for i in range(1, len(ctx.multiplicative())):
                op = ctx.getChild(2*i-1).getText()
                right = self.visit(ctx.multiplicative(i))
                temp = self.new_temp()
                self.emit(f"{temp} = {left} {op} {right}")
                left = temp
            return left
        return self.visit(ctx.multiplicative(0))

    def visitMultiplicative(self, ctx):
        if len(ctx.unary()) > 1:
            left = self.visit(ctx.unary(0))
            for i in range(1, len(ctx.unary())):
                op = ctx.getChild(2*i-1).getText()
                right = self.visit(ctx.unary(i))
                temp = self.new_temp()
                self.emit(f"{temp} = {left} {op} {right}")
                left = temp
            return left
        return self.visit(ctx.unary(0))

    def visitUnary(self, ctx):
        if ctx.unary():
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.unary())
            temp = self.new_temp()
            self.emit(f"{temp} = {op}{expr}")
            return temp
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
        if ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.INT():
            return ctx.INT().getText()
        return None