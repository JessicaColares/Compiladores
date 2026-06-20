import sys
from antlr4 import *
from miniCLexer import miniCLexer
from miniCParser import miniCParser
from miniCListener import miniCListener

# --- Compiladores ---
# --- Analise Sintatica ---
# Nome: Jessica de Figueredo Colares
# Matricula: 22060036

class AnalisadorMiniC(miniCListener):
    def __init__(self):
        self.tabela_simbolos = {
            'variaveis': [],     # Lista de dicionários: {nome, tipo, escopo}
            'funcoes': {},      # Dicionário: {nome_funcao: {tipo_retorno, parametros}}
            'estruturas': []     # Lista de dicionários: {tipo, condicao}
        }

    # --- Variáveis Globais/Locais ---
    def enterData_definition(self, ctx):
        tipo = ctx.INT().getText()  # "int"
        for declarador in ctx.declarator():
            nome_var = declarador.getText()
            escopo = 'global' if isinstance(ctx.parentCtx.parentCtx, miniCParser.ProgramContext) else 'local'
            self.tabela_simbolos['variaveis'].append({
                'nome': nome_var,
                'tipo': tipo,
                'escopo': escopo
            })

    # --- Funções ---
    def enterFunction_definition(self, ctx):
        tipo_retorno = ctx.INT().getText() if ctx.INT() else 'void'
        nome_funcao = ctx.function_header().declarator().getText()
        parametros = []

        # Extrai parâmetros (se existirem)
        if ctx.function_header().parameter_list().parameter_declaration():
            for param in ctx.function_header().parameter_list().parameter_declaration().declarator():
                parametros.append({
                    'nome': param.getText(),
                    'tipo': 'int'  # miniC só tem "int"
                })

        self.tabela_simbolos['funcoes'][nome_funcao] = {
            'tipo_retorno': tipo_retorno,
            'parametros': parametros
        }

    # --- Estruturas de Controle ---
    def enterStatement(self, ctx):
        if ctx.IF():
            self.tabela_simbolos['estruturas'].append({
                'tipo': 'if',
                'condicao': ctx.expression().getText()
            })
        elif ctx.WHILE():
            self.tabela_simbolos['estruturas'].append({
                'tipo': 'while',
                'condicao': ctx.expression().getText()
            })

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.miniC>")
        sys.exit(1)

    # Carrega o arquivo de entrada
    input_stream = FileStream(sys.argv[1])
    
    # Gera os analisadores léxico e sintático
    lexer = miniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = miniCParser(stream)
    tree = parser.program()

    # --- Árvore Sintática (opcional) ---
    print("\n[ÁRVORE SINTÁTICA]")
    print(tree.toStringTree(recog=parser), "\n")

    # --- Análise com Listener ---
    analisador = AnalisadorMiniC()
    walker = ParseTreeWalker()
    walker.walk(analisador, tree)

    # --- Resultados ---
    print("\n=== TABELA DE SÍMBOLOS ===")
    print("\nVariáveis:")
    for var in analisador.tabela_simbolos['variaveis']:
        print(f"- {var['nome']} (Tipo: {var['tipo']}, Escopo: {var['escopo']})")

    print("\nFunções:")
    for nome, dados in analisador.tabela_simbolos['funcoes'].items():
        print(f"- {nome} (Retorno: {dados['tipo_retorno']}, Parâmetros: {[p['nome'] for p in dados['parametros']]})")

    print("\nEstruturas de Controle:")
    for estrutura in analisador.tabela_simbolos['estruturas']:
        print(f"- {estrutura['tipo'].upper()}: Condição = {estrutura['condicao']}")

if __name__ == '__main__':
    main()