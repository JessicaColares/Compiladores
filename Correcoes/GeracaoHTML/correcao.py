import os
import subprocess
import shutil
import sys
import re
from pathlib import Path

# Cores para terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

class HtmlGrader:
    def __init__(self, student_dir):
        self.student_dir = Path(student_dir)
        self.student_name = self.student_dir.name
        
    def find_main_py(self):
        """Encontra o arquivo Python principal"""
        py_files = list(self.student_dir.glob("*.py"))
        if not py_files:
            return None
        
        priority_names = ["main.py", "Principal.py", "principal.py", "app.py", "run.py"]
        for py_file in py_files:
            if py_file.name in priority_names:
                return py_file
        
        for py_file in py_files:
            if 'listener' not in py_file.name.lower() and 'visitor' not in py_file.name.lower():
                return py_file
        
        return py_files[0]
    
    def find_grammar_file(self):
        """Encontra o arquivo de gramática (.g ou .g4)"""
        for f in self.student_dir.glob("*.g*"):
            if f.suffix in ['.g', '.g4']:
                return f
        return None
    
    def find_input_file(self):
        """Encontra o arquivo de entrada de teste (.txt)"""
        for f in self.student_dir.glob("*.txt"):
            return f
        return None
    
    def compile_grammar(self):
        """Compila a gramática com ANTLR"""
        grammar_file = self.find_grammar_file()
        if not grammar_file:
            return False, "Arquivo de gramática não encontrado"
        
        antlr_jar = self.student_dir / "antlr-4.13.2-complete.jar"
        if not antlr_jar.exists():
            return False, "ANTLR JAR não encontrado"
        
        try:
            cmd = [
                "java", "-jar", str(antlr_jar),
                "-Dlanguage=Python3", "-visitor", "-listener",
                str(grammar_file)
            ]
            result = subprocess.run(cmd, cwd=self.student_dir, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                return False, f"Erro na compilação: {result.stderr}"
            
            return True, "Compilado com sucesso"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def generate_html(self, main_py, input_file):
        """Executa o programa e gera o HTML"""
        original_dir = os.getcwd()
        os.chdir(self.student_dir)
        
        try:
            # Verifica se o programa lê de arquivo ou usa stdin
            program_type = "stdin"
            try:
                with open(main_py, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'open(' in content and '.txt' in content:
                        program_type = "arquivo"
                    elif 'sys.argv' in content:
                        program_type = "argumento"
            except:
                pass
            
            output_file = self.student_dir / "output.html"
            
            # Modo arquivo
            if program_type == "arquivo" and input_file:
                cmd = [sys.executable, str(main_py), str(input_file)]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                if result.returncode == 0 and result.stdout:
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(result.stdout)
                    return True, "HTML gerado com sucesso (modo arquivo)", result.stdout[:500]
                else:
                    return False, f"Erro na execução: {result.stderr or 'sem saída'}", None
            
            # Modo argumento
            elif program_type == "argumento":
                # Procura o arquivo de entrada
                if not input_file:
                    return False, "Arquivo de entrada não encontrado", None
                
                cmd = [sys.executable, str(main_py), str(input_file)]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                if result.returncode == 0 and result.stdout:
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(result.stdout)
                    return True, "HTML gerado com sucesso (modo argumento)", result.stdout[:500]
                else:
                    # Tenta com redirecionamento de arquivo
                    cmd = [sys.executable, str(main_py), str(input_file)]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                    if result.returncode == 0 and result.stdout:
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(result.stdout)
                        return True, "HTML gerado com sucesso (modo argumento)", result.stdout[:500]
                    else:
                        return False, f"Erro na execução: {result.stderr or 'sem saída'}", None
            
            # Modo stdin (padrão)
            else:
                # Primeiro tenta ler do arquivo de entrada
                if input_file and input_file.exists():
                    with open(input_file, 'r', encoding='utf-8') as f:
                        input_data = f.read()
                    
                    cmd = [sys.executable, str(main_py)]
                    result = subprocess.run(
                        cmd,
                        input=input_data,
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                    
                    if result.returncode == 0 and result.stdout:
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(result.stdout)
                        return True, "HTML gerado com sucesso (stdin com arquivo)", result.stdout[:500]
                
                # Se não funcionou, tenta interativo
                cmd = [sys.executable, str(main_py)]
                result = subprocess.run(
                    cmd,
                    input="\n",
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0 and result.stdout:
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(result.stdout)
                    return True, "HTML gerado com sucesso (stdin interativo)", result.stdout[:500]
                
                return False, "Não foi possível gerar HTML", None
                
        except subprocess.TimeoutExpired:
            return False, "Timeout (10s)", None
        except Exception as e:
            return False, f"Erro: {str(e)}", None
        finally:
            os.chdir(original_dir)
    
    def validate_html(self, html_content):
        """Valida se o HTML gerado contém elementos básicos"""
        if not html_content:
            return False, "HTML vazio"
        
        checks = []
        
        # Verifica tags básicas
        if '<html' in html_content or '<HTML' in html_content:
            checks.append(("Tag <html>", True))
        else:
            checks.append(("Tag <html>", False))
        
        if '<body' in html_content or '<BODY' in html_content:
            checks.append(("Tag <body>", True))
        else:
            checks.append(("Tag <body>", False))
        
        # Verifica elementos esperados (menu, botão, tabela)
        has_menu = '<select' in html_content or '<SELECT' in html_content
        has_button = '<button' in html_content or '<BUTTON' in html_content or 'onclick' in html_content
        has_table = '<table' in html_content or '<TABLE' in html_content
        has_caption = '<caption' in html_content or '<CAPTION' in html_content
        has_th = '<th' in html_content or '<TH' in html_content
        
        checks.append(("Menu (<select>)", has_menu))
        checks.append(("Botão (<button>)", has_button))
        checks.append(("Tabela (<table>)", has_table))
        checks.append(("Legenda (<caption>)", has_caption))
        checks.append(("Cabeçalho (<th>)", has_th))
        
        return checks
    
    def grade_student(self):
        """Avalia o aluno"""
        print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}Avaliando: {self.student_name}{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        # Encontra arquivos
        main_py = self.find_main_py()
        if not main_py:
            print(f"{Colors.RED}✗ Nenhum arquivo Python encontrado{Colors.END}")
            return
        
        grammar_file = self.find_grammar_file()
        if not grammar_file:
            print(f"{Colors.RED}✗ Nenhum arquivo de gramática encontrado{Colors.END}")
            return
        
        input_file = self.find_input_file()
        if input_file:
            print(f"  Arquivo de entrada: {input_file.name}")
        else:
            print(f"{Colors.YELLOW}  ⚠ Nenhum arquivo de entrada (.txt) encontrado{Colors.END}")
        
        print(f"  Arquivo Python: {main_py.name}")
        print(f"  Gramática: {grammar_file.name}")
        
        # Compila a gramática
        print(f"\n{Colors.BOLD}Compilando gramática...{Colors.END}")
        compiled, msg = self.compile_grammar()
        if not compiled:
            print(f"{Colors.RED}✗ {msg}{Colors.END}")
            return
        print(f"{Colors.GREEN}✓ {msg}{Colors.END}")
        
        # Gera o HTML
        print(f"\n{Colors.BOLD}Gerando HTML...{Colors.END}")
        success, msg, html_preview = self.generate_html(main_py, input_file)
        
        if not success:
            print(f"{Colors.RED}✗ {msg}{Colors.END}")
            return
        print(f"{Colors.GREEN}✓ {msg}{Colors.END}")
        
        # Valida o HTML
        html_file = self.student_dir / "output.html"
        if html_file.exists():
            print(f"\n{Colors.BOLD}Arquivo gerado: {html_file}{Colors.END}")
            
            # Mostra tamanho do arquivo
            size = html_file.stat().st_size
            print(f"  Tamanho: {size} bytes")
            
            # Valida o conteúdo
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            checks = self.validate_html(html_content)
            
            print(f"\n{Colors.BOLD}Verificação do HTML:{Colors.END}")
            all_passed = True
            for check_name, passed in checks:
                if passed:
                    print(f"  {Colors.GREEN}✓ {check_name}{Colors.END}")
                else:
                    print(f"  {Colors.RED}✗ {check_name}{Colors.END}")
                    all_passed = False
            
            if all_passed:
                print(f"\n{Colors.GREEN}{Colors.BOLD}✅ HTML gerado com todos os elementos esperados!{Colors.END}")
                print(f"{Colors.GREEN}  Arquivo salvo em: {html_file}{Colors.END}")
            else:
                print(f"\n{Colors.YELLOW}⚠ Alguns elementos não foram encontrados no HTML{Colors.END}")
                print(f"{Colors.YELLOW}  Verifique se o programa gerou o HTML corretamente{Colors.END}")
                print(f"{Colors.YELLOW}  Arquivo salvo em: {html_file}{Colors.END}")
            
            # Mostra preview
            print(f"\n{Colors.BOLD}Preview (primeiros 300 caracteres):{Colors.END}")
            print(html_content[:300] + ("..." if len(html_content) > 300 else ""))
            
        else:
            print(f"{Colors.RED}✗ Arquivo HTML não foi gerado{Colors.END}")


def main():
    """Função principal"""
    base_dir = Path.cwd()
    
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Corretor Automático - Atividade 05 (Geração de HTML){Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    
    # Verifica pexpect
    try:
        import pexpect
        print(f"{Colors.GREEN}✓ pexpect disponível{Colors.END}")
    except ImportError:
        print(f"{Colors.YELLOW}⚠ pexpect não instalado (opcional){Colors.END}")
    
    # Encontra alunos
    students = []
    for item in base_dir.iterdir():
        if item.is_dir() and item.name not in ["Testes", ".git", "__pycache__"] and not item.name.startswith('.'):
            students.append(item)
    
    if not students:
        print(f"{Colors.YELLOW}Nenhum aluno encontrado na pasta atual.{Colors.END}")
        return
    
    print(f"\nEncontrados {len(students)} alunos")
    print("Iniciando correção...\n")
    
    for student_dir in students:
        try:
            grader = HtmlGrader(student_dir)
            grader.grade_student()
        except Exception as e:
            print(f"{Colors.RED}Erro ao avaliar {student_dir.name}: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}Correção finalizada!{Colors.END}")


if __name__ == "__main__":
    main()