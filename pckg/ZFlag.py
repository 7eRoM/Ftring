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

    set_flag_z = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(set_flag_z)-1)
        tmp_set_flag = set_flag_z[method]

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 4294967295)
            VAL2 = 4294967296-VAL1
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 65535)
            VAL2 = 65536-VAL1
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 255)
            VAL2 = 256-VAL1
        else:
            VAL1 = randint(0, 255)
            VAL2 = 256-VAL1

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 4294967295)
            VAL2 = VAL1
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 65535)
            VAL2 = VAL1
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 255)
            VAL2 = VAL1
        else:
            VAL1 = randint(0, 255)
            VAL2 = VAL1

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
        tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = 4294967295
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = 65535
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = 255
        else:
            VAL1 = 255

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
        VAL1 = 1

        tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    return tmp_set_flag


def clear_flag(method=-1):

    clear_flag_z = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if method == -1:
        method = randint(0, len(clear_flag_z)-1)
        tmp_clear_flag = clear_flag_z[method]

    if method == 0:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 4294967295)
            VAL2 = randint(0, 4294967295)
            if VAL1 + VAL2 == 4294967296:
                VAL1 = (VAL1 + 1) % 4294967296
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 65535)
            VAL2 = randint(0, 65535)
            if VAL1 + VAL2 == 65536:
                VAL1 = (VAL1 + 1) % 65536
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 255)
            VAL2 = randint(0, 255)
            if VAL1 + VAL2 == 256:
                VAL1 = (VAL1 + 1) % 256
        else:
            VAL1 = randint(0, 255)
            VAL2 = randint(0, 255)
            if VAL1 + VAL2 == 256:
                VAL1 = (VAL1 + 1) % 256

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 1:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 4294967295)
            VAL2 = randint(0, 4294967295)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 4294967296
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 65535)
            VAL2 = randint(0, 65535)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 65536
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 255)
            VAL2 = randint(0, 255)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 256
        else:
            VAL1 = randint(0, 255)
            VAL2 = randint(0, 255)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 256

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
        tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    if method == 2:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        if sel_reg_type == "REGISTERS_32":
            VAL1 = randint(0, 4294967295)
            if VAL1 == 4294967295:
                VAL1 = (VAL1 + 1) % 4294967296
        elif sel_reg_type == "REGISTERS_16":
            VAL1 = randint(0, 65535)
            VAL2 = randint(0, 65535)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 65536
        elif sel_reg_type == "REGISTERS_8h":
            VAL1 = randint(0, 255)
            VAL2 = randint(0, 255)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 256
        else:
            VAL1 = randint(0, 255)
            VAL2 = randint(0, 255)
            if VAL1 == VAL2:
                VAL1 = (VAL1 + 1) % 256

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    if method == 3:
        sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
        sel_reg = globals()[sel_reg_type][randint(0, len(globals()[sel_reg_type])-1)]
        tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
        VAL1 = randint(0, 4294967295)

        if VAL1 == 1:
            VAL1 = 2

        tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    return tmp_clear_flag


def mov_flag_to_reg(reg="-1", method=-1):

    mov_flag_to_reg_z = ["setz $REG$"]

    if method == -1:
        method = randint(0, len(mov_flag_to_reg_z)-1)
    tmp_mov_flag_to_reg = mov_flag_to_reg_z[method].replace("$REG$", reg)

    return tmp_mov_flag_to_reg
