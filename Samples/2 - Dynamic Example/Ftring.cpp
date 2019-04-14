#include "pch.h"
#include <iostream>


char *dynamic_array = new char[8];
int main()
{
	__asm
	{

		// *** Creating char 'A' ***
		xor al, al

		mov di, 32768
		dec di
		sets bl
		xor al, bl
		shl al, 1

		mov ch, 192
		sub ch, 214
		lahf
		test ah, 10h
		jz KHMYVAGH
		xor al, 1
	KHMYVAGH:
		shl al, 1

		mov dx, 64470
		add dx, 128
		setc bl
		xor al, bl
		shl al, 1

		mov edx, 1860391589
		sub edx, 1668870984
		setz bl
		xor al, bl
		shl al, 1

		mov edx, 2147483648
		dec edx
		sets bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov di, 44502
		add di, 11812
		setc bl
		xor al, bl
		shl al, 1

		mov dl, 255
		inc dl
		setz bl
		xor al, bl

		// Writing char 'A' to memory
		mov esi, dword ptr[dynamic_array]
		mov byte ptr[esi + 0], al

		// *** Creating char 'B' ***
		xor al, al

		mov cl, 194
		inc cl
		setz bl
		xor al, bl
		shl al, 1

		mov cl, 199
		sub cl, 26
		lahf
		test ah, 10h
		jz yMBeSYPU
		xor al, 1
	yMBeSYPU:
		shl al, 1

		mov si, 65535
		inc si
		sets bl
		xor al, bl
		shl al, 1

		mov dh, 1866711762
		dec dh
		setz bl
		xor al, bl
		shl al, 1

		mov dl, 166
		add dl, -74
		sets bl
		xor al, bl
		shl al, 1

		mov ch, 29
		add ch, 81
		lahf
		test ah, 10h
		jz vGmVaPuR
		xor al, 1
	vGmVaPuR:
		shl al, 1

		mov cx, 2423
		sub cx, 51320
		setc bl
		xor al, bl
		shl al, 1

		mov ch, 55
		sub ch, 226
		setz bl
		xor al, bl

		// Writing char 'B' to memory
		mov esi, dword ptr[dynamic_array]
		mov byte ptr[esi + 1], al

		// *** Creating char 'C' ***
		xor al, al

		mov cl, 248
		dec cl
		setp bl
		xor al, bl
		shl al, 1

		mov cx, 14184
		add cx, 30092
		lahf
		test ah, 10h
		jz iouafHCH
		xor al, 1
	iouafHCH:
		shl al, 1

		mov di, 3891806791
		dec di
		setz bl
		xor al, bl
		shl al, 1

		mov bh, 61
		add bh, 41
		setz bl
		xor al, bl
		shl al, 1

		mov di, 2036
		sub di, 319
		setc bl
		xor al, bl
		shl al, 1

		mov dh, 213
		sub dh, 127
		setc bl
		xor al, bl
		shl al, 1

		mov edx, 1772343999
		inc edx
		lahf
		test ah, 10h
		jz Ndrdkhii
		xor al, 1
	Ndrdkhii:
		shl al, 1

		mov edi, 2113416391
		add edi, 2181550905
		setz bl
		xor al, bl

		// Writing char 'C' to memory
		mov ebx, dword ptr[dynamic_array]
		mov byte ptr[ebx + 2], al

		// *** Creating char 'D' ***
		xor al, al

		mov esi, 205146773
		sub esi, 338501444
		lahf
		test ah, 10h
		jz RbYoRBTw
		xor al, 1
	RbYoRBTw:
		shl al, 1

		mov dh, 1
		dec dh
		setz bl
		xor al, bl
		shl al, 1

		mov ch, 18
		add ch, 235
		setp bl
		xor al, bl
		shl al, 1

		mov cl, 81
		sub cl, 51
		setc bl
		xor al, bl
		shl al, 1

		mov cl, 188
		add cl, -114
		sets bl
		xor al, bl
		shl al, 1

		mov cl, 159
		inc cl
		lahf
		test ah, 10h
		jz JomahUVN
		xor al, 1
	JomahUVN:
		shl al, 1

		mov dx, 53763
		inc dx
		setz bl
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

		mov dh, 228
		add dh, 26
		setp bl
		xor al, bl
		shl al, 1

		mov ecx, 3860999396
		add ecx, 3261983825
		setc bl
		xor al, bl
		shl al, 1

		mov bl, 239
		add bl, 7
		setc bl
		xor al, bl
		shl al, 1

		mov bh, 255
		inc bh
		sets bl
		xor al, bl
		shl al, 1

		mov bl, 38
		dec bl
		lahf
		test ah, 10h
		jz hOUhOreD
		xor al, 1
	hOUhOreD:
		shl al, 1

		mov dh, 1
		dec dh
		setz bl
		xor al, bl
		shl al, 1

		mov cl, 128
		dec cl
		sets bl
		xor al, bl
		shl al, 1

		mov ebx, 1907993546
		sub ebx, 1907993546
		setz bl
		xor al, bl

		// Writing char 'E' to memory
		mov ebx, dword ptr[dynamic_array]
		mov byte ptr[ebx + 4], al

		// *** Creating char 'F' ***
		xor al, al

		mov dx, 60849
		inc dx
		lahf
		test ah, 10h
		jz ZozpLqME
		xor al, 1
	ZozpLqME:
		shl al, 1

		mov dl, 255
		inc dl
		setz bl
		xor al, bl
		shl al, 1

		mov edi, 2424951073
		sub edi, 1963506737
		sets bl
		xor al, bl
		shl al, 1

		mov di, 3716
		add di, 61285
		setp bl
		xor al, bl
		shl al, 1

		mov bl, 230
		sub bl, 161
		lahf
		test ah, 10h
		jz WqtjquVT
		xor al, 1
	WqtjquVT:
		shl al, 1

		mov di, 5918
		sub di, 5918
		setz bl
		xor al, bl
		shl al, 1

		mov bl, 55
		dec bl
		setp bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl

		// Writing char 'F' to memory
		mov ecx, dword ptr[dynamic_array]
		mov byte ptr[ecx + 5], al

		// *** Creating char 'G' ***
		xor al, al

		mov di, 39230
		add di, 8484
		setz bl
		xor al, bl
		shl al, 1

		mov dl, 72
		dec dl
		setp bl
		xor al, bl
		shl al, 1

		mov esi, 1313252980
		add esi, 3874260087
		lahf
		test ah, 10h
		jz MlNHZicY
		xor al, 1
	MlNHZicY:
		shl al, 1

		mov cx, 32768
		dec cx
		sets bl
		xor al, bl
		shl al, 1

		mov dx, 36131
		sub dx, 31088
		setc bl
		xor al, bl
		shl al, 1

		mov esi, 2023866991
		sub esi, 2558314733
		sets bl
		xor al, bl
		shl al, 1

		mov edi, 577449973
		add edi, 3675457510
		sets bl
		xor al, bl
		shl al, 1

		mov bl, 0
		dec bl
		sets bl
		xor al, bl

		// Writing char 'G' to memory
		mov ecx, dword ptr[dynamic_array]
		mov byte ptr[ecx + 6], al

		// *** Creating char ' ' ***
		xor al, al

		mov ebx, 1648226363
		sub ebx, 1892818039
		setp bl
		xor al, bl
		shl al, 1

		mov cl, 188
		add cl, 176
		lahf
		test ah, 10h
		jz lFKincTN
		xor al, 1
	lFKincTN:
		shl al, 1

		mov dx, 62720
		inc dx
		lahf
		test ah, 10h
		jz MljryqwJ
		xor al, 1
	MljryqwJ:
		shl al, 1

		mov dh, 255
		inc dh
		sets bl
		xor al, bl
		shl al, 1

		mov cl, 228
		sub cl, 235
		setz bl
		xor al, bl
		shl al, 1

		mov di, 40558
		sub di, 17063
		sets bl
		xor al, bl
		shl al, 1

		mov esi, 3051469706
		sub esi, 2716751261
		sets bl
		xor al, bl
		shl al, 1

		mov edx, 2665457733
		add edx, 519460137
		setc bl
		xor al, bl

		// Writing char ' ' to memory
		mov ebx, dword ptr[dynamic_array]
		mov byte ptr[ebx + 7], al

	}

	std::cout << dynamic_array << std::endl;

	return 0;
}
