import os
import sys
import binascii
import string
import random
from random import randint
from random import shuffle
from random import choice
import argparse
from pckg import AFlag
from pckg import CFlag
from pckg import PFlag
from pckg import SFlag
from pckg import ZFlag


REGISTERS_TYPE = ["REGISTERS_32", "REGISTERS_16", "REGISTERS_8h", "REGISTERS_8l"]
REGISTERS_32 = ["ebx", "ecx", "edx", "esi", "edi"]
REGISTERS_16 = ["bx", "cx", "dx", "si", "di"]
REGISTERS_8h = ["bh", "ch", "dh"]
REGISTERS_8l = ["bl", "cl", "dl"]


def xor_shl(curr_bit, prev_bit, is_lsb, is_msb):

    flags = ["c", "z", "s", "a", "p"]
    sel_flag = flags[randint(0, len(flags)-1)]
    if sel_flag == "a":
        if curr_bit == "0":
            res_flag = AFlag.clear_flag()
        else:
            res_flag = AFlag.set_flag()
        res_mov = AFlag.mov_flag_to_reg(reg="bl")
    elif sel_flag == "c":
        if curr_bit == "0":
            res_flag = CFlag.clear_flag()
        else:
            res_flag = CFlag.set_flag()
        res_mov = CFlag.mov_flag_to_reg(reg="bl")
    elif sel_flag == "p":
        if curr_bit == "0":
            res_flag = PFlag.clear_flag()
        else:
            res_flag = PFlag.set_flag()
        res_mov = PFlag.mov_flag_to_reg(reg="bl")   
    elif sel_flag == "s":
        if curr_bit == "0":
            res_flag = SFlag.clear_flag()
        else:
            res_flag = SFlag.set_flag()
        res_mov = SFlag.mov_flag_to_reg(reg="bl")   
    elif sel_flag == "z":
        if curr_bit == "0":
            res_flag = ZFlag.clear_flag()
        else:
            res_flag = ZFlag.set_flag()
        res_mov = ZFlag.mov_flag_to_reg(reg="bl")   



    if sel_flag == "a":
        if is_msb:
            bit_res = """
    {0}
    {1}""".format(res_flag, res_mov)
        else:
            bit_res = """
    {0}
    {1}
    shl al, 1""".format(res_flag, res_mov)

    else:
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
    bit_res = globals()[bit_gen_method[method]](
        curr_bit, prev_bit, is_lsb, is_msb)
    return bit_res


def byte_generator(curr_byte):
    prev_bit = -1
    byte_res = """xor al, al"""
    for i in range(0, len(curr_byte), 1):
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
    for i in range(0, len(char_list), 1):
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
    parser = argparse.ArgumentParser(
        description='Flag-Based String Generator, a C++ string obfuscator.')
    parser.add_argument('--version', action='version', version='Ftring v0.1.0')
    parser.add_argument('-r', '--var', help='varable name', required=True)
    parser.add_argument(
        '-l', '--val', help='a string would be assigned to the variable', required=True)
    parser.add_argument('-t', '--type', choices=[
                        's', 'd'], help='type of variable: static array or dynamic array', required=True)
    args = parser.parse_args()

    main_func(args.var, args.val, args.type)
