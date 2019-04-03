// Ftring.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>


char *dynamic_array = new char[8];
int main()
{
	__asm
	{

		// *** Creating char 'A' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov bx, 32177
		sub bx, 48058
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

		mov dh, 243
		add dh, 113
		setc bl
		xor al, bl

		// Writing char 'A' to memory
		mov edx, dword ptr[dynamic_array]
		mov byte ptr[edx + 0], al

		// *** Creating char 'B' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ch, 136
		add ch, 238
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

		mov bh, 81
		add bh, 197
		setc bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl

		// Writing char 'B' to memory
		mov edx, dword ptr[dynamic_array]
		mov byte ptr[edx + 1], al

		// *** Creating char 'C' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov si, 47666
		sub si, 56807
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

		mov bl, 203
		add bl, 141
		setc bl
		xor al, bl
		shl al, 1

		mov ch, 100
		add ch, 176
		setc bl
		xor al, bl

		// Writing char 'C' to memory
		mov edx, dword ptr[dynamic_array]
		mov byte ptr[edx + 2], al

		// *** Creating char 'D' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov edx, 3425777005
		sub edx, 3670954670
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

		// Writing char 'D' to memory
		mov edx, dword ptr[dynamic_array]
		mov byte ptr[edx + 3], al

		// *** Creating char 'E' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov bx, 36940
		sub bx, 64996
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

		mov bl, 163
		sub bl, 255
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
		mov ebx, dword ptr[dynamic_array]
		mov byte ptr[ebx + 4], al

		// *** Creating char 'F' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov ch, 51
		sub ch, 154
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

		stc
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

		// Writing char 'F' to memory
		mov ebx, dword ptr[dynamic_array]
		mov byte ptr[ebx + 5], al

		// *** Creating char 'G' ***
		xor al, al

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov cl, 136
		add cl, 206
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

		stc
		setc bl
		xor al, bl
		shl al, 1

		mov bl, 113
		sub bl, 145
		setc bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl

		// Writing char 'G' to memory
		mov edx, dword ptr[dynamic_array]
		mov byte ptr[edx + 6], al

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
		mov edx, dword ptr[dynamic_array]
		mov byte ptr[edx + 7], al

	}

	std::cout << dynamic_array << std::endl;

	return 0;
}
