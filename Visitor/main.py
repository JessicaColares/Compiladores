from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from Visitor import Visitor

# Jessica de Figueredo Colares - 22060036

def avaliar(expressao):
    input_stream = InputStream(expressao)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()
    
    visitor = Visitor()
    resultado = visitor.visit(tree)
    
    return resultado

if __name__ == '__main__':
    print("Calculadora de Expressões (digite 'sair' para terminar)")
    while True:
        try:
            expr = input(">> ")
            if expr.lower() == 'sair':
                break
            print(f"= {avaliar(expr)}")
        except Exception as e:
            print(f"Erro: {e}")