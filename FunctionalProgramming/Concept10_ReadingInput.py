"""
Python 2 has two functions to read input from the user
    1. raw_input() -- input is treated as string we need to explicit type casting
    2. input() -- input is treated as whatever the type we provided no type casting is needed

Python3 has only one function from the user
    1. input() -- input is always treated as string we need to explicit type casting if we want
"""

from math import pi

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
maximum_num = a if a > b and a > c else b if b > c else c
print(f"The maximum value of the 3 numbers you entered is : {maximum_num}")

r = int(input("Enter the radius of the circle : "))
print(f"Area of the circle is : {pi * (r ** 2)}")

# Reading multiple values from the user in a single line

a, b = [int(num) for num in input("Enter two numbers separated by comma : ").split(',')]
print(f"The sum of the numbers entered on the same line : {a + b }")

# eval function is used to evaluate an expression dynamically

result = eval("10 + 20 + 30")
print(f"The result after evaluating the expression using eval is : {result}")

data = eval(input("Enter some data : "))
print(f"The type of the variable data is {type(data)} and the value of it is {data}")
