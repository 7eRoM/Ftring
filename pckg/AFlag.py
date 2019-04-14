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

    set_flag_a = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(set_flag_a)-1)
        tmp_set_flag = set_flag_a[method]

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(randint(1, 15))[2:].zfill(4)
        low_nibble_val2 = bin(randint(16-int(low_nibble_val1, 2), 15))[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)
        VAL2 = int(rest_nibble_val2 + low_nibble_val2, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(randint(0, 14))[2:].zfill(4)
        low_nibble_val2 = bin(randint(int(low_nibble_val1, 2)+1, 15))[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)
        VAL2 = int(rest_nibble_val2 + low_nibble_val2, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(15)[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(0)[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    return tmp_set_flag


def clear_flag(method=-1):

    clear_flag_a = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(clear_flag_a)-1)
        tmp_clear_flag = clear_flag_a[method]

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(randint(0, 15))[2:].zfill(4)
        low_nibble_val2 = bin(randint(0, 15-int(low_nibble_val1, 2)))[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)
        VAL2 = int(rest_nibble_val2 + low_nibble_val2, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(randint(0, 15))[2:].zfill(4)
        low_nibble_val2 = bin(randint(0, int(low_nibble_val1, 2)))[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
            rest_nibble_val2 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)
        VAL2 = int(rest_nibble_val2 + low_nibble_val2, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(randint(0, 14))[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        low_nibble_val1 = bin(randint(1, 15))[2:].zfill(4)
        if sel_reg_type == "REGISTERS_32":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 29, 1)])
        elif sel_reg_type == "REGISTERS_16":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 13, 1)])
        elif sel_reg_type == "REGISTERS_8h":
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])
        else:
            rest_nibble_val1 = ''.join([str(randint(0, 1)) for i in range(1, 5, 1)])

        VAL1 = int(rest_nibble_val1 + low_nibble_val1, 2)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    return tmp_clear_flag


def mov_flag_to_reg(reg="-1", method=-1):

    mov_flag_to_reg_a = [
    """lahf
    test ah, 10h
    jz $LABEL$
    xor al, 1
$LABEL$:"""]
 
    if method == -1:
        method = randint(0, len(mov_flag_to_reg_a)-1)
    tmp_mov_flag_to_reg = mov_flag_to_reg_a[method].replace("$LABEL$", ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8)))

    return tmp_mov_flag_to_reg
