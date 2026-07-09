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

class MiniCIRGrader:
    def __init__(self, student_dir):
        self.student_dir = Path(student_dir)
        self.student_name = self.student_dir.name
        
    def find_main_py(self):
        """Encontra o arquivo Python principal"""
        py_files = list(self.student_dir.glob("*.py"))
        if not py_files:
            return None
        
        priority_names = ["main.py", "Principal.py", "principal.py", "app.py", "run.py", "PrincipalMiniC3.py"]
        for py_file in py_files:
            if py_file.name in priority_names:
                return py_file
        
        for py_file in py_files:
            if 'visitor' not in py_file.name.lower() and 'listener' not in py_file.name.lower():
                return py_file
        
        return py_files[0]
    
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
    
    def detect_extension(self, main_py):
        """Detecta qual extensão o programa do aluno espera (.c ou .mc)"""
        try:
            with open(main_py, 'r', encoding='utf-8') as f:
                content = f.read()
                if '.mc' in content and 'open(' in content:
                    return '.mc'
                if 'sys.argv' in content:
                    if '.c' in content and '.mc' not in content:
                        return '.c'
                    return '.c'
                return '.c'
        except:
            return '.c'
    
    def copy_test_files(self):
        """Copia todos os arquivos .c da pasta Testes para a pasta do aluno e também como .mc"""
        testes_dir = Path("Testes")
        if not testes_dir.exists():
            print(f"{Colors.RED}✗ Pasta Testes não encontrada!{Colors.END}")
            return False
        
        copied = 0
        for test_file in testes_dir.glob("*.c"):
            dest_c = self.student_dir / test_file.name
            shutil.copy(test_file, dest_c)
            
            mc_name = test_file.stem + '.mc'
            dest_mc = self.student_dir / mc_name
            shutil.copy(test_file, dest_mc)
            
            copied += 1
        
        if copied == 0:
            print(f"{Colors.YELLOW}⚠ Nenhum arquivo .c encontrado em Testes/{Colors.END}")
            return False
        
        return True
    
    def find_generated_file(self, test_file, main_py):
        """Procura por arquivo gerado na pasta do aluno"""
        base_name = test_file.rsplit('.', 1)[0]
        
        extensions = ['.tac', '.3addr', '.ir', '.txt', '.out', '.interm', '.il', '.3ac']
        
        for e in extensions:
            gen_file = self.student_dir / f"{base_name}{e}"
            if gen_file.exists():
                return gen_file
            
            gen_file = self.student_dir / f"{base_name}_tac{e}"
            if gen_file.exists():
                return gen_file
            
            gen_file = self.student_dir / f"{base_name}_erro{e}"
            if gen_file.exists():
                return gen_file
            
            gen_file = self.student_dir / f"{base_name}_3ac{e}"
            if gen_file.exists():
                return gen_file
        
        output_file = self.student_dir / "output.3ac"
        if output_file.exists():
            return output_file
        
        for f in self.student_dir.iterdir():
            if f.is_file() and base_name in f.name and f.suffix not in ['.c', '.py', '.g4', '.g', '.mc']:
                return f
        
        return None
    
    def run_test(self, test_file, main_py, ext):
        """Executa um teste específico com a extensão correta"""
        base_name = test_file.rsplit('.', 1)[0]
        file_with_ext = f"{base_name}{ext}"
        
        temp_test = self.student_dir / file_with_ext
        if not temp_test.exists():
            return "Arquivo não encontrado", False, None
        
        original_dir = os.getcwd()
        os.chdir(self.student_dir)
        
        try:
            output = None
            has_error = False
            
            cmd = [sys.executable, str(main_py), file_with_ext]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            output = result.stdout + result.stderr
            has_error = result.returncode != 0
            
            if not output or "No such file" in output:
                cmd = [sys.executable, str(main_py), str(temp_test)]
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
            
            if output:
                output_lower = output.lower()
                error_keywords = ['erro', 'error', 'mismatched', 'extraneous', 'no viable', 'expecting']
                has_error_in_output = any(word in output_lower for word in error_keywords)
                has_error = has_error or has_error_in_output
            
            gen_file = self.find_generated_file(test_file, main_py)
            
            return output, has_error, gen_file
            
        except subprocess.TimeoutExpired:
            return "Timeout (15s)", True, None
        except Exception as e:
            return f"Erro: {str(e)}", True, None
        finally:
            os.chdir(original_dir)
    
    def grade(self):
        """Avalia o aluno"""
        print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}Avaliando: {self.student_name}{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        main_py = self.find_main_py()
        if not main_py:
            print(f"{Colors.RED}✗ Nenhum arquivo Python encontrado{Colors.END}")
            return 0.0
        
        print(f"  Arquivo Python: {main_py.name}")
        
        # COMPILA A GRAMÁTICA
        grammar_file = self.find_grammar_file()
        if grammar_file:
            print(f"  Gramática: {grammar_file.name}")
            print(f"\n{Colors.BOLD}Compilando gramática...{Colors.END}")
            compiled, msg = self.compile_grammar()
            if not compiled:
                print(f"{Colors.RED}✗ {msg}{Colors.END}")
                # Mesmo com erro na compilação, continua para tentar executar
            else:
                print(f"{Colors.GREEN}✓ {msg}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}⚠ Nenhum arquivo de gramática encontrado{Colors.END}")
        
        ext = self.detect_extension(main_py)
        print(f"  Extensão detectada: {ext}")
        
        print(f"\n{Colors.BOLD}Copiando arquivos de teste...{Colors.END}")
        if not self.copy_test_files():
            print(f"{Colors.RED}✗ Falha ao copiar arquivos de teste{Colors.END}")
            return 0.0
        print(f"{Colors.GREEN}✓ Arquivos de teste copiados (.c e .mc){Colors.END}")
        
        tests = [
            ('test1.c', 'Declaração de variável'),
            ('test2.c', 'Declaração múltipla'),
            ('test3.c', 'Return'),
            ('test4.c', 'Chamada de função com char'),
            ('test5.c', 'Multiplicação'),
            ('test6.c', 'If-else'),
            ('test7.c', 'While com incremento'),
            ('test8.c', 'Atribuição composta'),
            ('test9.c', 'Função vazia'),
            ('test10.c', 'Operadores unários')
        ]
        
        test_scores = []
        results = {}
        
        print(f"\n{Colors.BOLD}Executando testes...{Colors.END}")
        
        for i, (test_file, description) in enumerate(tests, 1):
            print(f"\n  {Colors.BOLD}Teste {i}:{Colors.END} {test_file} ({description})")
            
            base_name = test_file.rsplit('.', 1)[0]
            file_with_ext = f"{base_name}{ext}"
            
            temp_test = self.student_dir / file_with_ext
            if not temp_test.exists():
                print(f"    {Colors.RED}✗ Arquivo não encontrado: {file_with_ext}{Colors.END}")
                test_scores.append(0.0)
                results[f"teste_{i}"] = {"score": 0.0}
                continue
            
            output, has_error, gen_file = self.run_test(test_file, main_py, ext)
            
            if gen_file:
                score = 1.0
                print(f"    {Colors.GREEN}✓ Passou{Colors.END} - Gerou: {gen_file.name}")
            elif not has_error and output:
                if any(keyword in output.lower() for keyword in ['t1', 't2', '=', '+', '-', '*', '/']):
                    score = 0.8
                    print(f"    {Colors.GREEN}✓ Passou{Colors.END} - Gerou código na saída")
                else:
                    score = 0.5
                    print(f"    {Colors.YELLOW}⚠ Parcial{Colors.END} - Executou sem erros mas sem código")
            else:
                score = 0.3
                print(f"    {Colors.RED}✗ Falhou{Colors.END}")
                if output and len(output) > 0:
                    output_preview = output[:200].replace('\n', ' ').strip()
                    print(f"    Saída: {output_preview}...")
            
            test_scores.append(score)
            results[f"teste_{i}"] = {"score": score}
        
        total_score = sum(test_scores)
        base_bonus = 0.0
        if main_py:
            base_bonus += 0.5
        if grammar_file:
            base_bonus += 0.5
        
        final_score = min(10.0, total_score + base_bonus)
        
        print(f"\n{Colors.BOLD}Nota final: {final_score:.1f}/10.0{Colors.END}")
        if final_score >= 8.0:
            print(f"  {Colors.GREEN}🎉 Parabéns! Trabalho muito bom!{Colors.END}")
        elif final_score >= 5.0:
            print(f"  {Colors.YELLOW}👍 Trabalho aceito!{Colors.END}")
        else:
            print(f"  {Colors.RED}⚠ Precisa revisar o trabalho.{Colors.END}")
        
        self.update_nota_md(results, final_score)
        
        return final_score
    
    def update_nota_md(self, results, final_score):
        """Atualiza o nota.md do aluno - preserva a estrutura original"""
        nota_path = self.student_dir / "nota.md"
        
        if not nota_path.exists():
            print(f"{Colors.YELLOW}⚠ Arquivo nota.md não encontrado em {self.student_name}{Colors.END}")
            return
        
        with open(nota_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        test_index = 1
        
        for line in lines:
            if "Ponto:" in line and "## Nota Final:" not in line and "Observação:" not in line:
                if test_index <= 10:
                    key = f"teste_{test_index}"
                    if key in results:
                        r = results[key]
                        new_lines.append(f"Ponto: {r['score']:.1f}\n")
                        test_index += 1
                        continue
                new_lines.append(line)
            else:
                new_lines.append(line)
        
        for i, line in enumerate(new_lines):
            if "## Nota Final:" in line:
                new_lines[i] = f"## Nota Final: {final_score:.1f}\n"
                break
        
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)


def main():
    """Função principal"""
    base_dir = Path.cwd()
    
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Corretor Automático - Atividade 07 (Representação Intermediária){Colors.END}")
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
    print("Copiando todos os testes .c e .mc para cada aluno...")
    print(f"Timeout por teste: {Colors.BOLD}15 segundos{Colors.END}")
    print(f"Critério: {Colors.BOLD}Generoso{Colors.END} - bônus por arquivos e geração de código\n")
    
    results = {}
    
    for student_dir in students:
        try:
            grader = MiniCIRGrader(student_dir)
            score = grader.grade()
            results[student_dir.name] = score
        except Exception as e:
            print(f"{Colors.RED}Erro ao avaliar {student_dir.name}: {e}{Colors.END}")
            results[student_dir.name] = 0.0
    
    # Gera CSV
    csv_file = base_dir / "notas_finais.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Aluno", "Nota Final", "Status"])
        
        for aluno, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
            status = "Aprovado" if score >= 5.0 else "Reprovado"
            writer.writerow([aluno, f"{score:.1f}", status])
    
    # Relatório final
    print(f"\n{Colors.CYAN}{'#'*80}{Colors.END}")
    print(f"{Colors.BOLD}RELATÓRIO FINAL{Colors.END}")
    print(f"{Colors.CYAN}{'#'*80}{Colors.END}\n")
    
    print(f"{'ALUNO':<35} {'NOTA':<8} {'STATUS':<10}")
    print("-" * 55)
    
    for aluno, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
        status = "Aprovado" if score >= 5.0 else "Reprovado"
        status_color = Colors.GREEN if score >= 5.0 else Colors.RED
        print(f"{aluno:<35} {score:<8.1f} {status_color}{status:<10}{Colors.END}")
    
    scores = list(results.values())
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