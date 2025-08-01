import sys
from antlr4 import *
from miniCLexer import miniCLexer
from miniCParser import miniCParser
from miniCVisitor import miniCVisitor

# Jessica de Figueredo Colares
# 22060036

class SemanticError:
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Erro semântico na linha {self.line}, coluna {self.column}: {self.message}"

class AnalisadorMiniC(miniCVisitor):
    def __init__(self):
        self.erros = []
        self.tabela_simbolos = {
            'variaveis': {},
            'funcoes': {},
            'escopo_atual': 'global'
        }
        self.escopos_anteriores = []
        self.loop_stack = []  # Pilha para controlar loops aninhados
    
    def adicionar_erro(self, message, ctx):
        token = ctx.start
        self.erros.append(SemanticError(message, token.line, token.column))
    
    def verificar_tipo(self, tipo1, tipo2, ctx):
        if tipo1 != tipo2:
            self.adicionar_erro(f"Tipos incompatíveis: {tipo1} e {tipo2}", ctx)
            return False
        return True
    
    def obter_tipo_variavel(self, nome, ctx=None):
        escopos = [self.tabela_simbolos['escopo_atual']] + self.escopos_anteriores + ['global']
        
        for escopo in escopos:
            if escopo in self.tabela_simbolos['variaveis']:
                if nome in self.tabela_simbolos['variaveis'][escopo]:
                    return self.tabela_simbolos['variaveis'][escopo][nome]
        
        return None
    
    def visitCOMMENT(self, ctx):
        return None
    
    def visitLINE_COMMENT(self, ctx):
        return None
    
    def visitProgram(self, ctx):
        self.tabela_simbolos['variaveis']['global'] = {}
        self.visitChildren(ctx)
        return None
    
    def visitFunction_definition(self, ctx):
        func_name = ctx.function_header().IDENTIFIER().getText()
        return_type = ctx.type_().getText() if ctx.type_() else 'void'
        
        parametros = []
        if ctx.function_header().parameter_list():
            for param in ctx.function_header().parameter_list().parameter_declaration():
                tipo = param.type_().getText()
                nome = param.declarator().IDENTIFIER().getText()
                parametros.append({'nome': nome, 'tipo': tipo})
        
        self.tabela_simbolos['funcoes'][func_name] = {
            'tipo_retorno': return_type,
            'parametros': parametros
        }
        
        self.escopos_anteriores.append(self.tabela_simbolos['escopo_atual'])
        self.tabela_simbolos['escopo_atual'] = func_name
        self.tabela_simbolos['variaveis'][func_name] = {}
        
        for param in parametros:
            self.tabela_simbolos['variaveis'][func_name][param['nome']] = param['tipo']
        
        self.visit(ctx.function_body())
        
        self.tabela_simbolos['escopo_atual'] = self.escopos_anteriores.pop()
        return None
    
    def visitBlock(self, ctx):
        escopo_anterior = self.tabela_simbolos['escopo_atual']
        novo_escopo = f"{escopo_anterior}_block_{id(ctx)}"
        
        self.escopos_anteriores.append(escopo_anterior)
        self.tabela_simbolos['escopo_atual'] = novo_escopo
        self.tabela_simbolos['variaveis'][novo_escopo] = {}
        
        self.visitChildren(ctx)
        
        self.tabela_simbolos['escopo_atual'] = self.escopos_anteriores.pop()
        return None
    
    def visitData_definition(self, ctx):
        tipo = ctx.type_().getText()
    
        for declarador in ctx.declarator():
            nome_var = declarador.IDENTIFIER().getText()
        
            if nome_var in self.tabela_simbolos['variaveis'].get(self.tabela_simbolos['escopo_atual'], {}):
                self.adicionar_erro(f"Variável '{nome_var}' já declarada neste escopo", declarador)
                continue
            
            if self.tabela_simbolos['escopo_atual'] not in self.tabela_simbolos['variaveis']:
                self.tabela_simbolos['variaveis'][self.tabela_simbolos['escopo_atual']] = {}
            
            self.tabela_simbolos['variaveis'][self.tabela_simbolos['escopo_atual']][nome_var] = tipo
        
            if declarador.expression():
                tipo_expr = self.visit(declarador.expression())
                if tipo_expr and tipo_expr != tipo:
                    self.adicionar_erro(
                        f"Tipo incompatível na inicialização. Esperado: {tipo}, obtido: {tipo_expr}",
                        declarador.expression()
                    )
        return None
    
    def visitFunction_call(self, ctx):
        nome_funcao = ctx.IDENTIFIER().getText()
        
        if nome_funcao not in self.tabela_simbolos['funcoes']:
            self.adicionar_erro(f"Função '{nome_funcao}' não declarada", ctx)
            return None
        
        funcao = self.tabela_simbolos['funcoes'][nome_funcao]
        args = ctx.argument_list().expression() if ctx.argument_list() else []
        
        if len(args) != len(funcao['parametros']):
            self.adicionar_erro(
                f"Número incorreto de argumentos para '{nome_funcao}'. Esperados: {len(funcao['parametros'])}, fornecidos: {len(args)}", 
                ctx
            )
        
        for i, (arg, param) in enumerate(zip(args, funcao['parametros'])):
            tipo_arg = self.visit(arg)
            if tipo_arg and tipo_arg != param['tipo']:
                self.adicionar_erro(
                    f"Tipo incorreto para argumento {i+1} de '{nome_funcao}'. Esperado: {param['tipo']}, fornecido: {tipo_arg}", 
                    arg
                )
        
        return funcao['tipo_retorno']
    
    def visitPrimary(self, ctx):
        if ctx.IDENTIFIER():
            nome = ctx.IDENTIFIER().getText()
            tipo_var = self.obter_tipo_variavel(nome, ctx)
            
            if tipo_var:
                return tipo_var
            elif nome in self.tabela_simbolos['funcoes']:
                return self.tabela_simbolos['funcoes'][nome]['tipo_retorno']
            else:
                self.adicionar_erro(f"Identificador '{nome}' não declarado", ctx)
                return None
            
        elif ctx.CONSTANT_INT():
            return 'int'
        elif ctx.CONSTANT_CHAR():
            return 'char'
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None
    
    def visitBinary(self, ctx):
        if ctx.IDENTIFIER() and ctx.getChild(1).getText() in ['=', '+=', '-=', '*=', '/=', '%=']:
            nome_var = ctx.IDENTIFIER().getText()
            tipo_var = self.obter_tipo_variavel(nome_var, ctx)
            
            if not tipo_var:
                self.adicionar_erro(f"Variável '{nome_var}' não declarada", ctx)
                return None
            
            tipo_expr = self.visit(ctx.binary(0))
            if tipo_expr:
                if ctx.getChild(1).getText() != '=' and tipo_var != 'int':
                    self.adicionar_erro(
                        f"Operação '{ctx.getChild(1).getText()}' só é permitida para inteiros",
                        ctx
                    )
                elif not self.verificar_tipo(tipo_var, tipo_expr, ctx):
                    self.adicionar_erro(
                        f"Tipos incompatíveis na atribuição. Esperado: {tipo_var}, fornecido: {tipo_expr}",
                        ctx
                    )
            return tipo_var
        
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/', '%']:
            left_type = self.visit(ctx.getChild(0))
            right_type = self.visit(ctx.getChild(2))
        
            if left_type and right_type:
                if ctx.getChild(1).getText() != '+' and (left_type != 'int' or right_type != 'int'):
                    self.adicionar_erro(
                        f"Operação '{ctx.getChild(1).getText()}' requer operandos do tipo 'int'",
                        ctx
                    )
                elif ctx.getChild(1).getText() == '+' and left_type != right_type:
                    self.adicionar_erro(
                        "Operação '+' requer operandos do mesmo tipo",
                        ctx
                    )
                
                return left_type if left_type == right_type else None
        
        return self.visitChildren(ctx)
    
    def visitUnary(self, ctx):
        if ctx.IDENTIFIER():
            nome_var = ctx.IDENTIFIER().getText()
            tipo_var = self.obter_tipo_variavel(nome_var, ctx)
            if not tipo_var:
                self.adicionar_erro(f"Variável '{nome_var}' não declarada", ctx)
                return None
                
            if tipo_var != 'int':
                self.adicionar_erro(f"Operação '{ctx.getChild(0).getText()}' não permitida para tipo '{tipo_var}'", ctx)
            
            return tipo_var
        return self.visitChildren(ctx)
    
    def visitWhile_statement(self, ctx):
        self.loop_stack.append(True)
        tipo_cond = self.visit(ctx.expression())
        if tipo_cond and tipo_cond != 'int':
            self.adicionar_erro("Condição do while deve ser do tipo 'int'", ctx.expression())
        self.visit(ctx.statement())
        self.loop_stack.pop()
        return None
    
    def visitIf_statement(self, ctx):
        tipo_cond = self.visit(ctx.expression())
        if tipo_cond and tipo_cond != 'int':
            self.adicionar_erro("Condição do if deve ser do tipo 'int'", ctx.expression())
        self.visit(ctx.statement(0))
        if ctx.ELSE():
            self.visit(ctx.statement(1))
        return None
    
    def visitBreak_statement(self, ctx):
        if not self.loop_stack:
            self.adicionar_erro("Comando 'break' fora de um loop", ctx)
        return None
    
    def visitContinue_statement(self, ctx):
        if not self.loop_stack:
            self.adicionar_erro("Comando 'continue' fora de um loop", ctx)
        return None
    
    def visitReturn_statement(self, ctx):
        if ctx.expression():
            tipo_retorno = self.visit(ctx.expression())
            if self.tabela_simbolos['escopo_atual'] in self.tabela_simbolos['funcoes']:
                tipo_esperado = self.tabela_simbolos['funcoes'][self.tabela_simbolos['escopo_atual']]['tipo_retorno']
                if tipo_esperado != 'void' and not self.verificar_tipo(tipo_esperado, tipo_retorno, ctx):
                    self.adicionar_erro(
                        f"Tipo de retorno incorreto. Esperado: {tipo_esperado}, obtido: {tipo_retorno}",
                        ctx.expression()
                    )
        return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.miniC>")
        sys.exit(1)

    input_stream = FileStream(sys.argv[1])
    lexer = miniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = miniCParser(stream)
    tree = parser.program()

    analisador = AnalisadorMiniC()
    analisador.visit(tree)

    if analisador.erros:
        print("\n=== ERROS SEMÂNTICOS ===")
        for erro in analisador.erros:
            print(erro)
    else:
        print("\nNenhum erro semântico encontrado.")

    print("\n=== TABELA DE SÍMBOLOS ===")
    print("\nVariáveis:")
    for escopo, variaveis in analisador.tabela_simbolos['variaveis'].items():
        print(f"Escopo: {escopo}")
        for nome, tipo in variaveis.items():
            print(f"  {nome}: {tipo}")

    print("\nFunções:")
    for nome, dados in analisador.tabela_simbolos['funcoes'].items():
        params = ", ".join([f"{p['nome']}: {p['tipo']}" for p in dados['parametros']])
        print(f"{nome} (Retorno: {dados['tipo_retorno']}, Parâmetros: {params})")

if __name__ == '__main__':
    main()