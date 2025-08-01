from antlr4 import *
from URLLexer import URLLexer
import sys

# Compiladores - Atividade Analisador Lexico
# Nome: Jessica de Figueredo Colares
# Matricula: 22060036

def validate_url_structure(tokens, lexer):
    if len(tokens) < 3:
        return False
    
    first_token = lexer.symbolicNames[tokens[0].type]
    second_token = lexer.symbolicNames[tokens[1].type]
    
    if first_token not in ['HTTP', 'HTTPS', 'FTP']:
        return False
    if second_token != 'PROTOCOL_SEP':
        return False
    if lexer.symbolicNames[tokens[2].type] != 'DOMAIN':
        return False
    
    return True

def format_protocol(protocol):
    mappings = {
        'http': 'http',
        'https': 'https',
        'ftp': 'ftp',
    }
    return mappings.get(protocol.lower(), protocol)

def main():
    print("\nAnalisador Léxico de URLs")
    print("Digite a URL para análise ou 'sair' para terminar:")
    
    while True:
        url = input("> ").strip()
        
        if url.lower() == 'sair':
            break
            
        input_stream = InputStream(url)
        lexer = URLLexer(input_stream)
        
        try:
            tokens = list(lexer.getAllTokens())
            
            if not validate_url_structure(tokens, lexer):
                print("\nERRO: A URL não é válida - estrutura incorreta")
                print("Formato esperado: protocolo://domínio[/caminho][?query][#fragmento]")
                continue
                
            print("\nComponentes reconhecidos:")
            
            token_labels = {
                'HTTP': 'Protocolo',
                'HTTPS': 'Protocolo',
                'FTP': 'Protocolo',
                'PROTOCOL_SEP': '',
                'DOMAIN': 'Domínio',
                'PORT': 'Porta',
                'PATH': 'Caminho',
                'QUERY': 'Query',
                'FRAGMENT': 'Fragmento'
            }
            
            for token in tokens:
                token_type = lexer.symbolicNames[token.type]
                if token_type in token_labels and token_labels[token_type]:
                    label = token_labels[token_type] + ":"
                    value = token.text
                    
                    if token_type == 'FRAGMENT':
                        value = value[1:]
                    elif token_type == 'QUERY':
                        value = value[1:]
                    elif token_type == 'PORT':
                        value = value[1:]
                    elif token_type in ('HTTP', 'HTTPS', 'FTP'):
                        value = format_protocol(value)
                    
                    print(f"{label:<12} {value}")
            
        except Exception as e:
            print("\nERRO: A URL não é válida -", str(e))
            print("Por favor, digite uma URL válida")
        
        print("\nDigite outra URL ou 'sair' para terminar:")

if __name__ == '__main__':
    main()