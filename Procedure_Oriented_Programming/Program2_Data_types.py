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

# bool datatype :- The only allowed values are True and False
bool_val1 = True
print(f'The value of the variable bool_val1 is {bool_val1} and the type of it is {type(bool_val1)}')

# Internally True and False are represented as 1 and 0 respectively hence we can perform some arithmetic operations
print(f'True + True = {True + True}')
print(f'True * False = {True * False}')
# print(f'True / False = {True / False}')  # ZeroDivisionError: division by zero

# str datatype is used to represent any sequence of characters
# We can represent single line string literals using single quotes or double quotes
# We can represent multi-line string literals using triple single quotes or triple double quotes

s1 = 'Dharani'
print(f'The value of the variable s1 is {s1} and the type of it is {type(s1)}')
print(f'The repetition operator on strings {s1 * 4}')
print(f'The length of the string s1 is :- {len(s1)}')  # len method will give us the length of the string

s2 = '''Dharani
Kumar Gopavaram'''
print(f'The value of the variable s2 is {s2} and the type of it is {type(s2)}')

# int, float, complex, bool and str are known as fundamental data types

# Type casting :- converting from one data type to another is called type casting
# Type casting functions :- int(), float(), bool(), complex(), str()

# int() function can be used to convert any other data type to int data type
print(f'int(123.456) = {int(123.456)}')  # float to int conversion
print(f'int(True) = {int(True)}')  # bool to int conversion
print(f'int(False) = {int(False)}')
print(f'int("10") = {int("10")}')  # string to int conversion

# print(f' int("10.5") = {int("10.5")}')  # ValueError: invalid literal for int() with base 10: '10.5'
# If we want to convert string literal to int the string value should be of base 10(decimal form) only
# print(f' int("Dharani") = {int("Dharani")}')  # ValueError: invalid literal for int() with base 10: 'Dharani'

# Different way of converting binary, octal, hexadecimal string to int
print(f'int("0b111",2) = {int("0b111", 2)}')
print(f'int("0o123",8) = {int("0o123", 8)}')
print(f'int("0xFace",16) = {int("0xFace", 16)}')

# float() function can be used to convert other data type to float
print(f'float(10) = {float(10)}')  # int to float conversion
print(f'float(True) = {float(True)}')
print(f'float("10") = {float("10")}')
print(f'float("10.78") = {float("10.78")}')
# print(f' float("Dharani") = {float("Dharani")}')  # ValueError: could not convert string to float: 'Dharani'

# bool() function can be used to convert other data type to bool
print(f'bool(-123) = {bool(-123)}')
print(f'bool(0) = {bool(0)}')  # For int literals if the value is 0 bool() returns False otherwise returns True
print(f'bool(0.01) = {bool(0.01)}')
print(f'bool(0.0) = {bool(0.0)}')  # If the final value of float is 0 then bool() returns False else True
print(f'bool("Dharani") = {bool("Dharani")}')
print(f'bool("") = {bool("")}')  # If the string literal is empty bool() returns False else True

# str() function can be used to convet other data type to string
print(f'str(10) = {str(10)}')
print(f'str(10.5) = {str(10.5)}')
print(f'str(True) = {str(True)}')
print(f'str(False) = {str(False)}')

# int, float, complex, bool, str are immutable data types
# Once we create an object we can not perform any change to the object
# If we try to perform changes then by default a new object will be created with the required changes
# Immutability mainly provides object re-usability

# bytes datatype is used to represent a group of byte numbers just like an array
# bytes data type is immutable we can not modify once we create

sample_list = [10, 20, 30, 40]
bytes_values = bytes(sample_list)
print(f'The type of the variable bytes_values is {type(bytes_values)}')
print(f'Accessing 1st element from bytes_values variable using index :- {bytes_values[0]}')
print(f'Accessing last element from bytes_values variable using negative index :- {bytes_values[-1]}')
print(f'All the values present in bytes_values variable are :- ')
for val in bytes_values: # we can use for loop on bytes data type like this
    print(val)

# bytes_values[0] = 100  # TypeError: 'bytes' object does not support item assignment
# Since bytes data type is immutable if we try to change a value we get Error

# bytes data type values must be in the range(0,256)
y = [100, 200, 300]
# b = bytes(y)  # ValueError: bytes must be in range(0, 256)

# bytearray is same as bytes the only difference is bytearray is mutable
x = [1, 2, 3, 4]
bytearray_var1 = bytearray(x)
print(f'The type of the variable bytearray_var1 is {type(bytearray_var1)}')
print(f'Accessing 1st element from bytearray_var1 variable using index :- {bytearray_var1[0]}')
print(f'Accessing last element from bytearray_var1 variable using negative index :- {bytearray_var1[-1]}')
print(f'Modifying the first element of bytearray variable')
bytearray_var1[0] = 100
print(f'The elements in bytearray_var1 after modifying is :-')
for val in bytearray_var1:
    print(val)

# None data type is used to represent the absence of a value or a null value
# It is often used to signify that variable or a function does not have a meaningful value or result


def f1():
    pass  # pass keyword is used to define a function which does not do anything


print(f'The return value from the function f1 is {f1()}')
# There are no constants in Python
