global_counter = 0

process_data:
param a
param b
param c
param d
param e
t1 = a + b
t2 = t1 + c
t3 = t2 + d
t4 = t3 + e
local_sum = t4
t5 = local_sum >= 100
else t5 goto L1
t6 = global_counter + 1
global_counter = t6
goto L2
L1:
t7 = global_counter - 1
global_counter = t7
L2:
L3:
t8 = global_counter < 5
else t8 goto L4
t9 = global_counter + 2
global_counter = t9
goto L3
L4:

main:
arg 10
arg 20
arg 30
arg 5
arg 8
call process_data
arg "global_counter: %d\n"
arg global_counter
call printf