import struct

# 0x00000000004008bc: pop r12; pop r13; pop r14; pop r15; ret;
pop_r15_addr = 0x4008c2
def pop_r15(r15_0):
    b = b''
    b += struct.pack('<Q', pop_r15_addr)
    b += struct.pack('<Q', r15_0)
    return b

# 0x00000000004006b0: pop rbp; ret;
pop_rbp_addr = 0x4006b0
def pop_rbp(rbp_0):
    b = b''
    b += struct.pack('<Q', pop_rbp_addr)
    b += struct.pack('<Q', rbp_0)
    return b

# 0x00000000004008c3: pop rdi; ret;
pop_rdi_addr = 0x4008c3
def pop_rdi(rdi_0):
    b = b''
    b += struct.pack('<Q', pop_rdi_addr)
    b += struct.pack('<Q', rdi_0)
    return b

# 0x00000000004008bc: pop r12; pop r13; pop r14; pop r15; ret;
pop_r14_r15_addr = 0x4008c0
def pop_r14_r15(r14_0, r15_1):
    b = b''
    b += struct.pack('<Q', pop_r14_r15_addr)
    b += struct.pack('<Q', r14_0)
    b += struct.pack('<Q', r15_1)
    return b

# 0x00000000004008c1: pop rsi; pop r15; ret;
pop_rsi_r15_addr = 0x4008c1
def pop_rsi_r15(rsi_0, r15_1):
    b = b''
    b += struct.pack('<Q', pop_rsi_r15_addr)
    b += struct.pack('<Q', rsi_0)
    b += struct.pack('<Q', r15_1)
    return b

# 0x00000000004008bc: pop r12; pop r13; pop r14; pop r15; ret;
pop_r13_r14_r15_addr = 0x4008be
def pop_r13_r14_r15(r13_0, r14_1, r15_2):
    b = b''
    b += struct.pack('<Q', pop_r13_r14_r15_addr)
    b += struct.pack('<Q', r13_0)
    b += struct.pack('<Q', r14_1)
    b += struct.pack('<Q', r15_2)
    return b

# 0x00000000004008bf: pop rbp; pop r14; pop r15; ret;
pop_rbp_r14_r15_addr = 0x4008bf
def pop_rbp_r14_r15(rbp_0, r14_1, r15_2):
    b = b''
    b += struct.pack('<Q', pop_rbp_r14_r15_addr)
    b += struct.pack('<Q', rbp_0)
    b += struct.pack('<Q', r14_1)
    b += struct.pack('<Q', r15_2)
    return b

# 0x00000000004008bc: pop r12; pop r13; pop r14; pop r15; ret;
pop_r12_r13_r14_r15_addr = 0x4008bc
def pop_r12_r13_r14_r15(r12_0, r13_1, r14_2, r15_3):
    b = b''
    b += struct.pack('<Q', pop_r12_r13_r14_r15_addr)
    b += struct.pack('<Q', r12_0)
    b += struct.pack('<Q', r13_1)
    b += struct.pack('<Q', r14_2)
    b += struct.pack('<Q', r15_3)
    return b

# 0x00000000004008bd: pop rsp; pop r13; pop r14; pop r15; ret;
pop_rsp_r13_r14_r15_addr = 0x4008bd
def pop_rsp_r13_r14_r15(rsp_0, r13_1, r14_2, r15_3):
    b = b''
    b += struct.pack('<Q', pop_rsp_r13_r14_r15_addr)
    b += struct.pack('<Q', rsp_0)
    b += struct.pack('<Q', r13_1)
    b += struct.pack('<Q', r14_2)
    b += struct.pack('<Q', r15_3)
    return b

# 0x00000000004008bb: pop rbp; pop r12; pop r13; pop r14; pop r15; ret;
pop_rbp_r12_r13_r14_r15_addr = 0x4008bb
def pop_rbp_r12_r13_r14_r15(rbp_0, r12_1, r13_2, r14_3, r15_4):
    b = b''
    b += struct.pack('<Q', pop_rbp_r12_r13_r14_r15_addr)
    b += struct.pack('<Q', rbp_0)
    b += struct.pack('<Q', r12_1)
    b += struct.pack('<Q', r13_2)
    b += struct.pack('<Q', r14_3)
    b += struct.pack('<Q', r15_4)
    return b

