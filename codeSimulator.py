<<<<<<< HEAD


=======
import sys

registers = {
    "00000": 0,  # zero
    "00001": 0,  # ra
    "00010": 0x0000_017C,  # sp 
    "00011": 0,  # gp
    "00100": 0,  # tp
    "00101": 0,  # t0
    "00110": 0,  # t1
    "00111": 0,  # t2
    "01000": 0,  # s0
    "01001": 0,  # s1
    "01010": 0,  # a0
    "01011": 0,  # a1
    "01100": 0,  # a2
    "01101": 0,  # a3
    "01110": 0,  # a4
    "01111": 0,  # a5
    "10000": 0,  # a6
    "10001": 0,  # a7
    "10010": 0,  # s2
    "10011": 0,  # s3
    "10100": 0,  # s4
    "10101": 0,  # s5
    "10110": 0,  # s6
    "10111": 0,  # s7
    "11000": 0,  # s8
    "11001": 0,  # s9
    "11010": 0,  # s10
    "11011": 0,
    "11100":0,
    "11101":0,
    "11110":0,
    "11111":0
}

datamem = {0x0001_0000 + 4 * i: 0 for i in range(32)}

R_type = ["0110011"]
I_type = ["0000011", "0010011", "1100111"]
S_type = ["0100011"]
B_type = ["1100011"]
J_type = ["1101111"]
BONUS_type = ["1111111"] 
<<<<<<< HEAD
>>>>>>> fc7f50164d44b100ac327de11928bedc8eac0e26
=======

def twocomp_to_dec(binary):
    num_bits = len(binary) 
    value = int(binary, 2) 
    if binary[0] == '1':  
        value -= (1 << num_bits) 
    return value

def add(instruction):
    rs1 = instruction[-20:-15]
    rs2 = instruction[-25:-20]
    rd = instruction[-12:-7]
    registers[rd] = registers[rs1] + registers[rs2]
>>>>>>> 14f3bd2275fd26f17621957edcd306e2e30fa89d

def sext(binary, num_bits):
    value = int(binary, 2)  
    if binary[0] == '1': 
        value -= (1 << len(binary)) 
    return format(value & ((1 << num_bits) - 1), f'0{num_bits}b')

def dec_to_twocomp(decimal_num, num_bits):
    if decimal_num < 0:
        decimal_num += (1 << num_bits)  
    return format(decimal_num, f'0{num_bits}b')

def unsigned(val):
    return val & 0xffffffff

def sub(instruction):
    rs1 = instruction[-20:-15]
    rs2 = instruction[-25:-20]
    rd = instruction[-12:-7]
    registers[rd] = registers[rs1] - registers[rs2]