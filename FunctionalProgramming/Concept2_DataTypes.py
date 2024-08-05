"""

Data types represent the type of value present inside a variable
int, float, complex, bool, str, bytes, bytearray, range, list, tuple, set, frozenset, dict, None
In Python everything is an object

"""

# int data type is used to represent integral values
# int data type can be represented in four ways
# decimal form(0-9), octal form(0-7), binary form(0 and 1), hexadecimal form(0-9,A-F(both upper case and lowercase))

a = 10
print(f"The type of the variable a is :- {type(a)}")
print(f"The variable a is stored in {id(a)} memory location")

b = 1941426574260576507614075641076501645072640  # int data type only can hold huge values
print(f"The type of the variable b is :- {type(b)}")

# binary number representation starts with either 0b or 0B
binary_num1 = 0b1111
binary_num2 = 0B1010
print(f"binary_num1 = {binary_num1}, binary_num2 = {binary_num2}")

# octal number representation starts with either 0o or 0O
octal_num1 = 0o176
octal_num2 = 0O12
print(f"octal_num1 = {octal_num1}, octal_num2 = {octal_num2}")

# hexadecimal representation starts with either 0x or 0X
hex_num1 = 0xFace
hex_num2 = 0Xcafebabe
print(f"hex_num1 = {hex_num1}, hex_num2 = {hex_num2}")

# base conversion functions
# bin() -- convert any base to binary, oct() -- convert any base to octal, hex() -- convert any base to hexadecimal

print(f"converting decimal to binary : {bin(15)}")
print(f"converting octal to binary : {bin(0o1675)}")
print(f"converting hexadecimal to binary : {bin(0xbabe)}")

print(f"converting decimal to octal : {oct(100)}")
print(f"converting binary to octal : {oct(0b10101011)}")
print(f"converting hexadecimal to octal : {oct(0xcafe)}")

print(f"converting decimal to hexadecimal : {hex(1984174783)}")
print(f"converting binary to hexadecimal : {hex(0b111100101110101)}")
print(f"converting octal to hexadecimal : {hex(0o1635135617235153)}")

# float data type is used to represent floating point values

f1 = 123.456
print(f"The type of the variable f1 is {type(f1)} and the value in it is : {f1}")

f2 = 3.4e5  # another way of representing floating point literals
print(f"The value of the variable f2 is {f2} and the type of it is : {type(f2)}")

# complex numbers are represented in the form of a + bj where 'a' is called the real part and 'b' is called the imaginary part
# The value of 'j' is sqrt(-1) which means j^2 is equal to -1

complex_num1 = 10 + 20j
print(f"The type of the variable complex_num1 is {type(complex_num1)} and the value of it is : {complex_num1}")

# Extracting real and imaginary part of a complex number
# by default the real and imag functions will return the output in floating point number only
print(f"The real part of the complex number {complex_num1} is : {complex_num1.real}")
print(f"The imaginary part of the complex number {complex_num1} is : {complex_num1.imag}")

# The real and imaginary part of the complex numbers can be either int or floating point literals
complex_num2 = 10.5 + 20.6j
print(f"The type of the variable complex_num2 is {type(complex_num2)} and the value is : {complex_num2}")

# we can specify the real part of the complex number in binary, octal and hexadecimal form
# but the imaginary part can be specified in decimal form only
complex_num3 = 0o1452 + 45.8j
print(f"The type of the variable complex_num2 is {type(complex_num3)} and the value is : {complex_num3}")

# operations on complex numbers
print(f"Addition of complex numbers :- {complex_num1 + complex_num2}")
print(f"Subtraction of complex numbers :- {complex_num1 - complex_num2}")
print(f"Multiplication of complex numbers :- {complex_num1 * complex_num2}")

# The only allowed values for bool datatype are True and False
bool_value1 = True
print(f"The type of the variable bool_value1 is {type(bool_value1)} and the value of it is : {bool_value1}")

# Internally True and False are represented as 1 and 0 respectively hence we can perform some arithmetic operations
print(f"True + True = {True + True}")
try:
    print(f"True / False = {True / False}")
except ZeroDivisionError:
    print(f"We can not divide any number with zero")

# str data type is used to represent any sequence of characters
# we can represent single line string literals using single quotes or double quotes
# we can represent multi-line string literals using triple single quotes or triple double quotes

s1 = "Dharani"
print(f"The type of the variable s1 is {type(s1)} and the value of it is {s1}")
print(f"The repetition operator on string s1 :- {s1 * 4}")
print(f"The number of characters in the string s1 is :- {len(s1)}")  # len function will give us the length of the string

s2 = """Dharani
Kumar Gopavaram"""
print(f"The type of the variable s2 is {type(s2)} and the value of it is {s2}")

# int, float, bool, complex and str are known as fundamental data types

# Type casting :- converting from one data type to another is called type casting
# int(), float(), bool(), complex(), str() are the functions used in type casting

# int() function can be used to convert other data type to int data type
print(f"Converting float to int :- {int(123.456)}")
print(f"Converting bool to int :- {int(True)}")

# print(f"Converting complex number to int :- {int(10+20j)}")  # TypeError: can't convert complex to int
# we can not convert complex number to int

try:
    print(f"Converting the string value which is of decimal form to int :- {int('100')}")
    print(f"Converting the string value which is of float form to int :- {int('10.5')}")
except ValueError:
    print("While converting string to int the string value should be of decimal form only")

# Different ways of converting binary, octal and hexadecimal string to int
print(f"Converting binary string to int :- {int('0b1111',2)}")
print(f"Converting octal string to int :- {int('0o1314134112',8)}")
print(f"Converting hexadecimal string to int :- {int('0xcafebabe',16)}")

# float() function can be used to convert other data types to float
print(f"Converting int to float :- {float(10)}")
print(f"Converting boolean to float :- {float(True)}")
# print(f"Converting complex to float :- {float(10+20j)}") # TypeError: can't convert complex to float

try:
    print(f"Converting string which is of decimal form to float :- {float('100')}")
    print(f"Converting string which is of float form to float :- {float('10.5')}")
    print(f"Converting string value which is of alphabets to float :- {float('package1')}")
except ValueError:
    print("While converting string to float the string should be of either decimal or float data type")

# complex() function can be used to convert other data types to complex
# It is an overloaded function which has two forms
# complex(x) --> x + 0j
# complex(x, y) --> x + yj

print(f"Converting int to complex using first form of complex function :- {complex(10)}")
print(f"Converting float to complex using first form of complex function :- {complex(10.5)}")
print(f"Converting bool to complex using first form of complex function :- {complex(False)}")
print(f"Converting string decimal value to complex using first form of complex function :- {complex('10')}")
print(f"Converting string float value to complex using first form of complex function :- {complex('10.6')}")

print(f"Converting int to complex using the second form of complex function :- {complex(10, 20)}")
print(f"Converting bool to complex using the second form of complex function :- {complex(True, True)}")
print(f"Converting float to complex using the second form of complex function :- {complex(10.8, 20.9)}")

# print(f"Converting string to complex using the second form of complex function :- {complex('10','20')}")
# The above statement will throw the error :- TypeError: complex() can't take second arg if first is a string

# bool function can be used to convert other data type to bool
# for int data type if the value is 0 bool function returns False else returns True

print(f"Converting non-zero positive int value to bool :- {bool(10)}")
print(f"Converting non-zero negative int value to bool :- {bool(-10)}")
print(f"Converting the int value 0 to bool :- {bool(0)}")

# for float data type if the value yields to 0 bool function returns False else returns True
print(f"Converting float value 0.05 to bool :- {bool(0.05)}")
print(f"Converting float value 0.0 to bool :- {bool(0.0)}")

# for string data type if the length of the string is 0 bool function returns False else returns True
print(f"Converting string value 'Dharani' to bool :- {bool('Dharani')}")
print(f"Converting string value '' to bool :- {bool('')}")

# Escape characters in string
print("using the new line escape character :- 'Dharani\nGopavaram'")
print(f"using the tab separated escape character :- 'Dharani\tGopavaram'")

# int, float, bool, str are immutable data types
# Once we create an object we can not perform any change to that object
# If we try to perform change then by default a new object will be created with the required changes
# Immutability mainly provides object reusability

# bytes data type is used to represent group of byte numbers just like an array
# bytes data type is immutable we can not modify once we create it

x = [100, 101, 102, 103, 104]
b = bytes(x)
print(f"The type of the variable b is {type(b)} and the value of it is : {b}")
print(f"Accessing the first element of the bytes date type using the index 0 : {b[0]}")
print(f"Accessing the last element of the bytes data type using the index -1 : {b[-1]}")
print(f"Using slice operator on bytes data type : {b[0:3]}")

print(f"Printing the values in the bytes data type using for loop")
for val in b:
    print(val, end=',')
print()

# since bytes data type is immutable we can not modify the values once we create
# b[0] = 30  # TypeError: 'bytes' object does not support item assignment

try:
    y = [100, 200, 256]
    b = bytes(y)
except ValueError:
    print("bytes data type accepts value in the range(0,256) even 256 is not allowed")

# bytearray is same as bytes the only difference bytearray is mutable whereas bytes is immutable

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ba = bytearray(x)
print(f"The type of the variable ba is {type(ba)}")
ba[0] = 97  # this is possible because bytearray is mutable
print("The values present in the bytearray variable after modifying is : ", end='')
for val in ba:
    print(val, end=',')
print()

# None data type is used to represent the absence of a value of null value
# It is often used to signify that variable or function does not have meaningful result or value


def f1():
    pass  # pass keyword is used to define a function without a body


print(f"The return value from the f1 function is : {f1()}")
# There are no constants in Python
