from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from Listener import Listener

def avaliar(expressao):
    input_stream = InputStream(expressao)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()
    
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    return listener.get_result()

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