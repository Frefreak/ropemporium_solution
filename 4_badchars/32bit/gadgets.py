import struct

# 0x080488fb: pop ebp; ret;
pop_ebp_addr = 0x80488fb
def pop_ebp(ebp_0):
    b = b''
    b += struct.pack('<I', pop_ebp_addr)
    b += struct.pack('<I', ebp_0)
    return b

# 0x08048896: pop ebx; pop ecx; ret;
pop_ecx_addr = 0x8048897
def pop_ecx(ecx_0):
    b = b''
    b += struct.pack('<I', pop_ecx_addr)
    b += struct.pack('<I', ecx_0)
    return b

# 0x08048461: pop ebx; ret;
pop_ebx_addr = 0x8048461
def pop_ebx(ebx_0):
    b = b''
    b += struct.pack('<I', pop_ebx_addr)
    b += struct.pack('<I', ebx_0)
    return b

# 0x0804889a: pop edi; ret;
pop_edi_addr = 0x804889a
def pop_edi(edi_0):
    b = b''
    b += struct.pack('<I', pop_edi_addr)
    b += struct.pack('<I', edi_0)
    return b

# 0x08048896: pop ebx; pop ecx; ret;
pop_ebx_ecx_addr = 0x8048896
def pop_ebx_ecx(ebx_0, ecx_1):
    b = b''
    b += struct.pack('<I', pop_ebx_ecx_addr)
    b += struct.pack('<I', ebx_0)
    b += struct.pack('<I', ecx_1)
    return b

# 0x080488f8: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_edi_ebp_addr = 0x80488fa
def pop_edi_ebp(edi_0, ebp_1):
    b = b''
    b += struct.pack('<I', pop_edi_ebp_addr)
    b += struct.pack('<I', edi_0)
    b += struct.pack('<I', ebp_1)
    return b

# 0x08048899: pop esi; pop edi; ret;
pop_esi_edi_addr = 0x8048899
def pop_esi_edi(esi_0, edi_1):
    b = b''
    b += struct.pack('<I', pop_esi_edi_addr)
    b += struct.pack('<I', esi_0)
    b += struct.pack('<I', edi_1)
    return b

# 0x080488f8: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_esi_edi_ebp_addr = 0x80488f9
def pop_esi_edi_ebp(esi_0, edi_1, ebp_2):
    b = b''
    b += struct.pack('<I', pop_esi_edi_ebp_addr)
    b += struct.pack('<I', esi_0)
    b += struct.pack('<I', edi_1)
    b += struct.pack('<I', ebp_2)
    return b

# 0x080488f8: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_ebx_esi_edi_ebp_addr = 0x80488f8
def pop_ebx_esi_edi_ebp(ebx_0, esi_1, edi_2, ebp_3):
    b = b''
    b += struct.pack('<I', pop_ebx_esi_edi_ebp_addr)
    b += struct.pack('<I', ebx_0)
    b += struct.pack('<I', esi_1)
    b += struct.pack('<I', edi_2)
    b += struct.pack('<I', ebp_3)
    return b

# 0x08048893: mov dword ptr [edi], esi; ret;
mov_ptr_edi_esi_addr = 0x8048893
def mov_ptr_edi_esi():
    b = b''
    b += struct.pack('<I', mov_ptr_edi_esi_addr)
    return b

