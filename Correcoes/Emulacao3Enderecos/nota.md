# Trabalho 08 - Emulação do Código de Três Endereços

Teste 1

```
a = 5
b = 10
c = a + b
print c
```

ponto:

Teste 2

```
a = 5
b = 10
t1 = a < b
print t1
if t1 goto L1
goto L2
L1:
c = a + b
print c
goto L3
L2:
c = a - b
print c
L3:
```

ponto:

Teste 3

```
a = 5 
b = 10 
t1: 
t4 = a + 1 
t5 = t4 < b 
if t5 goto t2 
goto t3 
t2: 
t6 = a < b 
if t6 goto t7 
goto t8 
t7: 
t9 = a * 2 
a = t9 
t8: 
goto t1 
t3: 
t10 = b - 1 
b = t10
```

ponto:

Teste 4

```
a = 5
b = 5
c = 5
t1 = a * b 
t2 = t1 + c 
print t2
```

ponto:

Teste 5

```
a = 5 
b = 10 
t1 = a + b 
c = t1 
t2 = "Resultado: %d"
print t2 
print c 
```

ponto:

Teste 6

```
a = 1 
b = 2 
c = 10 
d = 5 
param a 
param b 
t1 = call soma, 2 
x = t1 
param c 
param d 
t2 = call multiplicacao, 2 
y = t2 
param x 
param y 
t3 = call resultado, 2 
z = t3 
t4 = "Resultado: %d" 
print t4 
print z
```

ponto:

Teste 7

```
idade = 25
nota = 85
salario = 2500
param idade
param nota
t1 = call calcula_classificacao, 2
classif = t1
param salario
t2 = call calcula_salario_liquido, 1
salario_liq = t2
print "=== RELATORIO ==="
print "Idade: %d anos"
print idade
print "Nota: %d pontos"
print nota
print "Classificacao: %d"
print classif
print "Salario Bruto: R$ %d"
print salario
print "Salario Liquido: R$ %d"
print salario_liq
print "================="
```

ponto:

Teste 8

```
func soma, 2
t1 = a + b
return t1
endfunc

a = 5
b = 10
param a
param b
t1 = call soma, 2
print t1
```

ponto:

Teste 9

```
func multiplicacao, 2
t1 = a * b
return t1
endfunc

a = 2
b = 6
param a
param b
t1 = call multiplicacao, 2
print t1
```

ponto:

Teste 10

```
func soma, 3
t1 = p0 + p1
c = t1
return c
endfunc

func multiplicacao, 4
t2 = p0 * p1
t2 = t2 * p2
g = t2
return g
endfunc

a = 5
b = 5
c = 0
d = 6
e = 3
f = 2
g = 0

param a
param b
param c
t1 = call soma, 3

param d
param e
param f
param g
t2 = call multiplicacao, 4

t3 = "Resultado: %d"

print t3
print t1
print t3
print t2
```


ponto:

### Observação

## Nota Final:

