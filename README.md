# Ftring
Ftring: Flag-Based String Generator, a c++ string obfuscator.


## What is Ftring?

Ftring is an obfuscator which generates a string based on cpu flags including
1. CF (Carry Flag)
2. OF (Overflow Flag)
3. SF (Sign Flag)
4. ZF (Zero Flag)
5. AF (Auxiliary Carry Flag)
6. PF (Parity Flag)

A string consists of one/multiple char(s). A char is a byte. A byte consists of 8 bits. In Ftring, each bit will be generated by cpu flags.



## Features
* There is no need to use enc/dec routine to hide strings
* There is no embedded string in output exe file
* The embedded string extraction tools such as Strings cannot find any string
* Overwrite the memory of variable whenever there is no need to use it anymore



## How to use?

```console
> Ftring.py --version
Ftring v0.1.0


> Ftring.py -h
usage: Ftring.py [-h] [--version] -r VAR -l VAL -t {s,d}

Flag-Based String Generator, a C++ string obfuscator.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -r VAR, --var VAR     varable name
  -l VAL, --val VAL     a string would be assigned to the variable
  -t {s,d}, --type {s,d}
                        type of variable: static array or dynamic array
```

### Example: Static array

Here is a sample C++ code of a static array:
```C++
#include "pch.h"
#include <iostream>

int main()
{
	char static_array[8];
	strncpy_s(static_array, "ABCDEFG", (sizeof(static_array) / sizeof(char)) - 1);
	
  std::cout << static_array << std::endl;

	return 0;
}
```

Now, Fstring comes into play.
In order to generate a static array of a string:
```console
python "Ftring.py" --var "static_array" --val "ABCDEFG" -t "s"
```

Now it`s time to change the old assignment section to the new one like as follows:
```C++
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

```




### Example: Dynamic array

Here is a sample C++ code of a dynamic array:
```C++
#include "pch.h"
#include <iostream>

char *dynamic_array = new char[8];
int main()
{
	strncpy_s(dynamic_array, 8, "ABCDEFG", 8);

  std::cout << dynamic_array << std::endl;
	
	return 0;
}
```

Now, Fstring comes into play.
In order to generate a dynamic array of a string:
```console
python "Ftring.py" --var "dynamic_var" --val "ABCDEFG" -t "d"
```

Now it`s time to change the old assignment section to the new one like as follows:
```C++
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

```




## History
### v0.1.0 / Feb 2019
* String generation based on carry flag
* Supports C++ static and dynamic arrays

### Ongoing
* String generation based on Overflow Flag, Sign Flag, Zero Flag, Auxiliary Carry Flag and Parity Flag
* Add more methods to set or reset the aforementioned flags
* Generate a routine to overwrite the memory of variable whenever there is no need to use it anymore



