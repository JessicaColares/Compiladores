from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor

class ThreeAddressCodeVisitor(SimpleLangVisitor):
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []
        self.symbols = set()

    def new_temp(self):
        self.temp_count += 1
        return f't{self.temp_count}'

    def new_label(self):
        self.label_count += 1
        return f'L{self.label_count}'

    def visitProgram(self, ctx):
        for child in ctx.children:
            if isinstance(child, self.parser.FunctionContext):
                self.visitFunction(child)
            elif isinstance(child, self.parser.Global_declarationContext):
                self.visitGlobal_declaration(child)
        return '\n'.join(self.code)

    def visitGlobal_declaration(self, ctx):
        self.visit(ctx.var_list())

    def visitFunction(self, ctx):
        func_name = ctx.ID().getText()
        self.code.append(f'\n{func_name}:')

        if ctx.params() and ctx.params().param():
            for param in ctx.params().param():
                param_name = param.ID().getText()
                self.symbols.add(param_name)
                self.code.append(f'param {param_name}')

        self.visit(ctx.block())

    def visitBlock(self, ctx):
        for item in ctx.children:
            if isinstance(item, self.parser.DeclarationContext):
                self.visitDeclaration(item)
            elif isinstance(item, self.parser.StatementContext):
                self.visit(item)

    def visitDeclaration(self, ctx):
        self.visit(ctx.var_list())

    def visitExprStmt(self, ctx):
        self.visit(ctx.expression())

    def visitReturnStmt(self, ctx):
        value = self.visit(ctx.expression())
        self.code.append(f'return {value}')

    def visitAssignExpr(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.code.append(f'{var} = {value}')
        return var

    def visitMultAssignExpr(self, ctx):
        var = ctx.ID().getText()
        temp = self.new_temp()
        value = self.visit(ctx.expression())
        self.code.append(f'{temp} = {var} * {value}')
        self.code.append(f'{var} = {temp}')
        return var

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f'{temp} = {left} {op} {right}')
        return temp

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f'{temp} = {left} {op} {right}')
        return temp

    def visitRelExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f'{temp} = {left} {op} {right}')
        return temp

    def visitCompoundAssignExpr(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expression())
        op = ctx.op.text[0]
        temp = self.new_temp()
        self.code.append(f'{temp} = {var} {op} {value}')
        self.code.append(f'{var} = {temp}')
        return var

    def visitPreIncExpr(self, ctx):
        var = ctx.ID().getText()
        self.code.append(f'{var} = {var} + 1')
        return var

    def visitPreDecExpr(self, ctx):
        var = ctx.ID().getText()
        self.code.append(f'{var} = {var} - 1')
        return var

    def visitCharExpr(self, ctx):
        return str(ord(ctx.CHAR().getText()[1]))

    def visitVarExpr(self, ctx):
        return ctx.ID().getText()

    def visitIntExpr(self, ctx):
        return ctx.INT().getText()

    def visitStringExpr(self, ctx):
        return ctx.STRING().getText()

    def visitCallExpr(self, ctx):
        func_name = ctx.ID().getText()

        if ctx.argList():
            for arg in ctx.argList().children:
                if isinstance(arg, TerminalNode):
                    if arg.getSymbol().type == self.parser.STRING:
                        self.code.append(f'# string ignorada: {arg.getText()}')
                else:
                    value = self.visit(arg)
                    self.code.append(f'arg {value}')

        self.code.append(f'call {func_name}')

    def visitVar_list(self, ctx):
        var_count = len(ctx.ID())
        expr_count = len(ctx.expression()) if ctx.expression() else 0

        for i in range(var_count):
            var_name = ctx.ID(i).getText()
            self.symbols.add(var_name)

            if i < expr_count:
                value = self.visit(ctx.expression(i))
                self.code.append(f'{var_name} = {value}')
            else:
                self.code.append(f'{var_name} = 0')

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expression())
        label_else = self.new_label()
        label_end = self.new_label()

        self.code.append(f'else {cond} goto {label_else}')
        self.visit(ctx.block(0))

        if ctx.block(1):
            self.code.append(f'goto {label_end}')
            self.code.append(f'{label_else}:')
            self.visit(ctx.block(1))
            self.code.append(f'{label_end}:')
        else:
            self.code.append(f'{label_else}:')

    def visitWhileStmt(self, ctx):
        label_start = self.new_label()
        label_end = self.new_label()

        self.code.append(f'{label_start}:')
        cond = self.visit(ctx.expression())
        self.code.append(f'else {cond} goto {label_end}')
        self.visit(ctx.block())
        self.code.append(f'goto {label_start}')
        self.code.append(f'{label_end}:')

    def visitPrintfExpr(self, ctx):
        # Obtém todos os filhos do nó printfExpr
        children = list(ctx.getChildren())
        
        # O primeiro filho é 'printf', o segundo '(', o terceiro é a STRING, 
        # o quarto ',', o quinto é o argumento (ID/INT/CHAR), o sexto ')'
        if len(children) >= 6:
            format_str = children[2].getText()  # STRING
            arg = children[4].getText()        # ID/INT/CHAR
            
            # Gera código de três endereços para printf
            self.code.append(f'arg {format_str}')
            self.code.append(f'arg {arg}')
            self.code.append('call printf')
        else:
            # Caso inesperado (gerar erro ou ignorar)
            self.code.append("# erro: formato de printf inválido")