		.data
global_counter: .word 0
newline: .asciiz "\n"
format_str: .asciiz "global_counter: %d\n"
stack_bottom: .space 4096
stack_top:

t1: .word 0
t2: .word 0
t3: .word 0
t4: .word 0
t5: .word 0
t6: .word 0
t7: .word 0
t8: .word 0
t9: .word 0

		.code
main:
	daddi   $sp, $zero, stack_top
	daddi   $t0, $zero, 0
	sd      $t0, global_counter($zero)
	; arg 10
	daddi   $a0, $zero, 10
	; arg 20
	daddi   $a1, $zero, 20
	; arg 30
	daddi   $a2, $zero, 30
	; arg 5
	daddi   $t0, $zero, 5
	; arg 8
	daddi   $t0, $zero, 8
	; call process_data
	jal     process_data
	; arg "global_counter: %d\n"
	daddi   $t0, $zero, format_str
	; arg global_counter
	ld      $t0, 48($sp)
	; call printf
	daddi   $a0, $zero, format_str
	ld      $a1, 64($sp)
	SYSCALL 5
	daddi   $a0, $zero, format_str
	ld      $a1, global_counter($zero)
	SYSCALL 5
	daddi   $v0, $zero, 10
	SYSCALL 0
	; global_counter = 0

process_data:
	; param a
	; param b
	; param c
	; param d
	; param e
	; t1 = a + b
	; t2 = t1 + c
	; t3 = t2 + d
	; t4 = t3 + e
	; local_sum = t4
	; t5 = local_sum >= 100
	ld      $t8, 16($sp)
	daddi   $t9, $zero, 100
	slt     $t0, $t8, $t9
	sd      $t0, 72($sp)
	; else t5 goto L1
	; t6 = global_counter + 1
	; global_counter = t6
	; goto L2

L1:
	; t7 = global_counter - 1
	; global_counter = t7

L2:

L3:
	; t8 = global_counter < 5
	ld      $t8, 48($sp)
	daddi   $t9, $zero, 5
	slt     $t0, $t8, $t9
	sd      $t0, 80($sp)
	; else t8 goto L4
	; t9 = global_counter + 2
	; global_counter = t9
	SYSCALL 5
	daddi   $v0, $zero, 10
	SYSCALL 0

L4:
	; arg 10
	daddi   $t0, $zero, 10
	; arg 20
	daddi   $t0, $zero, 20
	; arg 30
	daddi   $t0, $zero, 30
	; arg 5
	daddi   $t0, $zero, 5
	; arg 8
	daddi   $t0, $zero, 8
	; call process_data
	jal     process_data
	; arg "global_counter: %d\n"
	daddi   $t0, $zero, format_str
	; arg global_counter
	ld      $t0, 48($sp)
	; call printf
	daddi   $a0, $zero, format_str
	ld      $a1, 64($sp)
	SYSCALL 5