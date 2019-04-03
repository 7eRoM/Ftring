// Ftring.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

int main()
{
	char static_array[8];

	__asm
	{

		// *** Creating char 'A' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ebx, 4202000527
		add ebx, 2746221193
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ecx, 1622013946
		sub ecx, 4095067046
		setc bl
		xor al, bl

		// Writing char 'A' to memory
		mov byte ptr[static_array + 0], al

		// *** Creating char 'B' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ecx, 2741558980
		add ecx, 1590161718
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov si, 57594
		sub si, 63027
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl

		// Writing char 'B' to memory
		mov byte ptr[static_array + 1], al

		// *** Creating char 'C' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ch, 233
		sub ch, 251
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov cl, 229
		add cl, 165
		setc bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl

		// Writing char 'C' to memory
		mov byte ptr[static_array + 2], al

		// *** Creating char 'D' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov dl, 131
		sub dl, 143
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl

		// Writing char 'D' to memory
		mov byte ptr[static_array + 3], al

		// *** Creating char 'E' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov bx, 57570
		sub bx, 62517
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl

		// Writing char 'E' to memory
		mov byte ptr[static_array + 4], al

		// *** Creating char 'F' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov bh, 36
		sub bh, 146
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ch, 121
		sub ch, 221
		setc bl
		xor al, bl
		shl al, 1

		mov cx, 13347
		add cx, 61391
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl

		// Writing char 'F' to memory
		mov byte ptr[static_array + 5], al

		// *** Creating char 'G' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov dx, 3820
		sub dx, 24712
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov cl, 16
		add cl, 253
		setc bl
		xor al, bl
		shl al, 1

		mov cl, 23
		add cl, 254
		setc bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl

		// Writing char 'G' to memory
		mov byte ptr[static_array + 6], al

		// *** Creating char ' ' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl

		// Writing char ' ' to memory
		mov byte ptr[static_array + 7], al

	}

    std::cout << static_array << std::endl;

	return 0;
}

