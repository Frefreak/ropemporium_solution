import struct

# 0x080486db: pop ebp; ret;
pop_ebp_addr = 0x80486db
def pop_ebp(ebp_0):
    b = b''
    b += struct.pack('<I', pop_ebp_addr)
    b += struct.pack('<I', ebp_0)
    return b

# 0x080483e1: pop ebx; ret;
pop_ebx_addr = 0x80483e1
def pop_ebx(ebx_0):
    b = b''
    b += struct.pack('<I', pop_ebx_addr)
    b += struct.pack('<I', ebx_0)
    return b

# 0x080486d8: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_edi_ebp_addr = 0x80486da
def pop_edi_ebp(edi_0, ebp_1):
    b = b''
    b += struct.pack('<I', pop_edi_ebp_addr)
    b += struct.pack('<I', edi_0)
    b += struct.pack('<I', ebp_1)
    return b

# 0x080486d8: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_esi_edi_ebp_addr = 0x80486d9
def pop_esi_edi_ebp(esi_0, edi_1, ebp_2):
    b = b''
    b += struct.pack('<I', pop_esi_edi_ebp_addr)
    b += struct.pack('<I', esi_0)
    b += struct.pack('<I', edi_1)
    b += struct.pack('<I', ebp_2)
    return b

# 0x080486d8: pop ebx; pop esi; pop edi; pop ebp; ret;
pop_ebx_esi_edi_ebp_addr = 0x80486d8
def pop_ebx_esi_edi_ebp(ebx_0, esi_1, edi_2, ebp_3):
    b = b''
    b += struct.pack('<I', pop_ebx_esi_edi_ebp_addr)
    b += struct.pack('<I', ebx_0)
    b += struct.pack('<I', esi_1)
    b += struct.pack('<I', edi_2)
    b += struct.pack('<I', ebp_3)
    return b

# 0x08048670: mov dword ptr [edi], ebp; ret;
mov_ptr_edi_ebp_addr = 0x8048670
def mov_ptr_edi_ebp():
    b = b''
    b += struct.pack('<I', mov_ptr_edi_ebp_addr)
    return b

