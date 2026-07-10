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