# 💻 Compiladores 
Trabalhos realizados na disciplina de Compiladores e Scripts de correção para usar na monitoria.

---

## 🔎 Como fazer a variável de ambiente funcionar

#### Criar a variável de ambiente no Windows.
```
python -m venv venv
```

#### Ativar a variável de ambiente.
```
.\venv\Scripts\activate
```

#### Instalar as ferramentas antlr4
```
pip install antlr4-tools
```

#### Instalar o runtime
```
pip install antlr4-python3-runtime
```

### Visitor
```
antlr4 -Dlanguage=Python3 -visitor Expr.g4
```
#### Se quiser usar com visitor sem gerar listener
```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -no-listener -visitor miniC.g4
```

### Ambos
```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -listener -visitor Html.g
```

🚨 Observação importante, lembre-se de sempre deixar o antlr-4.13.2-complete.jar dentro da pasta que pretende gerar os tokens.

---

## 📒 Instrução importante para o trabalho gerador de HTML

O windows 11 constantemente troca o enconding de saída, tanto na própria variável de ambiente como o terminal, então é necessário configurar ambos. É só copiar e colar no terminal as seguintes linhas.

#### Primeiro passo:
```
$env:PYTHONUTF8=1
```

#### Segundo passo:
```
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

#### Terceiro passo:
```
python main.py | Set-Content -Encoding UTF8 -Force output.html
```
#### ou
```
python main.py > output.html
```

Você pode testar direto no navegador ou se preferir tem um site excelente também: https://www.w3schools.com/tags/tag_select.asp
