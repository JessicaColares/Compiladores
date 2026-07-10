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