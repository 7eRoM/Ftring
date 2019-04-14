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

    set_flag_s = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(set_flag_s)-1)
        tmp_set_flag = set_flag_s[method]

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 2147483647)
            VAL2 = randint(2147483648-VAL1, 4294967295-VAL1)
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 32767)
            VAL2 = randint(32768-VAL1, 65535-VAL1)
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 127)
            VAL2 = randint(128-VAL1, 255-VAL1)
        else:
            VAL1 = randint(0, 127)
            VAL2 = randint(128-VAL1, 255-VAL1)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 2147483647)
            VAL2 = randint(VAL1+1, VAL1+2147483648)
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 32767)
            VAL2 = randint(VAL1+1, VAL1+32768)
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 127)
            VAL2 = randint(VAL1+1, VAL1+128)
        else:
            VAL1 = randint(0, 127)
            VAL2 = randint(VAL1+1, VAL1+128)

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = 2147483647
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = 32767
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = 127
        else:
            VAL1 = 127

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        VAL1 = 0

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    return tmp_set_flag


def clear_flag(method=-1):

    clear_flag_s = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(clear_flag_s)-1)
        tmp_clear_flag = clear_flag_s[method]

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(2147483648, 4294967295)
            VAL2 = randint(-1*VAL1, 2147483647-VAL1)
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(32768, 65535)
            VAL2 = randint(-1*VAL1, 32767-VAL1)
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(128, 255)
            VAL2 = randint(-1*VAL1, 127-VAL1)
        else:
            VAL1 = randint(128, 255)
            VAL2 = randint(-1*VAL1, 127-VAL1)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(2147483648, 4294967295)
            VAL2 = randint(VAL1-2147483647, VAL1)
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(32768, 65535)
            VAL2 = randint(VAL1-32767, VAL1)
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(128, 255)
            VAL2 = randint(VAL1-127, VAL1)
        else:
            VAL1 = randint(128, 255)
            VAL2 = randint(VAL1-127, VAL1)

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = 4294967295
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = 65535
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = 255
        else:
            VAL1 = 255

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)

        if sel_reg_type == "REGISTERS_32":
            VAL1 = 2147483648
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = 32768
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = 128
        else:
            VAL1 = 128

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    return tmp_clear_flag


def mov_flag_to_reg(reg="-1", method=-1):

    mov_flag_to_reg_s = ["sets $REG$"]

    if method == -1:
        method = randint(0, len(mov_flag_to_reg_s)-1)
    tmp_mov_flag_to_reg = mov_flag_to_reg_s[method].replace("$REG$", reg)

    return tmp_mov_flag_to_reg
