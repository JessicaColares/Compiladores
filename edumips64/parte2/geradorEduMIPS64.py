import sys
from typing import List, Dict, Set

class GeradorEduMIPS64:
    def __init__(self):
        self.variaveis_globais = {'global_counter', 'newline', 'format_str', 'stack_bottom', 'stack_top'}
        self.variaveis_locais: Dict[str, Dict[str, int]] = {}
        self.temporarios = ['$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$t8', '$t9']
        self.mapeamento = {'a': '0($sp)', 'b': '8($sp)', 'c': '16($sp)', 'd': '$a3', 'e': '32($sp)', 'local_sum': '16($sp)'}
        self.current_function = "main"
        self.stack_offset = 0
        self.label_count = 0
        self.labels_conteudo: Dict[str, List[str]] = {}

    def format_instr(self, instr: str, *args: str) -> str:
        instr_part = instr.ljust(8)
        args_part = ', '.join(args)
        return f"\t{instr_part}{args_part}"

    def get_offset(self, var: str) -> str:
        if var in self.mapeamento:
            return self.mapeamento[var]
        elif self.current_function:
            if var not in self.variaveis_locais.get(self.current_function, {}):
                self.variaveis_locais.setdefault(self.current_function, {})[var] = self.stack_offset
                self.stack_offset += 8
            offset = self.variaveis_locais[self.current_function][var]
            return f"{offset}($sp)"
        else:
            return f"{var}($zero)"

    def encontrar_proxima_label_nao_vazia(self, labels_ordenadas, atual):
        indice = labels_ordenadas.index(atual)
        for prox in labels_ordenadas[indice+1:]:
            if self.labels_conteudo[prox]:
                return prox
        return None

    def traduzir_argumento(self, linha: str) -> List[str]:
        asm = []
        valor = linha.split(' ', 1)[1].strip()

        registradores_args = ["$a0", "$a1", "$a2", "$a3"]
        reg_destino = registradores_args[min(self.stack_offset // 8, len(registradores_args) - 1)]

        if valor.startswith('"') and valor.endswith('"'):
            if "global_counter" in valor:
                asm.append(self.format_instr("daddi", reg_destino, "$zero", "format_str"))
            else:
                valor_limpo = valor.replace('"', '').replace(':', '').strip()
                asm.append(self.format_instr("ld", reg_destino, f"{valor_limpo}($zero)"))
        elif valor.isdigit():
            asm.append(self.format_instr("daddi", reg_destino, "$zero", valor))
        else:
            asm.append(self.format_instr("ld", reg_destino, self.get_offset(valor)))

        self.stack_offset += 8
        return asm

    def traduzir_condicao(self, cond: str, label_true: str, label_false: str = None) -> List[str]:
        asm = []
        ops = [('>=', 'slt', 'beqz', False),
               ('>', 'slt', 'bnez', True),
               ('<=', 'slt', 'beqz', True),
               ('<', 'slt', 'bnez', False),
               ('==', 'xor', 'beqz', None),
               ('!=', 'xor', 'bnez', None)]

        for op, inst, branch, invert in ops:
            if op in cond:
                var, val = [x.strip() for x in cond.split(op)]
                asm.append(self.format_instr("ld", "$t0", self.get_offset(var)))
                asm.append(self.format_instr("daddi", "$t1", "$zero", val))
                if inst == 'slt':
                    if invert:
                        asm.append(self.format_instr(inst, "$t2", "$t1", "$t0"))
                    else:
                        asm.append(self.format_instr(inst, "$t2", "$t0", "$t1"))
                elif inst == 'xor':
                    asm.append(self.format_instr("xor", "$t2", "$t0", "$t1"))
                asm.append(self.format_instr(branch, "$t2", label_true))
                if label_false:
                    asm.append(self.format_instr("j", label_false))
                break
        return asm

    def traduzir_chamada(self, linha: str) -> List[str]:
        asm = []
        if '=' in linha:
            dest, call_part = [x.strip() for x in linha.split('=')]
            _, func_name = call_part.split()
        else:
            parts = linha.strip().split()
            func_name = parts[1]

        if func_name == "printf":
            # Tratamento específico para printf
            asm.append(self.format_instr("daddi", "$a0", "$zero", "format_str"))
            # Carrega o argumento (ajuste conforme necessário)
            arg = parts[2] if len(parts) > 2 else "0"
            asm.append(self.format_instr("ld", "$a1", self.get_offset(arg)))
            asm.append(self.format_instr("SYSCALL", "5"))  # Chamada para printf
        else:
            asm.append(self.format_instr("jal", func_name))

        if '=' in linha:
            asm.append(self.format_instr("sd", "$v0", self.get_offset(dest)))
        return asm

    def traduzir_linha(self, linha: str, is_main: bool) -> List[str]:
        linha = linha.split(';')[0].strip()
        if not linha:
            return []

        asm = [f"\t; {linha}"]

        if ('int' in linha or 'void' in linha) and '(' in linha and not is_main:
            func_name = linha.split('(')[0].split()[-1]
            self.current_function = func_name
            self.variaveis_locais[func_name] = {}
            self.stack_offset = 0
            return ["", f"{func_name}:", self.format_instr("daddi", "$sp", "$sp", "-32")]

        if linha.startswith('if ') and ' goto ' in linha:
            cond_part, label = linha[3:].split(' goto ')
            cond = cond_part.strip()
            label = label.strip()
            cond_code = self.traduzir_condicao(cond, label)
            return asm + cond_code + [f"{label}:"]

        if linha.startswith('arg '):
            arg_asm = self.traduzir_argumento(linha)
            if '$a3' in arg_asm[-1]:
                arg_asm[-1] = arg_asm[-1].replace('$a3', '$t0')
            return asm + arg_asm

        for op, inst in [('+=' , 'daddu'), ('-=' , 'dsubu'), ('*=' , 'dmulu')]:
            if op in linha:
                dest, src = [x.strip() for x in linha.split(op)]
                asm.append(self.format_instr("ld", "$t8", self.get_offset(dest)))
                asm.append(self.format_instr("ld" if not src.isdigit() else "daddi", "$t9", self.get_offset(src) if not src.isdigit() else "$zero", src if src.isdigit() else None))
                asm.append(self.format_instr(inst, "$t0", "$t8", "$t9"))
                asm.append(self.format_instr("sd", "$t0", self.get_offset(dest)))
                return asm

        if '++' in linha or '--' in linha:
            var = linha.replace('++', '').replace('--', '').strip()
            delta = '1' if '++' in linha else '-1'
            asm.append(self.format_instr("ld", "$t0", self.get_offset(var)))
            asm.append(self.format_instr("daddi", "$t0", "$t0", delta))
            asm.append(self.format_instr("sd", "$t0", self.get_offset(var)))
            return asm

        if '=' in linha:
            dest, expr = [p.strip() for p in linha.split('=', 1)]

            ops = [('>=', 'slt', 'beqz', False),
                   ('>', 'slt', 'bnez', True),
                   ('<=', 'slt', 'beqz', True),
                   ('<', 'slt', 'bnez', False),
                   ('==', 'xor', 'beqz', None),
                   ('!=', 'xor', 'bnez', None)]

            for op, inst, branch, invert in ops:
                if op in expr:
                    x, y = [e.strip() for e in expr.split(op)]
                    asm.append(self.format_instr("ld", "$t8", self.get_offset(x)))
                    asm.append(self.format_instr("daddi", "$t9", "$zero", y))
                    if inst == 'slt':
                        if invert:
                            asm.append(self.format_instr(inst, "$t0", "$t9", "$t8"))
                        else:
                            asm.append(self.format_instr(inst, "$t0", "$t8", "$t9"))
                    elif inst == 'xor':
                        asm.append(self.format_instr("xor", "$t0", "$t8", "$t9"))
                        if branch == 'beqz':
                            asm.append(self.format_instr("seqz", "$t0", "$t0"))
                        else:
                            asm.append(self.format_instr("snez", "$t0", "$t0"))
                    asm.append(self.format_instr("sd", "$t0", self.get_offset(dest)))
                    return asm

        if linha.startswith('call '):
            return asm + self.traduzir_chamada(linha)

        if linha.startswith('goto '):
            label = linha.split()[1]
            if label in self.labels_conteudo and not self.labels_conteudo[label]:
                labels_ordenadas = list(self.labels_conteudo.keys())
                prox_label = self.encontrar_proxima_label_nao_vazia(labels_ordenadas, label)
                if prox_label:
                    label = prox_label
                else:
                    return [
                        self.format_instr("SYSCALL", "5"),
                        self.format_instr("daddi", "$v0", "$zero", "10"),
                        self.format_instr("SYSCALL", "0")
                    ]
                
                asm.append(self.format_instr("j", label))
            return asm

        if linha.endswith(':'):
            label_name = linha[:-1]
            if label_name not in self.labels_conteudo:
                self.labels_conteudo[label_name] = []
                return ["", linha]
            else:
                return []  # Evita definir a label duas vezes


        if linha.startswith('return'):
            has_value = 'return' in linha and not linha.endswith('return')
            return asm + self.traduzir_retorno(is_main, has_value)

        return asm


    def traduzir_argumento(self, linha: str) -> List[str]:
        asm = []
        valor = linha.split(' ', 1)[1].strip()

        # suporte a múltiplos argumentos: $a0, $a1, $a2, $a3...
        registradores_args = ["$a0", "$a1", "$a2", "$a3"]
        reg_destino = registradores_args[min(self.stack_offset // 8, len(registradores_args) - 1)]

        if valor.startswith('"') and valor.endswith('"'):
            if "global_counter" in valor:
                # exemplo específico para strings contendo global_counter
                asm.append(self.format_instr("daddi", reg_destino, "$zero", "format_str"))
            else:
                valor_limpo = valor.replace('"', '').replace(':', '').strip()
                asm.append(self.format_instr("ld", reg_destino, f"{valor_limpo}($zero)"))
        elif valor.isdigit():
            asm.append(self.format_instr("daddi", reg_destino, "$zero", valor))
        else:
            asm.append(self.format_instr("ld", reg_destino, self.get_offset(valor)))

        self.stack_offset += 8
        return asm


    def traduzir_atribuicao(self, dest: str, expr: str, is_main: bool) -> List[str]:
        asm = []
        # Handle local variable declaration
        if dest not in self.mapeamento and not dest.isdigit() and self.current_function:
            if dest not in self.variaveis_locais.get(self.current_function, {}):
                if self.current_function not in self.variaveis_locais:
                    self.variaveis_locais[self.current_function] = {}
                self.variaveis_locais[self.current_function][dest] = self.stack_offset
                self.stack_offset += 8

        # Special case for local_sum in process_data
        if dest == 'local_sum' and not is_main:
            asm.extend([
                self.format_instr("daddu", "$t0", "$a0", "$a1"),
                self.format_instr("daddu", "$t0", "$t0", "$a2"),
                self.format_instr("daddu", "$t0", "$t0", "$a3"),
                self.format_instr("ld", "$t1", "32($sp)"),
                self.format_instr("daddu", "$t0", "$t0", "$t1"),
                self.format_instr("sd", "$t0", "16($sp)")
            ])
            return asm

        # Handle arithmetic operations
        for op, inst in [('+', 'daddu'), ('-', 'dsubu'), ('*', 'dmulu'), ('/', 'ddiv')]:
            if op in expr:
                x, y = [p.strip() for p in expr.split(op)]
                # Load x
                if x.isdigit():
                    asm.append(self.format_instr("daddi", "$t8", "$zero", x))
                elif x in self.mapeamento:
                    asm.append(self.format_instr("ld", "$t8", self.mapeamento[x]))
                elif self.current_function and x in self.variaveis_locais.get(self.current_function, {}):
                    offset = self.variaveis_locais[self.current_function][x]
                    asm.append(self.format_instr("ld", "$t8", f"{offset}($sp)"))
                else:
                    asm.append(self.format_instr("ld", "$t8", f"{x}($zero)"))
                
                # Load y
                if y.isdigit():
                    asm.append(self.format_instr("daddi", "$t9", "$zero", y))
                elif y in self.mapeamento:
                    asm.append(self.format_instr("ld", "$t9", self.mapeamento[y]))
                elif self.current_function and y in self.variaveis_locais.get(self.current_function, {}):
                    offset = self.variaveis_locais[self.current_function][y]
                    asm.append(self.format_instr("ld", "$t9", f"{offset}($sp)"))
                else:
                    asm.append(self.format_instr("ld", "$t9", f"{y}($zero)"))
                
                # Perform operation
                asm.append(self.format_instr(inst, "$t0", "$t8", "$t9"))
                
                # Store result
                if dest in self.mapeamento:
                    asm.append(self.format_instr("sd", "$t0", self.mapeamento[dest]))
                elif self.current_function and dest in self.variaveis_locais.get(self.current_function, {}):
                    offset = self.variaveis_locais[self.current_function][dest]
                    asm.append(self.format_instr("sd", "$t0", f"{offset}($sp)"))
                else:
                    asm.append(self.format_instr("sd", "$t0", f"{dest}($zero)"))
                return asm

        # Simple assignment
        if expr.isdigit():
            asm.append(self.format_instr("daddi", "$t0", "$zero", expr))
        elif expr in self.mapeamento:
            asm.append(self.format_instr("ld", "$t0", self.mapeamento[expr]))
        elif self.current_function and expr in self.variaveis_locais.get(self.current_function, {}):
            offset = self.variaveis_locais[self.current_function][expr]
            asm.append(self.format_instr("ld", "$t0", f"{offset}($sp)"))
        else:
            asm.append(self.format_instr("ld", "$t0", f"{expr}($zero)"))
        
        if dest in self.mapeamento:
            asm.append(self.format_instr("sd", "$t0", self.mapeamento[dest]))
        elif self.current_function and dest in self.variaveis_locais.get(self.current_function, {}):
            offset = self.variaveis_locais[self.current_function][dest]
            asm.append(self.format_instr("sd", "$t0", f"{offset}($sp)"))
        else:
            asm.append(self.format_instr("sd", "$t0", f"{dest}($zero)"))
        return asm

    def traduzir_retorno(self, is_main: bool, has_value: bool = False) -> List[str]:
        if is_main:
            return [
                self.format_instr("daddi", "$a0", "$zero", "format_str"),
                self.format_instr("ld", "$a1", "global_counter($zero)"),
                self.format_instr("SYSCALL", "5"),
                self.format_instr("daddi", "$v0", "$zero", "10"),
                self.format_instr("SYSCALL", "0")
            ]
        else:
            asm = []
            if has_value:
                # Get return value from last assignment or specified variable
                if self.variaveis_locais.get(self.current_function):
                    last_var = list(self.variaveis_locais[self.current_function].keys())[-1]
                    offset = self.variaveis_locais[self.current_function][last_var]
                    asm.append(self.format_instr("ld", "$v0", f"{offset}($sp)"))
            asm.extend([
                self.format_instr("daddi", "$sp", "$sp", "32"),
                self.format_instr("jr", "$ra")
            ])
            return asm

    def gerar_assembly(self, codigo: List[str]) -> List[str]:
        asm = [
            "\t\t.data",
            "global_counter: .word 0",
            'newline: .asciiz "\\n"',
            'format_str: .asciiz "global_counter: %d\\n"',
            "stack_bottom: .space 4096",
            "stack_top:",
            ""
        ]

        # Add temporary variables if used
        temp_vars = set()
        for linha in codigo:
            if '=' in linha:
                dest = linha.split('=')[0].strip()
                if dest.startswith('t') and dest[1:].isdigit():
                    temp_vars.add(dest)
        
        if temp_vars:
            asm.extend([f"{t}: .word 0" for t in sorted(temp_vars)])
            asm.append("")

        asm.extend([
            "\t\t.code",
            "main:",
            self.format_instr("daddi", "$sp", "$zero", "stack_top"),
            self.format_instr("daddi", "$t0", "$zero", "0"),
            self.format_instr("sd", "$t0", "global_counter($zero)")
        ])

        # Translate main
        asm_main = []
        in_main = False
        for linha in codigo:
            linha = linha.strip()
            if linha == "main:" or linha.startswith("int main()"):
                in_main = True
                self.current_function = "main"
                continue
            elif ('int' in linha or 'void' in linha) and '(' in linha:
                in_main = False
                self.current_function = linha.split('(')[0].split()[-1]

            if in_main and linha:
                asm_main.extend(self.traduzir_linha(linha, True))

        asm.extend(asm_main)
        
        # Add syscalls for main return
        asm.extend(self.traduzir_retorno(is_main=True))

        # Translate other functions
        asm_restante = []
        in_main = False
        for linha in codigo:
            linha = linha.strip()
            if linha == "main:" or linha.startswith("int main()"):
                continue
            elif ('int' in linha or 'void' in linha) and '(' in linha:
                func_name = linha.split('(')[0].split()[-1]
                asm_restante.extend(["", f"{func_name}:", self.format_instr("daddi", "$sp", "$sp", "-32")])
                self.current_function = func_name
                self.stack_offset = 0
                continue

            if not in_main and linha:
                translated = self.traduzir_linha(linha, False)
                if translated:  # Avoid adding empty lines
                    asm_restante.extend(translated)

        asm.extend(asm_restante)
        return asm

def main():
    if len(sys.argv) != 2:
        print("Uso: python geradorEduMIPS64.py arquivo.tac")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        codigo = f.readlines()

    gerador = GeradorEduMIPS64()
    assembly = gerador.gerar_assembly(codigo)

    output_file = sys.argv[1].replace('.tac', '.s')
    with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(assembly))

    print(f"Arquivo gerado com sucesso: {output_file}")

if __name__ == "__main__":
    main()