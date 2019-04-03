import os
import sys
import binascii
from random import randint
import argparse


REGISTERS_TYPE = ["REGISTERS_32", "REGISTERS_16", "REGISTERS_8h", "REGISTERS_8l"]
REGISTERS_32 = ["ebx", "ecx", "edx", "esi", "edi"]
REGISTERS_16 = ["bx", "cx", "dx", "si", "di"]
REGISTERS_8h = ["bh", "ch", "dh"]
REGISTERS_8l = ["bl", "cl", "dl"]


def set_flag(flag, method=-1):
    set_flag_c = [
    """stc""",
    """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
    """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$"""]
    if flag == "c":
        if method == -1:
            method = randint(0, len(set_flag_c)-1)
            tmp_set_flag = set_flag_c[method]
        
        if method == 1:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(1, 4294967295)
                VAL2 = randint(4294967296-VAL1, 4294967295)
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(1, 65535)
                VAL2 = randint(65536-VAL1, 65535)
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(1, 255)
                VAL2 = randint(256-VAL1, 255)
            else:
                VAL1 = randint(1, 255)
                VAL2 = randint(256-VAL1, 255)

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
            tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))
        
        if method == 2:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(1, 4294967295)
                VAL2 = randint(VAL1+1, 4294967295)
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(1, 65535)
                VAL2 = randint(VAL1+1, 65535)
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(1, 255)
                VAL2 = randint(VAL1+1, 255)
            else:
                VAL1 = randint(1, 255)
                VAL2 = randint(VAL1+1, 255)

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
            tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

        return tmp_set_flag


def clear_flag(flag, method=-1):
    clear_flag_c = ["clc"]
    if flag == "c":
        if method == -1:
            method = randint(0, len(clear_flag_c)-1)
        return clear_flag_c[method]


def mov_flag_to_reg(flag, reg="-1", method=-1):
    mov_flag_to_reg_c = ["setc $REG$"]
    if flag == "c":
        if method == -1:
            method = randint(0, len(mov_flag_to_reg_c)-1)
        return mov_flag_to_reg_c[method].replace("$REG$", reg)


def xor_shl(curr_bit, prev_bit, is_lsb, is_msb):
    if curr_bit == "0":
        res_flag = clear_flag("c")
    else:
        res_flag = set_flag("c")
    res_mov = mov_flag_to_reg("c", reg="bl")

    if is_msb:
        bit_res = """
    {0}
    {1}
    xor al, bl""".format(res_flag, res_mov)
    else:
        bit_res = """
    {0}
    {1}
    xor al, bl
    shl al, 1""".format(res_flag, res_mov)

    return bit_res


def bit_generator(curr_bit, prev_bit, is_lsb, is_msb, method=-1):
    bit_gen_method = ["xor_shl"]
    if method == -1:
        method = randint(0, len(bit_gen_method)-1)
    if curr_bit == "0":
        res_flag = 756756
    else:
        res_flag = 75676
    bit_res = globals()[bit_gen_method[method]](curr_bit, prev_bit, is_lsb, is_msb)
    return bit_res


def byte_generator(curr_byte):
    prev_bit = -1
    byte_res = """xor al, al"""
    for i in range(0,len(curr_byte),1):
        is_lsb = is_msb = False
        if i == 0:
            is_lsb = True
        if i == 7:
            is_msb = True       
        bit_res = bit_generator(curr_byte[i], prev_bit, is_lsb, is_msb)
        byte_res = byte_res + """
    {0}""".format(bit_res)
        prev_bit = curr_byte[i]
    
    return byte_res


def main_func(var, val, type):
    cumm_res = ""
    val = val + "\0"
    char_list = [bin(x)[2:].zfill(8) for x in val.encode('UTF-8')]
    for i in range(0,len(char_list),1):
        byte_res = byte_generator(char_list[i])
        if type == "s":
            cumm_res = cumm_res + """
    // *** Creating char '{0}' ***
    {1}

    // Writing char '{2}' to memory
    mov byte ptr[{3} + {4}], al
       
        """.format(val[i], byte_res, val[i], var, i)
        elif type == "d":
            cumm_res = cumm_res + """
    // *** Creating char '{0}' ***
    {1}

    // Writing char '{2}' to memory
    mov {3}, dword ptr [{4}]
    mov byte ptr[{3} + {5}], al       
        """.format(val[i], byte_res, val[i], REGISTERS_32[randint(0, len(REGISTERS_32)-1)], var, i)

    # Final result
    res = """
__asm
{{
    {0}
}}
    """.format(cumm_res)

    print(res)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Flag-Based String Generator, a C++ string obfuscator.')
    parser.add_argument('--version', action='version', version='Ftring v0.1.0')
    parser.add_argument('-r', '--var', help='varable name', required=True)
    parser.add_argument('-l', '--val', help='a string would be assigned to the variable', required=True)
    parser.add_argument('-t', '--type', choices=['s', 'd'], help='type of variable: static array or dynamic array', required=True)
    args = parser.parse_args()
    
    main_func(args.var, args.val, args.type)
