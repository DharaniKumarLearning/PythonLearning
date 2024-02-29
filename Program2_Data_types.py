"""

This program explains about data types in Python
Data types represent type of data present inside a variable
int, float, complex, bool, str, bytes, bytearray, range, list, tuple, set, frozenset, dict, None

In Python everything is an object

"""

# int data type is used to represent integral values
int_num1 = 10
print(f'The type of the variable int_num1 is :- {type(int_num1)}')
print(f'The variable int_num1 is stored in {id(int_num1)} memory location')

# int datatype can hold huge values as well
int_num2 = 10431591351397451035130754103746031640136503174530175013745103
print(f'The type of the variable int_num2 is :- {type(int_num2)}')

"""

int data type can be represented in 4 ways.
    1. Decimal form(base10 -- allowed digits are 0 to 9)
    2. Binary form(base2 -- allowed digits are 0 and 1)
    3. Octal form(base8 -- allowed digits are 0 to 7)
    4. Hexadecimal form(base16 -- allowed characters are 0-9,a,b,c,d,e,f(both uppercase and lowercase)

"""

# binary number representation starts with either 0b or 0B
binary_num1 = 0b1111
binary_num2 = 0B1010
print(f'binary_num1 :- {binary_num1}')
print(f'binary_num2 :- {binary_num2}')

# octal number representation starts with either 0o or 0O
octal_num1 = 0o10
octal_num2 = 0O111
print(f'octal_num1 :- {octal_num1}')
print(f'octal_num2 :- {octal_num2}')

# Hexadecimal representation starts with either 0x or 0X
hexadecimal_num1 = 0x12
hexadecimal_num2 = 0XA2
print(f'Hexadecimal_num1 :- {hexadecimal_num1}')
print(f'Hexadecimal_num2 :- {hexadecimal_num2}')

# Base conversion functions
# bin() -- convert any base to binary
# oct() -- convert any base to octal
# hex() -- convert any base to hexadecimal

print(f'converting decimal to binary: {bin(15)}')
print(f'converting octal to binary: {bin(0o10)}')
print(f'converting hexadecimal to binary: {bin(0x10)}')

print(f'converting decimal to octal: {oct(15)}')
print(f'converting binary to octal: {oct(0b1111)}')
print(f'converting hexadecimal to octal: {oct(0x10)}')

print(f'converting decimal to hexadecimal: {hex(15)}')
print(f'converting binary to hexadecimal: {hex(0b1111)}')
print(f'converting octal to hexadecimal: {hex(0o1234)}')

# float data type is used to represent floating point values
float_num1 = 123.456
print(f'The type of the variable float_num1 is {type(float_num1)}')

float_num2 = 3.5e4  # another way of representing floating point numbers
print(f'The type of the variable float_num2 is {type(float_num2)}')
print(f'The value of the variable float_num2 is {type(float_num2)}')

# complex numbers are represented in the format of a + bj where 'a' is called real part and 'b' is called imaginary part
# The value of j is sqrt(-1) which means j^2 = -1

complex_num1 = 10 + 20j
print(f'The value of the variable complex_num1 is {complex_num1} and the type of it is : {type(complex_num1)}')

# Extracting real and imaginary part of a complex number
# Internally both real and imag will return the output in floating point number only
print(f'The value of real part of complex_number {complex_num1} is {complex_num1.real}')
print(f'The value of imaginary part of complex_number {complex_num1} is {complex_num1.imag}')

# The real and imaginary part can be either int of floating point literals
complex_num2 = 10.5 + 20.6j
print(f'The value of the variable complex_num2 is {complex_num2} and the type of it is : {type(complex_num2)}')
