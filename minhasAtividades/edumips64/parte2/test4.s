		.data
global_counter: .word 0
newline: .asciiz "\n"
format_str: .asciiz "global_counter: %d\n"
stack_bottom: .space 4096
stack_top:

t1: .word 0

		.code
main:
	daddi   $sp, $zero, stack_top
	daddi   $t0, $zero, 0
	sd      $t0, global_counter($zero)
	; arg 10
	daddi   $a0, $zero, 10
	; arg 5
	daddi   $a1, $zero, 5
	; call multiplica
	jal     multiplica
	; return 0
	daddi   $v0, $zero, 10
	SYSCALL 0
	daddi   $v0, $zero, 10
	SYSCALL 0

multiplica:
	; param a
	; param b
	; resultado = 0
	; t1 = a * b
	; resultado = t1
	; return resultado
	daddi   $sp, $sp, 32
	jr      $ra
	; arg 10
	daddi   $a2, $zero, 10
	; arg 5
	daddi   $t0, $zero, 5
	; call multiplica
	jal     multiplica
	; return 0
	daddi   $sp, $sp, 32
	jr      $ra