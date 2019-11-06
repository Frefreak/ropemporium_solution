.global main

.section .text
main:
	leaq cmd, %rdi
	mov $0xdeadbeef, %r13
	call system

.section .data
cmd:
	.asciz "cat flag.txt"
