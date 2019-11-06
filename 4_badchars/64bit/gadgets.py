import struct

# 0x0000000000400bac: pop r12; pop r13; pop r14; pop r15; ret;
pop_r15_addr = 0x400bb2
def pop_r15(r15_0):
    b = b''
    b += struct.pack('<Q', pop_r15_addr)
    b += struct.pack('<Q', r15_0)
    return b

# 0x0000000000400b3b: pop r12; pop r13; ret;
pop_r13_addr = 0x400b3d
def pop_r13(r13_0):
    b = b''
    b += struct.pack('<Q', pop_r13_addr)
    b += struct.pack('<Q', r13_0)
    return b

# 0x00000000004007f0: pop rbp; ret;
pop_rbp_addr = 0x4007f0
def pop_rbp(rbp_0):
    b = b''
    b += struct.pack('<Q', pop_rbp_addr)
    b += struct.pack('<Q', rbp_0)
    return b

# 0x0000000000400b39: pop rdi; ret;
pop_rdi_addr = 0x400b39
def pop_rdi(rdi_0):
    b = b''
    b += struct.pack('<Q', pop_rdi_addr)
    b += struct.pack('<Q', rdi_0)
    return b

# 0x0000000000400bac: pop r12; pop r13; pop r14; pop r15; ret;
pop_r14_r15_addr = 0x400bb0
def pop_r14_r15(r14_0, r15_1):
    b = b''
    b += struct.pack('<Q', pop_r14_r15_addr)
    b += struct.pack('<Q', r14_0)
    b += struct.pack('<Q', r15_1)
    return b

# 0x0000000000400b3b: pop r12; pop r13; ret;
pop_r12_r13_addr = 0x400b3b
def pop_r12_r13(r12_0, r13_1):
    b = b''
    b += struct.pack('<Q', pop_r12_r13_addr)
    b += struct.pack('<Q', r12_0)
    b += struct.pack('<Q', r13_1)
    return b

# 0x0000000000400b41: pop rsi; pop r15; ret;
pop_rsi_r15_addr = 0x400b41
def pop_rsi_r15(rsi_0, r15_1):
    b = b''
    b += struct.pack('<Q', pop_rsi_r15_addr)
    b += struct.pack('<Q', rsi_0)
    b += struct.pack('<Q', r15_1)
    return b

# 0x0000000000400b3c: pop rsp; pop r13; ret;
pop_rsp_r13_addr = 0x400b3c
def pop_rsp_r13(rsp_0, r13_1):
    b = b''
    b += struct.pack('<Q', pop_rsp_r13_addr)
    b += struct.pack('<Q', rsp_0)
    b += struct.pack('<Q', r13_1)
    return b

# 0x0000000000400bac: pop r12; pop r13; pop r14; pop r15; ret;
pop_r13_r14_r15_addr = 0x400bae
def pop_r13_r14_r15(r13_0, r14_1, r15_2):
    b = b''
    b += struct.pack('<Q', pop_r13_r14_r15_addr)
    b += struct.pack('<Q', r13_0)
    b += struct.pack('<Q', r14_1)
    b += struct.pack('<Q', r15_2)
    return b

# 0x0000000000400baf: pop rbp; pop r14; pop r15; ret;
pop_rbp_r14_r15_addr = 0x400baf
def pop_rbp_r14_r15(rbp_0, r14_1, r15_2):
    b = b''
    b += struct.pack('<Q', pop_rbp_r14_r15_addr)
    b += struct.pack('<Q', rbp_0)
    b += struct.pack('<Q', r14_1)
    b += struct.pack('<Q', r15_2)
    return b

# 0x0000000000400bac: pop r12; pop r13; pop r14; pop r15; ret;
pop_r12_r13_r14_r15_addr = 0x400bac
def pop_r12_r13_r14_r15(r12_0, r13_1, r14_2, r15_3):
    b = b''
    b += struct.pack('<Q', pop_r12_r13_r14_r15_addr)
    b += struct.pack('<Q', r12_0)
    b += struct.pack('<Q', r13_1)
    b += struct.pack('<Q', r14_2)
    b += struct.pack('<Q', r15_3)
    return b

# 0x0000000000400bad: pop rsp; pop r13; pop r14; pop r15; ret;
pop_rsp_r13_r14_r15_addr = 0x400bad
def pop_rsp_r13_r14_r15(rsp_0, r13_1, r14_2, r15_3):
    b = b''
    b += struct.pack('<Q', pop_rsp_r13_r14_r15_addr)
    b += struct.pack('<Q', rsp_0)
    b += struct.pack('<Q', r13_1)
    b += struct.pack('<Q', r14_2)
    b += struct.pack('<Q', r15_3)
    return b

# 0x0000000000400bab: pop rbp; pop r12; pop r13; pop r14; pop r15; ret;
pop_rbp_r12_r13_r14_r15_addr = 0x400bab
def pop_rbp_r12_r13_r14_r15(rbp_0, r12_1, r13_2, r14_3, r15_4):
    b = b''
    b += struct.pack('<Q', pop_rbp_r12_r13_r14_r15_addr)
    b += struct.pack('<Q', rbp_0)
    b += struct.pack('<Q', r12_1)
    b += struct.pack('<Q', r13_2)
    b += struct.pack('<Q', r14_3)
    b += struct.pack('<Q', r15_4)
    return b

# 0x0000000000400b35: mov dword ptr [rbp], esp; ret;
mov_ptr_rbp_esp_addr = 0x400b35
def mov_ptr_rbp_esp():
    b = b''
    b += struct.pack('<Q', mov_ptr_rbp_esp_addr)
    return b

# 0x0000000000400b34: mov qword ptr [r13], r12; ret;
mov_ptr_r13_r12_addr = 0x400b34
def mov_ptr_r13_r12():
    b = b''
    b += struct.pack('<Q', mov_ptr_r13_r12_addr)
    return b

