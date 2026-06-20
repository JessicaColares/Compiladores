import os
import subprocess
import shutil
import sys
import re
import time
import signal
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

class ExpressionGrader:
    def __init__(self, student_dir):
        self.student_dir = Path(student_dir)
        self.student_name = self.student_dir.name
        
    def find_main_py(self):
        """Encontra o arquivo Python principal"""
        py_files = list(self.student_dir.glob("*.py"))
        if not py_files:
            return None
        
        priority_names = ["main.py", "Principal.py", "principal.py", "app.py", "run.py", "calc.py"]
        for py_file in py_files:
            if py_file.name in priority_names:
                return py_file
        
        for py_file in py_files:
            if 'listener' not in py_file.name.lower() and 'visitor' not in py_file.name.lower():
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
    
    def extract_number(self, text):
        """Extrai o primeiro número (inteiro ou float) da saída"""
        patterns = [
            r'[-+]?\d+\.\d+',
            r'[-+]?\d+',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            if matches:
                last_match = matches[-1]
                if '.' in last_match:
                    return float(last_match)
                return int(last_match)
        
        return None
    
    def detect_program_type(self, main_py):
        """Detecta o tipo de programa Python"""
        try:
            with open(main_py, 'r', encoding='utf-8') as f:
                content = f.read()
                if '.txt' in content and 'open(' in content:
                    return "arquivo"
                if 'input(' in content and 'while' in content:
                    return "interativo"
                if 'expression = ' in content and 'input' not in content:
                    return "fixo"
                if 'sys.argv' in content:
                    return "argumento"
                return "argumento"
        except:
            return "desconhecido"
    
    def run_interactive_test_pexpect(self, cmd, expression, timeout=5):
        """Tenta usar pexpect para programas interativos"""
        try:
            import pexpect
            import pexpect.popen_spawn
            
            child = pexpect.popen_spawn.PopenSpawn(cmd, timeout=timeout)
            child.expect(['> ', pexpect.EOF, pexpect.TIMEOUT], timeout=2)
            child.sendline(expression)
            child.expect(['> ', pexpect.EOF, pexpect.TIMEOUT], timeout=timeout)
            output = child.before.decode('utf-8', errors='ignore')
            child.terminate(force=True)
            return output, None
        except ImportError:
            return None, "pexpect não instalado"
        except Exception as e:
            return None, f"Erro no pexpect: {str(e)}"
    
    def run_interactive_test_stdin(self, cmd, expression, timeout=5):
        """Abordagem padrão com stdin"""
        process = None
        try:
            process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            
            time.sleep(0.3)
            process.stdin.write(expression + '\n')
            process.stdin.flush()
            time.sleep(0.3)
            
            try:
                stdout, stderr = process.communicate(timeout=timeout)
                return stdout + stderr, None
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
                return None, f"Timeout após {timeout}s"
                
        except Exception as e:
            if process and process.poll() is None:
                try:
                    process.kill()
                    process.wait()
                except:
                    pass
            return None, f"Erro: {str(e)}"
        finally:
            if process and process.poll() is None:
                try:
                    process.kill()
                    process.wait()
                except:
                    pass
    
    def run_interactive_test(self, cmd, expression, timeout=5):
        """Tenta várias abordagens para programas interativos"""
        output, error = self.run_interactive_test_pexpect(cmd, expression, timeout)
        if output is not None:
            return output, None
        return self.run_interactive_test_stdin(cmd, expression, timeout)
    
    def run_test(self, expression, expected_value):
        """Executa um teste com a expressão fornecida"""
        main_java = self.find_main_java()
        main_py = self.find_main_py()
        
        if not main_py and not main_java:
            return None, "Nenhum arquivo Python ou Java encontrado"
        
        original_dir = os.getcwd()
        os.chdir(self.student_dir)
        
        try:
            output = None
            method = None
            error = None
            
            # --- CASO JAVA ---
            if main_java:
                class_files = list(self.student_dir.glob("*.class"))
                if not class_files:
                    compiled, msg = self.compile_java_files()
                    if not compiled:
                        return None, f"Erro na compilação Java: {msg}"
                
                class_name = main_java.stem
                try:
                    cmd = ["java", "-cp", f".:{str(self.student_dir / 'antlr-4.13.2-complete.jar')}", class_name]
                    result_output, error = self.run_interactive_test(cmd, expression, timeout=5)
                    if result_output is not None:
                        output = result_output
                        method = "java_interativo"
                except Exception as e:
                    return None, f"Erro ao executar Java: {str(e)}"
            
            # --- CASO PYTHON ---
            elif main_py:
                program_type = self.detect_program_type(main_py)
                cmd = [sys.executable, str(main_py)]
                
                # --- CASO ARQUIVO .TXT ---
                if program_type == "arquivo":
                    try:
                        temp_file = self.student_dir / "temp_expressao.txt"
                        with open(temp_file, 'w', encoding='utf-8') as f:
                            f.write(expression + '\n')
                        
                        cmd_arg = [sys.executable, str(main_py), str(temp_file)]
                        result_output, error = self.run_test_with_timeout(cmd_arg, timeout=5)
                        
                        if temp_file.exists():
                            temp_file.unlink()
                        
                        if result_output is not None and self.extract_number(result_output) is not None:
                            output = result_output
                            method = "arquivo"
                    except Exception as e:
                        if temp_file.exists():
                            temp_file.unlink()
                        return None, f"Erro no modo arquivo: {str(e)}"
                
                # --- CASO INTERATIVO ---
                elif program_type == "interativo":
                    result_output, error = self.run_interactive_test(cmd, expression, timeout=5)
                    if result_output is not None and self.extract_number(result_output) is not None:
                        output = result_output
                        method = "interativo"
                    else:
                        return None, error
                
                # --- CASO ARGUMENTO ---
                else:
                    try:
                        cmd_arg = [sys.executable, str(main_py), expression]
                        result_output, error = self.run_test_with_timeout(cmd_arg, timeout=5)
                        if result_output is not None and self.extract_number(result_output) is not None:
                            output = result_output
                            method = "argumento"
                    except:
                        pass
                    
                    if output is None or self.extract_number(output) is None:
                        try:
                            result_output, error = self.run_interactive_test(cmd, expression, timeout=5)
                            if result_output is not None and self.extract_number(result_output) is not None:
                                output = result_output
                                method = "interativo"
                        except:
                            pass
                    
                    if output is None or self.extract_number(output) is None:
                        try:
                            cmd_arg = [sys.executable, str(main_py), f'"{expression}"']
                            result_output, error = self.run_test_with_timeout(cmd_arg, timeout=5)
                            if result_output is not None and self.extract_number(result_output) is not None:
                                output = result_output
                                method = "argumento_com_aspas"
                        except:
                            pass
            
            if output is None:
                if error:
                    return None, error
                return None, "Não foi possível executar o programa"
            
            result_value = self.extract_number(output)
            if result_value is None:
                return None, f"Saída sem número: {output[:100]}"
            
            if isinstance(expected_value, float) or isinstance(result_value, float):
                passed = abs(float(expected_value) - float(result_value)) < 0.01
            else:
                passed = result_value == expected_value
            
            return {
                "output": output.strip(),
                "result": result_value,
                "expected": expected_value,
                "passed": passed,
                "method": method
            }, None
            
        except Exception as e:
            return None, f"Erro geral: {str(e)}"
        finally:
            os.chdir(original_dir)
    
    def run_test_with_timeout(self, cmd, timeout=5):
        """Executa um comando simples com timeout"""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.stdout + result.stderr, None
        except subprocess.TimeoutExpired:
            return None, f"Timeout após {timeout}s"
        except Exception as e:
            return None, f"Erro: {str(e)}"
    
    def grade_student(self):
        """Avalia o aluno em todos os testes"""
        print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}Avaliando: {self.student_name}{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        main_py = self.find_main_py()
        main_java = self.find_main_java()
        
        if not main_py and not main_java:
            print(f"{Colors.RED}✗ Nenhum arquivo encontrado{Colors.END}")
            self.update_nota_md_with_error("Nenhum arquivo Python ou Java encontrado")
            return 0.0, {}
        
        if main_py:
            print(f"  Arquivo Python: {main_py.name}")
            compiled, msg = self.compile_grammar()
            if not compiled:
                print(f"{Colors.RED}✗ {msg}{Colors.END}")
                self.update_nota_md_with_compilation_error(msg)
                return 0.0, {}
            print(f"{Colors.GREEN}✓ Gramática compilada com sucesso{Colors.END}")
        
        if main_java:
            print("✓ Arquivos Java encontrados")
            class_files = list(self.student_dir.glob("*.class"))
            if not class_files:
                print("  Compilando arquivos Java...")
                compiled, msg = self.compile_java_files()
                if not compiled:
                    print(f"{Colors.RED}✗ {msg}{Colors.END}")
                    self.update_nota_md_with_compilation_error(msg)
                    return 0.0, {}
                print(f"{Colors.GREEN}✓ Arquivos Java compilados{Colors.END}")
        
        tests = [
            ("(5*4)", 20),
            ("2 + 3", 5),
            ("abs(-10)", 10),
            ("-9/3", -3),
            ("3.5 * (2 + 1)", 10.5),
            ("-15 + 20", 5),
            ("(2^3)^2", 64),
            ("abs(fat(3))", 6),
            ("(2+3)*(4-1)", 15),
            ("fat(abs(-5))", 120)
        ]
        
        results = {}
        loop_detected = False
        
        print("\n--- Executando Testes ---")
        for i, (expression, expected) in enumerate(tests, 1):
            print(f"\n{Colors.BOLD}Teste {i}:{Colors.END} {expression}")
            print(f"  Esperado: {expected}")
            
            result, error = self.run_test(expression, expected)
            
            if error and "Timeout" in error:
                loop_detected = True
                print(f"  {Colors.YELLOW}⚠ LOOP DETECTADO! {error}{Colors.END}")
            
            if result is None:
                print(f"  {Colors.RED}✗ Erro: {error}{Colors.END}")
                results[f"teste_{i}"] = {
                    "expression": expression,
                    "expected": expected,
                    "passed": False,
                    "score": 0.0,
                    "obs": None,
                    "output": None,
                    "result": None,
                    "error": error
                }
            else:
                passed = result["passed"]
                score = 1.0 if passed else 0.0
                
                status = f"{Colors.GREEN}✓ Passou{Colors.END}" if passed else f"{Colors.RED}✗ Falhou{Colors.END}"
                print(f"  Resultado: {result['result']} - {status}")
                print(f"  Método: {result['method']}")
                
                results[f"teste_{i}"] = {
                    "expression": expression,
                    "expected": expected,
                    "passed": passed,
                    "score": score,
                    "obs": None,
                    "output": result["output"],
                    "result": result["result"],
                    "method": result["method"],
                    "error": None
                }
        
        total_score = sum(r["score"] for r in results.values())
        print(f"\n{Colors.BOLD}Nota final: {total_score:.1f}/10.0{Colors.END}")
        
        if loop_detected:
            print(f"  {Colors.YELLOW}⚠ ALERTA: Loops infinitos detectados!{Colors.END}")
        
        self.update_nota_md(results)
        
        return total_score, results
    
    def update_nota_md_with_compilation_error(self, error_msg):
        """Atualiza o nota.md com erro de compilação"""
        nota_path = self.student_dir / "nota.md"
        
        original_content = ""
        if nota_path.exists():
            with open(nota_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        
        observations = {}
        for i in range(1, 11):
            pattern = rf"### Teste {i}:\s*\n.*?\nObservação: (.*?)(?:\n|$)"
            match = re.search(pattern, original_content, re.DOTALL)
            if match:
                observations[i] = match.group(1).strip()
            else:
                observations[i] = "Valor esperado: [ver nota.md original]"
        
        content = """## Aceitação:

"""
        
        for i in range(1, 11):
            obs = observations.get(i, "Valor esperado: [ver nota.md original]")
            obs = f"{obs} (erro: {error_msg})"
            content += f"""### Teste {i}:
Ponto: 0<br>
Observação: {obs}<br>

"""
        
        consideracoes = ""
        match = re.search(r"## Considerações:\s*\n(.*?)(?:\n## Nota Final:|$)", original_content, re.DOTALL)
        if match:
            consideracoes = match.group(1).strip()
        
        content += f"""## Considerações:
{consideracoes}

## Nota Final: 0.0
"""
        
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def update_nota_md_with_error(self, error_msg):
        """Atualiza o nota.md com erro"""
        nota_path = self.student_dir / "nota.md"
        
        original_content = ""
        if nota_path.exists():
            with open(nota_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        
        observations = {}
        for i in range(1, 11):
            pattern = rf"### Teste {i}:\s*\n.*?\nObservação: (.*?)(?:\n|$)"
            match = re.search(pattern, original_content, re.DOTALL)
            if match:
                observations[i] = match.group(1).strip()
            else:
                observations[i] = "Valor esperado: [ver nota.md original]"
        
        content = """## Aceitação:

"""
        
        for i in range(1, 11):
            obs = observations.get(i, "Valor esperado: [ver nota.md original]")
            obs = f"{obs} (erro: {error_msg})"
            content += f"""### Teste {i}:
Ponto: 0<br>
Observação: {obs}<br>

"""
        
        consideracoes = ""
        match = re.search(r"## Considerações:\s*\n(.*?)(?:\n## Nota Final:|$)", original_content, re.DOTALL)
        if match:
            consideracoes = match.group(1).strip()
        
        content += f"""## Considerações:
{consideracoes}

## Nota Final: 0.0
"""
        
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def update_nota_md(self, results):
        """Atualiza o nota.md do aluno"""
        nota_path = self.student_dir / "nota.md"
        
        original_content = ""
        if nota_path.exists():
            with open(nota_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        
        observations = {}
        for i in range(1, 11):
            pattern = rf"### Teste {i}:\s*\n.*?\nObservação: (.*?)(?:\n|$)"
            match = re.search(pattern, original_content, re.DOTALL)
            if match:
                observations[i] = match.group(1).strip()
            else:
                observations[i] = "Valor esperado: [ver nota.md original]"
        
        content = """## Aceitação:

"""
        
        for i in range(1, 11):
            key = f"teste_{i}"
            if key in results:
                r = results[key]
                obs = observations.get(i, "Valor esperado: [ver nota.md original]")
                
                if r.get('error') and "Timeout" in r['error']:
                    obs = f"{obs} (loop infinito detectado)"
                elif r.get('method') == "fixo":
                    obs = f"{obs} (programa com expressão fixa)"
                elif r.get('method') == "arquivo":
                    obs = f"{obs} (programa lê arquivo .txt)"
                
                content += f"""### Teste {i}:
Ponto: {r['score']:.1f}<br>
Observação: {obs}<br>

"""
            else:
                obs = observations.get(i, "Valor esperado: [ver nota.md original]")
                content += f"""### Teste {i}:
Ponto: 0<br>
Observação: {obs}<br>

"""
        
        consideracoes = ""
        match = re.search(r"## Considerações:\s*\n(.*?)(?:\n## Nota Final:|$)", original_content, re.DOTALL)
        if match:
            consideracoes = match.group(1).strip()
        
        loops_detected = any(
            r.get('error') and "Timeout" in r['error'] 
            for r in results.values() 
            if isinstance(r, dict)
        )
        
        if loops_detected:
            consideracoes = f"{consideracoes}\n\n⚠️ Foram detectados loops infinitos em alguns testes."
        
        content += f"""## Considerações:
{consideracoes}

## Nota Final: {sum(r['score'] for r in results.values() if 'score' in r):.1f}
"""
        
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.write(content)


def main():
    """Função principal"""
    base_dir = Path.cwd()
    
    try:
        import pexpect
        print(f"{Colors.GREEN}✓ pexpect disponivel{Colors.END}")
    except ImportError:
        print(f"{Colors.YELLOW}⚠ pexpect não instalado. Para melhor experiência: pip install pexpect{Colors.END}")
    
    javac_available = shutil.which('javac') is not None
    if not javac_available:
        print(f"{Colors.YELLOW}⚠ javac não encontrado. Arquivos Java não serão compilados.{Colors.END}")
    
    students = []
    for item in base_dir.iterdir():
        if item.is_dir() and item.name not in ["Testes", ".git", "__pycache__"] and not item.name.startswith('.'):
            students.append(item)
    
    print(f"Encontrados {len(students)} alunos")
    print("Iniciando correção...")
    print(f"Timeout por teste: {Colors.BOLD}5 segundos{Colors.END}\n")
    
    results = {}
    total_loops = 0
    
    for student_dir in students:
        try:
            grader = ExpressionGrader(student_dir)
            score, details = grader.grade_student()
            results[student_dir.name] = {
                "score": score,
                "details": details
            }
            
            if details:
                for key, value in details.items():
                    if isinstance(value, dict) and value.get('error') and "Timeout" in value['error']:
                        total_loops += 1
                        
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
        writer.writerow(["Aluno", "Nota Final", "Status", "Loops"])
        
        for aluno, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
            score = data['score']
            status = "Aprovado" if score >= 6.0 else "Reprovado"
            
            loops = 0
            if data.get('details'):
                for key, value in data['details'].items():
                    if isinstance(value, dict) and value.get('error') and "Timeout" in value['error']:
                        loops += 1
            
            writer.writerow([aluno, f"{score:.1f}", status, loops])
    
    # Relatório
    print(f"\n{Colors.CYAN}{'#'*80}{Colors.END}")
    print(f"{Colors.BOLD}RELATÓRIO FINAL{Colors.END}")
    print(f"{Colors.CYAN}{'#'*80}{Colors.END}\n")
    
    print(f"{'ALUNO':<35} {'NOTA':<8} {'STATUS':<10} {'LOOPS'}")
    print("-" * 65)
    
    for aluno, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
        score = data['score']
        status = "Aprovado" if score >= 6.0 else "Reprovado"
        
        status_color = Colors.GREEN if score >= 6.0 else Colors.RED
        
        loops = 0
        if data.get('details'):
            for key, value in data['details'].items():
                if isinstance(value, dict) and value.get('error') and "Timeout" in value['error']:
                    loops += 1
        
        print(f"{aluno:<35} {score:<8.1f} {status_color}{status:<10}{Colors.END} {loops}")
    
    scores = [data['score'] for data in results.values()]
    if scores:
        print(f"\n{Colors.BOLD}ESTATÍSTICAS{Colors.END}")
        print(f"{'Média:':<35} {sum(scores)/len(scores):.1f}")
        print(f"{'Maior:':<35} {max(scores):.1f}")
        print(f"{'Menor:':<35} {min(scores):.1f}")
        print(f"{'Aprovados:':<35} {sum(1 for s in scores if s >= 6.0)}/{len(scores)}")
        print(f"{'Taxa:':<35} {sum(1 for s in scores if s >= 6.0)/len(scores)*100:.0f}%")
        print(f"{'Total loops:':<35} {total_loops}")
    
    print(f"\nCSV: {csv_file}")


if __name__ == "__main__":
    main()