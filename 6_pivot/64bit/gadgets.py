import struct

# 0x0000000000400b6c: pop r12; pop r13; pop r14; pop r15; ret;
pop_r15_addr = 0x400b72
def pop_r15(r15_0):
    b = b''
    b += struct.pack('<Q', pop_r15_addr)
    b += struct.pack('<Q', r15_0)
    return b

# 0x0000000000400b00: pop rax; ret;
pop_rax_addr = 0x400b00
def pop_rax(rax_0):
    b = b''
    b += struct.pack('<Q', pop_rax_addr)
    b += struct.pack('<Q', rax_0)
    return b

# 0x0000000000400900: pop rbp; ret;
pop_rbp_addr = 0x400900
def pop_rbp(rbp_0):
    b = b''
    b += struct.pack('<Q', pop_rbp_addr)
    b += struct.pack('<Q', rbp_0)
    return b

# 0x0000000000400b73: pop rdi; ret;
pop_rdi_addr = 0x400b73
def pop_rdi(rdi_0):
    b = b''
    b += struct.pack('<Q', pop_rdi_addr)
    b += struct.pack('<Q', rdi_0)
    return b

# 0x0000000000400b6c: pop r12; pop r13; pop r14; pop r15; ret;
pop_r14_r15_addr = 0x400b70
def pop_r14_r15(r14_0, r15_1):
    b = b''
    b += struct.pack('<Q', pop_r14_r15_addr)
    b += struct.pack('<Q', r14_0)
    b += struct.pack('<Q', r15_1)
    return b

# 0x0000000000400b71: pop rsi; pop r15; ret;
pop_rsi_r15_addr = 0x400b71
def pop_rsi_r15(rsi_0, r15_1):
    b = b''
    b += struct.pack('<Q', pop_rsi_r15_addr)
    b += struct.pack('<Q', rsi_0)
    b += struct.pack('<Q', r15_1)
    return b

# 0x0000000000400b6c: pop r12; pop r13; pop r14; pop r15; ret;
pop_r13_r14_r15_addr = 0x400b6e
def pop_r13_r14_r15(r13_0, r14_1, r15_2):
    b = b''
    b += struct.pack('<Q', pop_r13_r14_r15_addr)
    b += struct.pack('<Q', r13_0)
    b += struct.pack('<Q', r14_1)
    b += struct.pack('<Q', r15_2)
    return b

# 0x0000000000400b6f: pop rbp; pop r14; pop r15; ret;
pop_rbp_r14_r15_addr = 0x400b6f
def pop_rbp_r14_r15(rbp_0, r14_1, r15_2):
    b = b''
    b += struct.pack('<Q', pop_rbp_r14_r15_addr)
    b += struct.pack('<Q', rbp_0)
    b += struct.pack('<Q', r14_1)
    b += struct.pack('<Q', r15_2)
    return b

# 0x0000000000400b6c: pop r12; pop r13; pop r14; pop r15; ret;
pop_r12_r13_r14_r15_addr = 0x400b6c
def pop_r12_r13_r14_r15(r12_0, r13_1, r14_2, r15_3):
    b = b''
    b += struct.pack('<Q', pop_r12_r13_r14_r15_addr)
    b += struct.pack('<Q', r12_0)
    b += struct.pack('<Q', r13_1)
    b += struct.pack('<Q', r14_2)
    b += struct.pack('<Q', r15_3)
    return b

# 0x0000000000400b6d: pop rsp; pop r13; pop r14; pop r15; ret;
pop_rsp_r13_r14_r15_addr = 0x400b6d
def pop_rsp_r13_r14_r15(rsp_0, r13_1, r14_2, r15_3):
    b = b''
    b += struct.pack('<Q', pop_rsp_r13_r14_r15_addr)
    b += struct.pack('<Q', rsp_0)
    b += struct.pack('<Q', r13_1)
    b += struct.pack('<Q', r14_2)
    b += struct.pack('<Q', r15_3)
    return b

# 0x0000000000400b6b: pop rbp; pop r12; pop r13; pop r14; pop r15; ret;
pop_rbp_r12_r13_r14_r15_addr = 0x400b6b
def pop_rbp_r12_r13_r14_r15(rbp_0, r12_1, r13_2, r14_3, r15_4):
    b = b''
    b += struct.pack('<Q', pop_rbp_r12_r13_r14_r15_addr)
    b += struct.pack('<Q', rbp_0)
    b += struct.pack('<Q', r12_1)
    b += struct.pack('<Q', r13_2)
    b += struct.pack('<Q', r14_3)
    b += struct.pack('<Q', r15_4)
    return b

