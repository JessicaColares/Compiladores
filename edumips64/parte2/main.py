import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from ThreeAddressCodeVisitor import ThreeAddressCodeVisitor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file.c>")
        return
    
    input_file = sys.argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')
    
    lexer = SimpleLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleLangParser(tokens)
    tree = parser.program()
    
    converter = ThreeAddressCodeVisitor()
    converter.parser = parser  # Adiciona referência ao parser
    three_address_code = converter.visit(tree)
    
    output_file = input_file.replace('.c', '.tac')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(three_address_code)
    
    print(f"Codigo Three-address gerado em {output_file}")
    print("Codigo gerado: ")
    print(three_address_code)  # Mostra o código no console

if __name__ == '__main__':
    main()