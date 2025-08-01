from antlr4 import *
from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from Visitor import Visitor

def main():
    # Carrega o arquivo de entrada
    input_file = FileStream("input.txt", encoding="utf-8")
    
    # Cria o lexer e parser
    lexer = HtmlLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = HtmlParser(stream)
    
    # Parseia o conteúdo
    tree = parser.root()
    
    # Executa o visitor
    visitor = Visitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()