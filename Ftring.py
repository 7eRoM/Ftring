import os
import sys
import binascii
from random import randint
import argparse


REGISTERS_TYPE = ["REGISTERS_32", "REGISTERS_16",
                  "REGISTERS_8h", "REGISTERS_8l"]
REGISTERS_32 = ["ebx", "ecx", "edx", "esi", "edi"]
REGISTERS_16 = ["bx", "cx", "dx", "si", "di"]
REGISTERS_8h = ["bh", "ch", "dh"]
REGISTERS_8l = ["bl", "cl", "dl"]


def set_flag(flag, method=-1):
    tmp_set_flag = ""

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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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

    set_flag_z = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if flag == "z":
        if method == -1:
            method = randint(0, len(set_flag_z)-1)
            tmp_set_flag = set_flag_z[method]

        if method == 0:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            VAL1 = 1

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    set_flag_o = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if flag == "o":
        if method == -1:
            method = randint(0, len(set_flag_o)-1)
            tmp_set_flag = set_flag_o[method]

        if method == 0:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                if VAL1 <= 2147483647:
                    VAL2 = randint(2147483648-VAL1, 4294967295-VAL1)                  
                else:
                    VAL2 = randint(-1*VAL1, 2147483647-VAL1)
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                if VAL1 <= 32767:
                    VAL2 = randint(32768-VAL1, 65535-VAL1)                  
                else:
                    VAL2 = randint(-1*VAL1, 32767-VAL1)

            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(128-VAL1, 255-VAL1)                  
                else:
                    VAL2 = randint(-1*VAL1, 127-VAL1)
            else:
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(128-VAL1, 255-VAL1)                  
                else:
                    VAL2 = randint(-1*VAL1, 127-VAL1)

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
            tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

        if method == 1:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                if VAL1 <= 2147483647:
                    VAL2 = randint(VAL1+1, VAL1+2147483648)                    
                else:
                    VAL2 = randint(VAL1-2147483647, VAL1)
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                if VAL1 <= 32767:
                    VAL2 = randint(VAL1+1, VAL1+32768)                    
                else:
                    VAL2 = randint(VAL1-32767, VAL1)
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(VAL1+1, VAL1+128)                    
                else:
                    VAL2 = randint(VAL1-127, VAL1)
            else:
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(VAL1+1, VAL1+128)                    
                else:
                    VAL2 = randint(VAL1-127, VAL1)

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))
            tmp_set_flag = tmp_set_flag.replace("$VAL2$", str(VAL2))

        if method == 2:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([2147483647,4294967295])
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([32767,65535])
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([127,255])
            else:
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([127,255])

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

        if method == 3:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([0,2147483648])
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([0,32768])
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([0,128])
            else:
                VAL1 = (lambda val_list : val_list[randint(0, 1)])([0,128])

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    set_flag_s = [
            """mov $TMP_REG$, $VAL1$
        add $TMP_REG$, $VAL2$""",
            """mov $TMP_REG$, $VAL1$
        sub $TMP_REG$, $VAL2$""",
            """mov $TMP_REG$, $VAL1$
        inc $TMP_REG$""",
            """mov $TMP_REG$, $VAL1$
        dec $TMP_REG$"""]

    if flag == "s":
        if method == -1:
            method = randint(0, len(set_flag_o)-1)
            tmp_set_flag = set_flag_o[method]

        if method == 0:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_set_flag = tmp_set_flag.replace("$TMP_REG$", sel_reg)
            VAL1 = 0

            tmp_set_flag = tmp_set_flag.replace("$VAL1$", str(VAL1))

    return tmp_set_flag


def clear_flag(flag, method=-1):
    clear_flag_c = [
        """clc""",
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$"""]

    if flag == "c":
        if method == -1:
            method = randint(0, len(clear_flag_c)-1)
            tmp_clear_flag = clear_flag_c[method]

        if method == 1:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                VAL2 = randint(0, 4294967295-VAL1)
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                VAL2 = randint(0, 65535-VAL1)
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                VAL2 = randint(0, 255-VAL1)
            else:
                VAL1 = randint(0, 255)
                VAL2 = randint(0, 255-VAL1)

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
            tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

        if method == 2:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                VAL2 = randint(0, VAL1)
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                VAL2 = randint(0, VAL1)
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                VAL2 = randint(0, VAL1)
            else:
                VAL1 = randint(0, 255)
                VAL2 = randint(0, VAL1)

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
            tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

    clear_flag_z = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if flag == "z":
        if method == -1:
            method = randint(0, len(clear_flag_z)-1)
            tmp_clear_flag = clear_flag_z[method]

        if method == 0:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
            VAL1 = randint(0, 4294967295)

            if VAL1 == 1:
                VAL1 = 2

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    clear_flag_o = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if flag == "o":
        if method == -1:
            method = randint(0, len(clear_flag_o)-1)
            tmp_clear_flag = clear_flag_o[method]

        if method == 0:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                if VAL1 <= 2147483647:
                    VAL2 = randint(-1*VAL1, 2147483647-VAL1)                                     
                else:
                    VAL2 = randint(2147483648-VAL1, 4294967295-VAL1) 
                    
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                if VAL1 <= 32767:
                    VAL2 = randint(-1*VAL1, 32767-VAL1)
                else:
                    VAL2 = randint(32768-VAL1, 65535-VAL1)

            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(-1*VAL1, 127-VAL1)
                else:
                    VAL2 = randint(128-VAL1, 255-VAL1)                  

            else:
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(-1*VAL1, 127-VAL1)
                else:
                    VAL2 = randint(128-VAL1, 255-VAL1)

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
            tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))

        if method == 1:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                if VAL1 <= 2147483647:
                    VAL2 = randint(VAL1-2147483647, VAL1)
                else:
                    VAL2 = randint(VAL1+1, VAL1+2147483648) 
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                if VAL1 <= 32767:
                    VAL2 = randint(VAL1-32767, VAL1)
                else:
                    VAL2 = randint(VAL1+1, VAL1+32768)                    
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(VAL1-127, VAL1)
                else:
                    VAL2 = randint(VAL1+1, VAL1+128)       
            else:
                VAL1 = randint(0, 255)
                if VAL1 <= 127:
                    VAL2 = randint(VAL1-127, VAL1)
                else:
                    VAL2 = randint(VAL1+1, VAL1+128)

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))
            tmp_clear_flag = tmp_clear_flag.replace("$VAL2$", str(VAL2))
        
        if method == 2:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)
            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                if VAL1 == 2147483647 or VAL1 == 4294967295:
                    VAL1 = VAL1 - 1
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                if VAL1 == 32767 or VAL1 == 65535:
                    VAL1 = VAL1 - 1
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                if VAL1 == 127 or VAL1 == 255:
                    VAL1 = VAL1 - 1
            else:
                VAL1 = randint(0, 255)
                if VAL1 == 127 or VAL1 == 255:
                    VAL1 = VAL1 - 1

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

        if method == 3:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
            tmp_clear_flag = tmp_clear_flag.replace("$TMP_REG$", sel_reg)

            if sel_reg_type == "REGISTERS_32":
                VAL1 = randint(0, 4294967295)
                if VAL1 == 0 or VAL1 == 2147483648:
                    VAL1 = VAL1 + 1
            elif sel_reg_type == "REGISTERS_16":
                VAL1 = randint(0, 65535)
                if VAL1 == 0 or VAL1 == 32768:
                    VAL1 = VAL1 + 1
            elif sel_reg_type == "REGISTERS_8h":
                VAL1 = randint(0, 255)
                if VAL1 == 0 or VAL1 == 128:
                    VAL1 = VAL1 + 1
            else:
                VAL1 = randint(0, 255)
                if VAL1 == 0 or VAL1 == 128:
                    VAL1 = VAL1 + 1

            tmp_clear_flag = tmp_clear_flag.replace("$VAL1$", str(VAL1))

    clear_flag_s = [
        """mov $TMP_REG$, $VAL1$
    add $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    sub $TMP_REG$, $VAL2$""",
        """mov $TMP_REG$, $VAL1$
    inc $TMP_REG$""",
        """mov $TMP_REG$, $VAL1$
    dec $TMP_REG$"""]

    if flag == "s":
        if method == -1:
            method = randint(0, len(clear_flag_s)-1)
            tmp_clear_flag = clear_flag_s[method]

        if method == 0:
            sel_reg_type = REGISTERS_TYPE[randint(0, len(REGISTERS_TYPE)-1)]
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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
            sel_reg = globals()[sel_reg_type][randint(
                0, len(globals()[sel_reg_type])-1)]
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


def mov_flag_to_reg(flag, reg="-1", method=-1):
    mov_flag_to_reg_c = ["setc $REG$"]
    mov_flag_to_reg_z = ["setz $REG$"]
    mov_flag_to_reg_o = ["seto $REG$"]
    mov_flag_to_reg_s = ["sets $REG$"]
    if flag == "c":
        if method == -1:
            method = randint(0, len(mov_flag_to_reg_c)-1)
        tmp_mov_flag_to_reg = mov_flag_to_reg_c[method].replace("$REG$", reg)
    
    elif flag == "z":
        if method == -1:
            method = randint(0, len(mov_flag_to_reg_z)-1)
        tmp_mov_flag_to_reg = mov_flag_to_reg_z[method].replace("$REG$", reg)

    elif flag == "o":
        if method == -1:
            method = randint(0, len(mov_flag_to_reg_o)-1)
        tmp_mov_flag_to_reg = mov_flag_to_reg_o[method].replace("$REG$", reg)

    elif flag == "s":
        if method == -1:
            method = randint(0, len(mov_flag_to_reg_s)-1)
        tmp_mov_flag_to_reg = mov_flag_to_reg_s[method].replace("$REG$", reg)

    return tmp_mov_flag_to_reg


def xor_shl(curr_bit, prev_bit, is_lsb, is_msb):
    if curr_bit == "0":
        res_flag = clear_flag("s")
    else:
        res_flag = set_flag("s")
    res_mov = mov_flag_to_reg("s", reg="bl")

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
