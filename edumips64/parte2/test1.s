		.data
global_counter: .word 0
newline: .asciiz "\n"
format_str: .asciiz "global_counter: %d\n"
stack_bottom: .space 4096
stack_top:

		.code
main:
	daddi   $sp, $zero, stack_top
	daddi   $t0, $zero, 0
	sd      $t0, global_counter($zero)
	; a = 0
	; b = 0
	; c = 0
	daddi   $v0, $zero, 10
	SYSCALL 0
	; a = 0
	; b = 0
	; c = 0