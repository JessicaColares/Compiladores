import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from ThreeAddressCodeVisitor import ThreeAddressCodeVisitor

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo_entrada>")
        return

    input_stream = FileStream(sys.argv[1])
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    
    try:
        tree = parser.prog()
        visitor = ThreeAddressCodeVisitor()
        output = visitor.visit(tree)
        print(output)
    except Exception as e:
        print(f"Erro durante a compilação: {e}")

if __name__ == '__main__':
    main()