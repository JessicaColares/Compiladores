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