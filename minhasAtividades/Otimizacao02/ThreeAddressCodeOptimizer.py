from antlr4 import *
from ThreeAddressCodeLexer import ThreeAddressCodeLexer
from ThreeAddressCodeParser import ThreeAddressCodeParser
from ThreeAddressCodeVisitor import ThreeAddressCodeVisitor

class ThreeAddressCodeOptimizer(ThreeAddressCodeVisitor):
    def __init__(self):
        self.constants = {}
        self.subexpressions = {}  # Armazena subexpressões e suas variáveis temporárias
        self.var_values = {}      # Armazena o valor atual de cada variável
        self.optimized_code = []
        self.changed = False

    def optimize(self, code):
        iterations = 0
        max_iterations = 10
        
        while True:
            iterations += 1
            self.changed = False
            self.optimized_code = []
            self.subexpressions = {}
            self.var_values = {}
            
            input_stream = InputStream('\n'.join(code))
            lexer = ThreeAddressCodeLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ThreeAddressCodeParser(stream)
            parser.removeErrorListeners()
            tree = parser.program()
            
            self.visitProgram(tree)
            
            if not self.changed or iterations >= max_iterations:
                break
                
            code = self.optimized_code.copy()
                
        return self.optimized_code

    def visitProgram(self, ctx):
        for child in ctx.children:
            if not isinstance(child, TerminalNode):
                self.visit(child)

    def visitAssignment(self, ctx):
        left = ctx.ID().getText()
        right_expr = self.visit(ctx.expr())
        
        # Propagação de constantes
        if right_expr.isdigit():
            self.constants[left] = right_expr
        
        # Eliminação de subexpressões comuns
        if isinstance(ctx.expr(), ThreeAddressCodeParser.BinaryExprContext):
            left_op = ctx.expr().expr(0).getText()
            right_op = ctx.expr().expr(1).getText()
            op = ctx.expr().op.text
            
            # Propagação de constantes para os operandos
            left_op = self.constants.get(left_op, left_op)
            right_op = self.constants.get(right_op, right_op)
            
            expr_key = f"{left_op} {op} {right_op}"
            self.subexpressions[expr_key] = left
        
        # Atualiza o valor da variável
        self.var_values[left] = right_expr
        
        self.optimized_code.append(f"{left} = {right_expr}")

    def visitBinaryExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        
        # Dobrando constantes (constant folding)
        folded = self._constant_folding(left, op, right)
        if folded is not None:
            self.changed = True
            return folded
        
        # Simplificação de expressões
        simplified = self._simplify_expression(left, op, right)
        if simplified is not None:
            self.changed = True
            return simplified
        
        # Propagação de constantes
        left_val = self.constants.get(left, left)
        right_val = self.constants.get(right, right)
        
        # Eliminação de subexpressões comuns
        expr_key = f"{left_val} {op} {right_val}"
        
        # Verifica se a expressão já foi computada e nenhum operando foi modificado
        if expr_key in self.subexpressions:
            existing_var = self.subexpressions[expr_key]
            # Verifica se os operandos originais não foram modificados
            if (self._check_operands_unchanged(existing_var, left_val, right_val)):
                self.changed = True
                return existing_var
        
        # Se não for uma atribuição direta, retorna a expressão
        if not isinstance(ctx.parentCtx, ThreeAddressCodeParser.AssignmentContext):
            return f"{left_val} {op} {right_val}"
        
        return f"{left_val} {op} {right_val}"

    def _constant_folding(self, left, op, right):
        if left is None or right is None:
            return None
        if left.isdigit() and right.isdigit():
            left_num = int(left)
            right_num = int(right)
            try:
                if op == '+': return str(left_num + right_num)
                elif op == '-': return str(left_num - right_num)
                elif op == '*': return str(left_num * right_num)
                elif op == '/': 
                    if right_num == 0:
                        return None
                    return str(left_num // right_num)
            except:
                return None
        return None

    def _check_operands_unchanged(self, var, left, right):
        # Verifica se os operandos originais não foram modificados
        original_expr = self.var_values.get(var, "")
        return (left in original_expr and right in original_expr)

    def _simplify_expression(self, left, op, right):
        # Regras de simplificação
        if op == '*':
            if right == '1': return left
            if left == '1': return right
            if left == '0' or right == '0': return '0'
        elif op == '/':
            if right == '1': return left
            if left == '0': return '0'
        elif op == '+':
            if right == '0': return left
            if left == '0': return right
        elif op == '-':
            if right == '0': return left
        return None

    def visitId(self, ctx):
        var = ctx.getText()
        return self.constants.get(var, var)

    def visitInt(self, ctx):
        return ctx.getText()

    def visitReturn_stmt(self, ctx):
        expr = self.visit(ctx.expr())
        self.optimized_code.append(f"return {expr}")

    def visitLabel(self, ctx):
        self.optimized_code.append(f"{ctx.ID().getText()}:")

    def visitGoto(self, ctx):
        self.optimized_code.append(f"goto {ctx.ID().getText()}")

    def visitEOL(self, ctx):
        pass
    
    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())  # Processa a expressão dentro dos parênteses