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
	; call atualiza
	jal     atualiza
	; return 0
	daddi   $v0, $zero, 10
	SYSCALL 0
	daddi   $v0, $zero, 10
	SYSCALL 0

atualiza:
	; y = 0
	; y = 10
	; t1 = y * 2
	; y = t1
	; return y
	daddi   $sp, $sp, 32
	jr      $ra
	; call atualiza
	jal     atualiza
	; return 0
	daddi   $sp, $sp, 32
	jr      $ra