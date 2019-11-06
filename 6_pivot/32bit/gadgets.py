import struct

# 0x080488c0: pop eax; ret;
pop_eax_addr = 0x80488c0
def pop_eax(eax_0):
    b = b''
    b += struct.pack('<I', pop_eax_addr)
    b += struct.pack('<I', eax_0)
    return b

# 0x0804892b: pop ebp; ret;
pop_ebp_addr = 0x804892b
def pop_ebp(ebp_0):
    b = b''
    b += struct.pack('<I', pop_ebp_addr)
    b += struct.pack('<I', ebp_0)
    return b

# 0x08048571: pop ebx; ret;
pop_ebx_addr = 0x8048571
def pop_ebx(ebx_0):
    b = b''
    b += struct.pack('<I', pop_ebx_addr)
    b += struct.pack('<I', ebx_0)
    return b

# 0x08048928: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_edi_ebp_addr = 0x804892a
def pop_edi_ebp(edi_0, ebp_1):
    b = b''
    b += struct.pack('<I', pop_edi_ebp_addr)
    b += struct.pack('<I', edi_0)
    b += struct.pack('<I', ebp_1)
    return b

# 0x08048928: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_esi_edi_ebp_addr = 0x8048929
def pop_esi_edi_ebp(esi_0, edi_1, ebp_2):
    b = b''
    b += struct.pack('<I', pop_esi_edi_ebp_addr)
    b += struct.pack('<I', esi_0)
    b += struct.pack('<I', edi_1)
    b += struct.pack('<I', ebp_2)
    return b

# 0x08048928: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_ebx_esi_edi_ebp_addr = 0x8048928
def pop_ebx_esi_edi_ebp(ebx_0, esi_1, edi_2, ebp_3):
    b = b''
    b += struct.pack('<I', pop_ebx_esi_edi_ebp_addr)
    b += struct.pack('<I', ebx_0)
    b += struct.pack('<I', esi_1)
    b += struct.pack('<I', edi_2)
    b += struct.pack('<I', ebp_3)
    return b

