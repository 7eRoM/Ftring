#include "pch.h"
#include <iostream>


int main()
{
	char static_array[8];

	__asm
	{

		// *** Creating char 'A' ***
		xor al, al

		mov cl, 225
		add cl, 9
		setc bl
		xor al, bl
		shl al, 1

		mov dl, 144
		dec dl
		lahf
		test ah, 10h
		jz RHpFexiD
		xor al, 1
		RHpFexiD:
		shl al, 1

		mov dh, 2
		inc dh
		setz bl
		xor al, bl
		shl al, 1

		mov edx, 803704434
		inc edx
		setp bl
		xor al, bl
		shl al, 1

		mov si, 27175
		sub si, 20613
		setz bl
		xor al, bl
		shl al, 1

		mov bl, 149
		add bl, 39
		setp bl
		xor al, bl
		shl al, 1

		mov dh, 59
		sub dh, 218
		lahf
		test ah, 10h
		jz IWsajNHQ
		xor al, 1
	IWsajNHQ:
		shl al, 1

		mov cx, 19329
		add cx, 16579
		setp bl
		xor al, bl

		// Writing char 'A' to memory
		mov byte ptr[static_array + 0], al


		// *** Creating char 'B' ***
		xor al, al

		mov bh, 231
		dec bh
		setp bl
		xor al, bl
		shl al, 1

		mov si, 32665
		inc si
		setp bl
		xor al, bl
		shl al, 1

		mov edx, 95790338
		add edx, 3377626285
		setc bl
		xor al, bl
		shl al, 1

		mov esi, 2598286386
		dec esi
		setp bl
		xor al, bl
		shl al, 1

		mov edx, 3426816507
		sub edx, 1655163896
		setc bl
		xor al, bl
		shl al, 1

		mov bl, 1762553890
		dec bl
		setz bl
		xor al, bl
		shl al, 1

		mov ebx, 336454216
		add ebx, 3411391724
		sets bl
		xor al, bl
		shl al, 1

		mov dh, 182
		inc dh
		setz bl
		xor al, bl

		// Writing char 'B' to memory
		mov byte ptr[static_array + 1], al


		// *** Creating char 'C' ***
		xor al, al

		mov ch, 104
		add ch, 140
		setp bl
		xor al, bl
		shl al, 1

		mov dl, 10
		sub dl, 72
		sets bl
		xor al, bl
		shl al, 1

		mov dx, 39785
		sub dx, 9596
		sets bl
		xor al, bl
		shl al, 1

		mov bh, 244
		sub bh, 146
		setp bl
		xor al, bl
		shl al, 1

		mov ch, 90
		sub ch, 168
		setz bl
		xor al, bl
		shl al, 1

		mov edi, 3938737555
		sub edi, 2288317187
		lahf
		test ah, 10h
		jz bFxbAGOk
		xor al, 1
	bFxbAGOk:
		shl al, 1

		mov dl, 1
		sub dl, 1
		setz bl
		xor al, bl
		shl al, 1

		mov edx, 0
		dec edx
		sets bl
		xor al, bl

		// Writing char 'C' to memory
		mov byte ptr[static_array + 2], al


		// *** Creating char 'D' ***
		xor al, al

		mov bx, 46340
		sub bx, 35770
		setz bl
		xor al, bl
		shl al, 1

		mov cl, 19
		add cl, 254
		lahf
		test ah, 10h
		jz SIOZAxwK
		xor al, 1
	SIOZAxwK:
		shl al, 1

		mov ch, 128
		dec ch
		sets bl
		xor al, bl
		shl al, 1

		mov dl, 128
		dec dl
		sets bl
		xor al, bl
		shl al, 1

		mov bh, 85
		sub bh, 193
		lahf
		test ah, 10h
		jz iJtOSNHj
		xor al, 1
	iJtOSNHj:
		shl al, 1

		mov ebx, 2124192713
		add ebx, 3426582157
		setp bl
		xor al, bl
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov dh, 2019837532
		dec dh
		setz bl
		xor al, bl

		// Writing char 'D' to memory
		mov byte ptr[static_array + 3], al


		// *** Creating char 'E' ***
		xor al, al

		mov edx, 2530793283
		sub edx, 1153677674
		setp bl
		xor al, bl
		shl al, 1

		mov dh, 15
		add dh, 192
		setp bl
		xor al, bl
		shl al, 1

		mov cl, 155
		dec cl
		lahf
		test ah, 10h
		jz zuNsYsfV
		xor al, 1
	zuNsYsfV:
		shl al, 1

		mov esi, 2898705489
		inc esi
		setz bl
		xor al, bl
		shl al, 1

		mov bl, 133
		add bl, 128
		lahf
		test ah, 10h
		jz qDOkSUTB
		xor al, 1
	qDOkSUTB:
		shl al, 1

		mov ch, 0
		dec ch
		sets bl
		xor al, bl
		shl al, 1

		mov ch, 255
		inc ch
		sets bl
		xor al, bl
		shl al, 1

		stc
		setc bl
		xor al, bl

		// Writing char 'E' to memory
		mov byte ptr[static_array + 4], al


		// *** Creating char 'F' ***
		xor al, al

		mov cl, 119
		dec cl
		setp bl
		xor al, bl
		shl al, 1

		mov ch, 254
		add ch, 177
		setc bl
		xor al, bl
		shl al, 1

		mov edi, 2204711093
		add edi, 1510475662
		setp bl
		xor al, bl
		shl al, 1

		mov bl, 202
		sub bl, 145
		sets bl
		xor al, bl
		shl al, 1

		mov cl, 71
		inc cl
		setz bl
		xor al, bl
		shl al, 1

		mov bl, 209
		add bl, 47
		setz bl
		xor al, bl
		shl al, 1

		mov bl, 197
		sub bl, 89
		lahf
		test ah, 10h
		jz jMVnHGUk
		xor al, 1
	jMVnHGUk:
		shl al, 1

		mov esi, 2221654487
		dec esi
		setz bl
		xor al, bl

		// Writing char 'F' to memory
		mov byte ptr[static_array + 5], al


		// *** Creating char 'G' ***
		xor al, al

		mov bl, 64
		add bl, 203
		setp bl
		xor al, bl
		shl al, 1

		mov bh, 130
		add bh, 126
		setz bl
		xor al, bl
		shl al, 1

		mov esi, 993301417
		dec esi
		setp bl
		xor al, bl
		shl al, 1

		mov dl, 147
		inc dl
		setz bl
		xor al, bl
		shl al, 1

		mov di, 1275706985
		dec di
		setz bl
		xor al, bl
		shl al, 1

		mov dl, 30
		sub dl, 254
		setc bl
		xor al, bl
		shl al, 1

		mov edi, 3901161328
		dec edi
		lahf
		test ah, 10h
		jz AnAGSdXb
		xor al, 1
	AnAGSdXb:
		shl al, 1

		mov esi, 1982766754
		sub esi, 3973862322
		setc bl
		xor al, bl

		// Writing char 'G' to memory
		mov byte ptr[static_array + 6], al


		// *** Creating char ' ' ***
		xor al, al

		mov bx, 18716
		add bx, 56771
		lahf
		test ah, 10h
		jz vgncyQEX
		xor al, 1
	vgncyQEX:
		shl al, 1

		mov ebx, 2147483648
		dec ebx
		sets bl
		xor al, bl
		shl al, 1

		mov bl, 203
		inc bl
		lahf
		test ah, 10h
		jz eOQHmMCC
		xor al, 1
	eOQHmMCC:
		shl al, 1

		clc
		setc bl
		xor al, bl
		shl al, 1

		mov cx, 65535
		inc cx
		sets bl
		xor al, bl
		shl al, 1

		mov dh, 0
		inc dh
		lahf
		test ah, 10h
		jz KqNtzWBa
		xor al, 1
	KqNtzWBa:
		shl al, 1

		mov edi, 2372219362
		add edi, 994455071
		setp bl
		xor al, bl
		shl al, 1

		mov cl, 3990191501
		dec cl
		setz bl
		xor al, bl

		// Writing char ' ' to memory
		mov byte ptr[static_array + 7], al


	}

	std::cout << static_array << std::endl;

	return 0;
}
