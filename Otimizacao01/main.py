import sys
from antlr4 import *
from ThreeAddressCodeLexer import ThreeAddressCodeLexer
from ThreeAddressCodeParser import ThreeAddressCodeParser
from ThreeAddressCodeOptimizer import ThreeAddressCodeOptimizer

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo_entrada.txt")
        sys.exit(1)
    
    # Lê o arquivo e garante que termina com uma quebra de linha
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        code = f.read()
        code = code.replace('\r\n', '\n').replace('\r', '\n')
        if not code.endswith('\n'):
            code += '\n'
    
    # Remove linhas vazias para evitar problemas com o parser
    lines = [line for line in code.splitlines() if line.strip()]
    code = '\n'.join(lines) + '\n'
    
    # Cria o input stream
    input_stream = InputStream(code)
    
    # Configura o lexer e parser
    lexer = ThreeAddressCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ThreeAddressCodeParser(stream)
    
    # Executa o parser (ignorando erros de sintaxe)
    parser.removeErrorListeners()
    tree = parser.program()
    
    # Otimiza o código
    optimizer = ThreeAddressCodeOptimizer()
    optimized_code = optimizer.optimize(lines)
    
    # Imprime o código otimizado
    for line in optimized_code:
        if line.strip():  # Ignora linhas vazias
            print(line)

if __name__ == '__main__':
    main()