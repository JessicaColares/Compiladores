import os
import subprocess
import shutil
import sys
import re
from pathlib import Path
import csv

# Cores para terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

class MiniCGrader:
    def __init__(self, student_dir):
        self.student_dir = Path(student_dir)
        self.student_name = self.student_dir.name
        
    def find_main_py(self):
        """Encontra o arquivo Python principal"""
        py_files = list(self.student_dir.glob("*.py"))
        if not py_files:
            return None
        
        priority_names = ["main.py", "Principal.py", "principal.py", "app.py", "run.py", "VisitanteMiniC2.py"]
        for py_file in py_files:
            if py_file.name in priority_names:
                return py_file
        
        for py_file in py_files:
            if 'visitor' not in py_file.name.lower() and 'listener' not in py_file.name.lower():
                return py_file
        
        return py_files[0]
    
    def find_main_java(self):
        """Encontra o arquivo Java principal"""
        java_files = list(self.student_dir.glob("*.java"))
        for java_file in java_files:
            if java_file.name == "Main.java":
                return java_file
            try:
                with open(java_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'public static void main' in content:
                        return java_file
            except:
                pass
        return None
    
    def find_grammar_file(self):
        """Encontra o arquivo de gramática (.g ou .g4)"""
        for f in self.student_dir.glob("*.g*"):
            if f.suffix in ['.g', '.g4']:
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
    
    def compile_java_files(self):
        """Compila os arquivos Java"""
        java_files = list(self.student_dir.glob("*.java"))
        if not java_files:
            return False, "Nenhum arquivo Java encontrado"
        
        antlr_jar = self.student_dir / "antlr-4.13.2-complete.jar"
        if not antlr_jar.exists():
            return False, "ANTLR JAR não encontrado"
        
        try:
            cmd = ["javac", "-cp", str(antlr_jar)] + [str(f) for f in java_files]
            result = subprocess.run(cmd, cwd=self.student_dir, capture_output=True, text=True, timeout=60)
            
            if result.returncode != 0:
                return False, f"Erro na compilação Java:\n{result.stderr}"
            
            return True, "Compilado com sucesso"
        except FileNotFoundError:
            return False, "javac não encontrado."
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def detect_program_type(self, main_py):
        """Detecta o tipo de programa Python"""
        try:
            with open(main_py, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'sys.argv' in content and 'FileStream' in content:
                    return "arquivo"
                if 'sys.argv' in content:
                    return "argumento"
                if 'input(' in content:
                    return "interativo"
                return "argumento"
        except:
            return "desconhecido"
    
    def run_test(self, test_file):
        """Executa um teste específico"""
        test_path = Path("Testes") / test_file
        if not test_path.exists():
            return "Teste não encontrado", False
        
        main_py = self.find_main_py()
        main_java = self.find_main_java()
        
        if not main_py and not main_java:
            return "Nenhum arquivo Python ou Java encontrado", False
        
        original_dir = os.getcwd()
        os.chdir(self.student_dir)
        
        try:
            # COPIA O ARQUIVO PARA A PASTA DO ALUNO (mesmo nome)
            temp_test = self.student_dir / test_file
            shutil.copy(test_path, temp_test)
            
            output = None
            has_error = False
            
            # --- CASO JAVA ---
            if main_java:
                class_files = list(self.student_dir.glob("*.class"))
                if not class_files:
                    compiled, msg = self.compile_java_files()
                    if not compiled:
                        return f"Erro na compilação Java: {msg}", True
                
                class_name = main_java.stem
                cmd = ["java", "-cp", f".:{str(self.student_dir / 'antlr-4.13.2-complete.jar')}", class_name, test_file]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                output = result.stdout + result.stderr
                has_error = result.returncode != 0
            
            # --- CASO PYTHON ---
            elif main_py:
                program_type = self.detect_program_type(main_py)
                
                if program_type == "arquivo":
                    cmd = [sys.executable, str(main_py), test_file]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                    output = result.stdout + result.stderr
                    has_error = result.returncode != 0
                else:
                    cmd = [sys.executable, str(main_py), test_file]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                    output = result.stdout + result.stderr
                    has_error = result.returncode != 0
                    
                    if not output or "No such file" in output:
                        with open(temp_test, 'r', encoding='utf-8') as f:
                            content = f.read().strip()
                        cmd = [sys.executable, str(main_py), content]
                        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                        output = result.stdout + result.stderr
                        has_error = result.returncode != 0
            
            # Verifica se há erro na saída (sintático ou semântico)
            if output:
                output_lower = output.lower()
                error_keywords = ['erro', 'error', 'mismatched', 'extraneous', 'no viable', 'expecting']
                has_error_in_output = any(word in output_lower for word in error_keywords)
                has_error = has_error or has_error_in_output
            
            return output, has_error
            
        except subprocess.TimeoutExpired:
            return "Timeout (15s)", True
        except Exception as e:
            return f"Erro: {str(e)}", True
        finally:
            os.chdir(original_dir)
            try:
                if temp_test.exists():
                    temp_test.unlink()
            except:
                pass
    
    def grade_student(self):
        """Avalia o aluno em todos os testes"""
        print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}Avaliando: {self.student_name}{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        main_py = self.find_main_py()
        main_java = self.find_main_java()
        
        if not main_py and not main_java:
            print(f"{Colors.RED}✗ Nenhum arquivo Python ou Java encontrado{Colors.END}")
            self.update_nota_md_all_fail("Nenhum arquivo Python ou Java encontrado")
            return 0.0
        
        if main_py:
            print(f"  Arquivo Python: {main_py.name}")
        if main_java:
            print(f"  Arquivo Java: {main_java.name}")
        
        grammar_file = self.find_grammar_file()
        if not grammar_file:
            print(f"{Colors.RED}✗ Nenhum arquivo de gramática encontrado{Colors.END}")
            self.update_nota_md_all_fail("Arquivo de gramática não encontrado")
            return 0.0
        
        print(f"  Gramática: {grammar_file.name}")
        
        if main_py:
            print(f"\n{Colors.BOLD}Compilando gramática...{Colors.END}")
            compiled, msg = self.compile_grammar()
            if not compiled:
                print(f"{Colors.RED}✗ {msg}{Colors.END}")
                self.update_nota_md_all_fail(msg)
                return 0.0
            print(f"{Colors.GREEN}✓ {msg}{Colors.END}")
        
        if main_java:
            print(f"\n{Colors.BOLD}Compilando arquivos Java...{Colors.END}")
            compiled, msg = self.compile_java_files()
            if not compiled:
                print(f"{Colors.RED}✗ {msg}{Colors.END}")
                self.update_nota_md_all_fail(msg)
                return 0.0
            print(f"{Colors.GREEN}✓ {msg}{Colors.END}")
        
        tests = [
            ('teste1.c', True, 'Variável não declarada'),
            ('teste2.c', True, 'Redeclaração de variável'),
            ('teste3.c', True, 'Número de argumentos'),
            ('teste4.c', True, 'Tipos dos argumentos'),
            ('teste5.c', True, 'Compatibilidade de tipos'),
            ('teste6.c', True, 'Operandos int'),
            ('teste7.c', False, 'Válido (char + int)'),
            ('teste8.c', False, 'Válido (break/continue)'),
            ('teste9.c', True, 'Break/continue fora do while'),
            ('teste10.c', False, 'Válido')
        ]
        
        results = {}
        
        print(f"\n{Colors.BOLD}Executando testes...{Colors.END}")
        for i, (test_file, should_error, description) in enumerate(tests, 1):
            print(f"\n  {Colors.BOLD}Teste {i}:{Colors.END} {test_file} ({description})")
            
            output, has_error = self.run_test(test_file)
            
            if should_error:
                passed = has_error
                score = 1.0 if passed else 0.0
            else:
                passed = not has_error
                score = 1.0 if passed else 0.0
            
            if passed:
                print(f"    {Colors.GREEN}✓ Passou{Colors.END}")
            else:
                print(f"    {Colors.RED}✗ Falhou{Colors.END}")
                if output and len(output) > 0:
                    output_preview = output[:300].replace('\n', ' ').strip()
                    print(f"    Saída: {output_preview}...")
            
            results[f"teste_{i}"] = {
                "file": test_file,
                "should_error": should_error,
                "description": description,
                "passed": passed,
                "score": score,
                "output": output[:500] if output else ""
            }
        
        total_score = sum(r["score"] for r in results.values())
        print(f"\n{Colors.BOLD}Nota final: {total_score:.1f}/10.0{Colors.END}")
        
        self.update_nota_md(results)
        
        return total_score, results
    
    def update_nota_md_all_fail(self, error_msg):
        """Atualiza nota.md com todos os testes falhos"""
        nota_path = self.student_dir / "nota.md"
        
        content = f"""# Avaliação do trabalho 06 - Verificação de Variáveis, Tipos e Funções

### T1
Ponto: 0<br>

### T2
Ponto: 0<br>

### T3
Ponto: 0<br>

### T4
Ponto: 0<br>

### T5
Ponto: 0<br>

### T6
Ponto: 0<br>

### T7
Ponto: 0<br>

### T8
Ponto: 0<br>

### T9
Ponto: 0<br>

### T10
Ponto: 0<br>

## Nota Final: 0.0
"""
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def update_nota_md(self, results):
        """Atualiza o nota.md do aluno - preserva a estrutura original"""
        nota_path = self.student_dir / "nota.md"
        
        # Lê o conteúdo original completo
        if not nota_path.exists():
            print(f"{Colors.YELLOW}⚠ Arquivo nota.md não encontrado em {self.student_name}{Colors.END}")
            return
        
        with open(nota_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Processa linha por linha
        new_lines = []
        test_index = 1
        
        for line in lines:
            # Verifica se é uma linha "Ponto:" de um teste
            if "Ponto:" in line and not line.strip().startswith("##"):
                # Encontra qual teste é (pela ordem)
                if test_index <= 10:
                    key = f"teste_{test_index}"
                    if key in results:
                        r = results[key]
                        # Substitui a linha pelo valor correto
                        new_lines.append(f"Ponto: {r['score']:.1f}\n")
                        test_index += 1
                        continue
                # Se não encontrou o teste correspondente, mantém a linha original
                new_lines.append(line)
            else:
                new_lines.append(line)
        
        # Atualiza a nota final
        total = sum(r['score'] for r in results.values() if 'score' in r)
        for i, line in enumerate(new_lines):
            if "## Nota Final:" in line:
                new_lines[i] = f"## Nota Final: {total:.1f}\n"
                break
        
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)


def main():
    """Função principal"""
    base_dir = Path.cwd()
    
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Corretor Automático - Atividade 06 (Verificação de Variáveis, Tipos e Funções){Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    
    try:
        import pexpect
        print(f"{Colors.GREEN}✓ pexpect disponível{Colors.END}")
    except ImportError:
        print(f"{Colors.YELLOW}⚠ pexpect não instalado (opcional){Colors.END}")
    
    javac_available = shutil.which('javac') is not None
    if not javac_available:
        print(f"{Colors.YELLOW}⚠ javac não encontrado. Arquivos Java não serão compilados.{Colors.END}")
    
    alunos_dir = base_dir / "Alunos"
    if not alunos_dir.exists():
        print(f"{Colors.RED}✗ Pasta 'Alunos' não encontrada!{Colors.END}")
        return
    
    students = []
    for item in alunos_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            students.append(item)
    
    if not students:
        print(f"{Colors.YELLOW}Nenhum aluno encontrado na pasta Alunos.{Colors.END}")
        return
    
    print(f"\nEncontrados {len(students)} alunos")
    print("Iniciando correção...")
    print(f"Timeout por teste: {Colors.BOLD}15 segundos{Colors.END}\n")
    
    results = {}
    
    for student_dir in students:
        try:
            grader = MiniCGrader(student_dir)
            score, details = grader.grade_student()
            results[student_dir.name] = {
                "score": score,
                "details": details
            }
        except Exception as e:
            print(f"{Colors.RED}Erro ao avaliar {student_dir.name}: {e}{Colors.END}")
            results[student_dir.name] = {
                "score": 0.0,
                "details": {"error": str(e)}
            }
    
    # Gera CSV
    csv_file = base_dir / "notas_finais.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Aluno", "Nota Final", "Status"])
        
        for aluno, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
            score = data['score']
            status = "Aprovado" if score >= 5.0 else "Reprovado"
            writer.writerow([aluno, f"{score:.1f}", status])
    
    print(f"\n{Colors.CYAN}{'#'*80}{Colors.END}")
    print(f"{Colors.BOLD}RELATÓRIO FINAL{Colors.END}")
    print(f"{Colors.CYAN}{'#'*80}{Colors.END}\n")
    
    print(f"{'ALUNO':<35} {'NOTA':<8} {'STATUS':<10}")
    print("-" * 55)
    
    for aluno, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
        score = data['score']
        status = "Aprovado" if score >= 5.0 else "Reprovado"
        status_color = Colors.GREEN if score >= 5.0 else Colors.RED
        print(f"{aluno:<35} {score:<8.1f} {status_color}{status:<10}{Colors.END}")
    
    scores = [data['score'] for data in results.values()]
    if scores:
        print(f"\n{Colors.BOLD}ESTATÍSTICAS{Colors.END}")
        print(f"{'Média:':<35} {sum(scores)/len(scores):.1f}")
        print(f"{'Maior nota:':<35} {max(scores):.1f}")
        print(f"{'Menor nota:':<35} {min(scores):.1f}")
        print(f"{'Aprovados:':<35} {sum(1 for s in scores if s >= 5.0)}/{len(scores)}")
        print(f"{'Taxa de aprovação:':<35} {sum(1 for s in scores if s >= 5.0)/len(scores)*100:.0f}%")
    
    print(f"\nCSV: {csv_file}")


if __name__ == "__main__":
    main()