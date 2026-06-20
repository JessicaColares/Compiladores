import os
import subprocess
import shutil
import sys
import re
from pathlib import Path
import csv

class MiniCGrader:
    def __init__(self, student_dir):
        self.student_dir = Path(student_dir)
        self.student_name = self.student_dir.name
        self.antlr_jar = self.student_dir / "antlr-4.13.2-complete.jar"
        
    def find_grammar_file(self):
        """Encontra o arquivo de gramática (.g ou .g4)"""
        for f in self.student_dir.glob("*.g*"):
            if f.suffix in ['.g', '.g4']:
                return f
        return None
    
    def find_main_py(self):
        """Encontra o arquivo Python principal"""
        py_files = list(self.student_dir.glob("*.py"))
        if not py_files:
            return None
        
        # Prioriza main.py, depois qualquer outro que não seja visitor
        for py_file in py_files:
            if py_file.name == "main.py":
                return py_file
        
        for py_file in py_files:
            if 'visitor' not in py_file.name.lower() and 'listener' not in py_file.name.lower():
                return py_file
        
        return py_files[0]
    
    def compile_grammar(self):
        """Compila a gramática com ANTLR"""
        grammar_file = self.find_grammar_file()
        if not grammar_file:
            return False, "Arquivo de gramática não encontrado"
        
        if not self.antlr_jar.exists():
            return False, "ANTLR JAR não encontrado"
        
        try:
            cmd = [
                "java", "-jar", str(self.antlr_jar),
                "-Dlanguage=Python3", "-visitor", "-listener",
                str(grammar_file)
            ]
            result = subprocess.run(cmd, cwd=self.student_dir, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                return False, f"Erro na compilação: {result.stderr}"
            
            return True, "Compilado com sucesso"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def run_test(self, test_file, test_type):
        """Executa um teste específico"""
        test_path = Path("Testes") / test_type / test_file
        if not test_path.exists():
            return "Teste não encontrado", False
        
        main_py = self.find_main_py()
        if not main_py:
            return "Nenhum arquivo Python encontrado", False
        
        # Copia o teste para a pasta do aluno
        temp_test = self.student_dir / test_file
        shutil.copy(test_path, temp_test)
        
        original_dir = os.getcwd()
        os.chdir(self.student_dir)
        
        try:
            cmd = [sys.executable, str(main_py), str(temp_test)]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            output = result.stdout + result.stderr
            has_error = result.returncode != 0 or "error" in output.lower() or "erro" in output.lower()
            return output, has_error
        except subprocess.TimeoutExpired:
            return "Timeout", True
        except Exception as e:
            return f"Erro: {str(e)}", True
        finally:
            os.chdir(original_dir)
            if temp_test.exists():
                temp_test.unlink()
    
    def grade_student(self):
        """Avalia o aluno em todos os testes"""
        print(f"\n{'='*60}")
        print(f"Avaliando: {self.student_name}")
        print(f"{'='*60}")
        
        # Primeiro, compila a gramática
        compiled, msg = self.compile_grammar()
        if not compiled:
            print(f"✗ {msg}")
            self.update_nota_md(all_fail=True)
            return 0.0, {}
        
        print("✓ Gramática compilada com sucesso")
        
        # Testes de aceitação (devem passar sem erro)
        acceptance_tests = [
            "teste1.c", "teste2.c", "teste3.c", "teste4.c", "teste5.c",
            "teste6.c", "teste7.c", "teste8.c", "teste9.c", "teste10.c"
        ]
        
        # Testes de rejeição (devem dar erro)
        rejection_tests = [
            "teste1.c", "teste2.c", "teste3.c", "teste4.c", "teste5.c",
            "teste6.c", "teste7.c", "teste8.c", "teste9.c", "teste10.c"
        ]
        
        results = {}
        
        # Executa testes de aceitação
        print("\n--- Testes de Aceitação ---")
        for i, test_file in enumerate(acceptance_tests, 1):
            output, has_error = self.run_test(test_file, "Aceitacao")
            
            # Para aceitação: esperamos que NÃO tenha erro
            passed = not has_error
            score = 0.5 if passed else 0.0
            obs = "certo" if passed else "não atingiu o resultado esperado"
            
            results[f"aceitacao_{i}"] = {
                "file": test_file,
                "passed": passed,
                "score": score,
                "obs": obs,
                "output": output[:200]
            }
            
            status = "✓" if passed else "✗"
            print(f"  {status} {test_file}: {score:.1f} - {obs}")
        
        # Executa testes de rejeição
        print("\n--- Testes de Rejeição ---")
        for i, test_file in enumerate(rejection_tests, 1):
            output, has_error = self.run_test(test_file, "Rejeicao")
            
            # Para rejeição: esperamos que TENHA erro
            passed = has_error
            score = 0.5 if passed else 0.0
            obs = "certo" if passed else "não atingiu o resultado esperado"
            
            results[f"rejeicao_{i}"] = {
                "file": test_file,
                "passed": passed,
                "score": score,
                "obs": obs,
                "output": output[:200]
            }
            
            status = "✓" if passed else "✗"
            print(f"  {status} {test_file}: {score:.1f} - {obs}")
        
        # Calcula nota final
        total_score = sum(r["score"] for r in results.values())
        print(f"\nNota final: {total_score:.1f}/10.0")
        
        # Atualiza o nota.md do aluno
        self.update_nota_md(results)
        
        return total_score, results
    
    def update_nota_md(self, results):
        """Atualiza o arquivo nota.md do aluno"""
        nota_path = self.student_dir / "nota.md"
        
        if results == "all_fail" or (isinstance(results, dict) and "all_fail" in results):
            # Caso de falha na compilação
            content = """# Avaliação 02: Análise sintática da Linguagem MiniC

## Aceitação:

### Teste 1:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 2:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 3:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 4:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 5:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 6:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 7:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 8:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 9:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 10:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

## Rejeição:

### Teste 1:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 2:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 3:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 4:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 5:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 6:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 7:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 8:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 9:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

### Teste 10:
Ponto: 0<br>
Observação: erro na compilação da gramática<br>

## Considerações:
Gramática não compilou corretamente.

## Nota Final: 0.0
"""
            with open(nota_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return
        
        # Caso normal com resultados
        content = """# Avaliação 02: Análise sintática da Linguagem MiniC

## Aceitação:

"""
        
        # Adiciona resultados de aceitação
        for i in range(1, 11):
            key = f"aceitacao_{i}"
            if key in results:
                r = results[key]
                content += f"""### Teste {i}:

Ponto: {r['score']:.1f}<br>
Observação: {r['obs']}<br>

"""
            else:
                content += f"""### Teste {i}:
Ponto: 0<br>
Observação: não executado<br>

"""
        
        content += "## Rejeição:\n\n"
        
        # Adiciona resultados de rejeição
        for i in range(1, 11):
            key = f"rejeicao_{i}"
            if key in results:
                r = results[key]
                content += f"""### Teste {i}:


Ponto: {r['score']:.1f}<br>
Observação: {r['obs']}<br>

"""
            else:
                content += f"""### Teste {i}:
Ponto: 0<br>
Observação: não executado<br>

"""
        
        # Adiciona considerações e nota final
        total = sum(r['score'] for r in results.values() if 'score' in r)
        content += f"""## Considerações:
Testes automatizados executados.

## Nota Final: {total:.1f}
"""
        
        with open(nota_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _get_test_content(self, test_num, test_type):
        """Retorna o conteúdo do arquivo de teste"""
        test_file = f"teste{test_num}.c"
        test_path = Path("Testes") / test_type / test_file
        if test_path.exists():
            with open(test_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        return "Arquivo não encontrado"


def main():
    """Função principal"""
    base_dir = Path.cwd()
    
    # Encontra pastas dos alunos
    students = []
    for item in base_dir.iterdir():
        if item.is_dir() and item.name not in ["Testes", ".git", "__pycache__"] and not item.name.startswith('.'):
            students.append(item)
    
    print(f"Encontrados {len(students)} alunos para avaliar")
    print("Iniciando correção...")
    
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
            print(f"Erro ao avaliar {student_dir.name}: {e}")
            results[student_dir.name] = {
                "score": 0.0,
                "details": {"error": str(e)}
            }
    
    # Gera relatório CSV
    csv_file = base_dir / "notas_finais.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Aluno", "Nota Final", "Status"])
        
        for aluno, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
            score = data['score']
            status = "Aprovado" if score >= 5.0 else "Reprovado"
            writer.writerow([aluno, f"{score:.1f}", status])
    
    # Relatório final
    print(f"\n{'#'*80}")
    print("RELATÓRIO FINAL")
    print(f"{'#'*80}\n")
    
    print(f"{'ALUNO':<35} {'NOTA':<8} {'STATUS':<10}")
    print("-" * 55)
    
    for aluno, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
        score = data['score']
        status = "Aprovado" if score >= 5.0 else "Reprovado"
        print(f"{aluno:<35} {score:<8.1f} {status:<10}")
    
    # Estatísticas
    scores = [data['score'] for data in results.values()]
    if scores:
        print(f"\n{'ESTATÍSTICAS':<35}")
        print(f"{'Média:':<35} {sum(scores)/len(scores):.1f}")
        print(f"{'Maior nota:':<35} {max(scores):.1f}")
        print(f"{'Menor nota:':<35} {min(scores):.1f}")
        print(f"{'Aprovados:':<35} {sum(1 for s in scores if s >= 5.0)}/{len(scores)}")
        print(f"{'Taxa de aprovação:':<35} {sum(1 for s in scores if s >= 5.0)/len(scores)*100:.0f}%")
    
    print(f"\nRelatório CSV salvo em: {csv_file}")


if __name__ == "__main__":
    main()