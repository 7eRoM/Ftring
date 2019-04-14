import os
import sys
import binascii
import string
import random
from random import randint
from random import shuffle
from random import choice
import argparse


REGISTERS_TYPE = ["REGISTERS_32", "REGISTERS_16", "REGISTERS_8h", "REGISTERS_8l"]
REGISTERS_32 = ["ebx", "ecx", "edx", "esi", "edi"]
REGISTERS_16 = ["bx", "cx", "dx", "si", "di"]
REGISTERS_8h = ["bh", "ch", "dh"]
REGISTERS_8l = ["bl", "cl", "dl"]


def set_flag(method=-1):

    set_flag_p = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(set_flag_p)-1)
        tmp_set_flag = set_flag_p[method]

    bit_num = [i for i in range(8)]
    shuffle(bit_num)
    sel_bit_num = (lambda val_list: val_list[0:choice([2, 4, 6])])(bit_num)
    lowest_final_val = ["0" for i in range(8)]
    for i in sel_bit_num:
        lowest_final_val[i] = "1"
    lowest_final_val = ''.join(lowest_final_val)

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(randint(0, 255))[2:].zfill(8)
        lowest_val2 = bin((int(lowest_final_val, 2) - int(lowest_val1, 2))%256)[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
            rest_val2 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
            rest_val2 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""
            rest_val2 = ""

        VAL1 = int(rest_val1 + lowest_val1, 2)
        VAL2 = int(rest_val2 + lowest_val2, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(randint(0, 255))[2:].zfill(8)
        lowest_val2 = bin((int(lowest_val1, 2) - int(lowest_final_val, 2))%256)[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
            rest_val2 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
            rest_val2 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""
            rest_val2 = ""

        VAL1 = int(rest_val1 + lowest_val1, 2)
        VAL2 = int(rest_val2 + lowest_val2, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(abs(int(lowest_final_val, 2) - 1))[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""                

        VAL1 = int(rest_val1 + lowest_val1, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(int(lowest_final_val, 2) + 1)[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""                

        VAL1 = int(rest_val1 + lowest_val1, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    return tmp_set_flag


def clear_flag(method=-1):

    clear_flag_p = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(clear_flag_p)-1)
        tmp_clear_flag = clear_flag_p[method]

    bit_num = [i for i in range(8)]
    shuffle(bit_num)
    sel_bit_num = (lambda val_list: val_list[0:choice([1, 3, 5, 7])])(bit_num)
    lowest_final_val = ["0" for i in range(8)]
    for i in sel_bit_num:
        lowest_final_val[i] = "1"
    lowest_final_val = ''.join(lowest_final_val)

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(randint(0, 255))[2:].zfill(8)
        lowest_val2 = bin((int(lowest_final_val, 2) - int(lowest_val1, 2))%256)[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
            rest_val2 = ''.join(
                [str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
            rest_val2 = ''.join(
                [str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""
            rest_val2 = ""

        VAL1 = int(rest_val1 + lowest_val1, 2)
        VAL2 = int(rest_val2 + lowest_val2, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(randint(0, 255))[2:].zfill(8)
        lowest_val2 = bin((int(lowest_val1, 2) - int(lowest_final_val, 2))%256)[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join([str(randint(0, 1)) for i in range(1, 25, 1)])
            rest_val2 = ''.join([str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join([str(randint(0, 1)) for i in range(1, 9, 1)])
            rest_val2 = ''.join([str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""
            rest_val2 = ""

        VAL1 = int(rest_val1 + lowest_val1, 2)
        VAL2 = int(rest_val2 + lowest_val2, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(abs(int(lowest_final_val, 2) - 1))[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join([str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join([str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""                

        VAL1 = int(rest_val1 + lowest_val1, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        lowest_val1 = bin(int(lowest_final_val, 2) + 1)[2:].zfill(8)
        if sel_reg_type == "REGISTERS_32":
            rest_val1 = ''.join([str(randint(0, 1)) for i in range(1, 25, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_val1 = ''.join([str(randint(0, 1)) for i in range(1, 9, 1)])
        else:
            rest_val1 = ""                

        VAL1 = int(rest_val1 + lowest_val1, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))


    return tmp_clear_flag


def mov_flag_to_reg(reg="-1", method=-1):
    mov_flag_to_reg_p = ["setp $REG$"]

    if method == -1:
        method = randint(0, len(mov_flag_to_reg_p)-1)
    tmp_mov_flag_to_reg = mov_flag_to_reg_p[method].replace("$REG$", reg)

    return tmp_mov_flag_to_reg

