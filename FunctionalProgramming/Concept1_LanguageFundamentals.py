"""

When compared with other programming languages Python is very easy to learn
Python is a general purpose high level programming language
General purpose :- can be used to develop data analysis applications, web applications, desktop applications etc.,
Human understandable languages are called high level programming language

Python was developed by Guido Van Rossum in 1989

C and Java are statically typed programming language (the data type of the variable should be declared before using it)
Python is dynamically typed programming language (no need to declare the type of the variable before using it)
    Based on the value we assign to the variable the data type of the variable will be determined

Features of Python :-
---------------------

1. Simple and easy to learn
2. Freeware (no need to pay anything to use the software) and open source (we can see the source code of the
    functions and customize if we want to)
3. Python is both procedure oriented and object-oriented programming language
4. Python is interpreted programming language
5. Python has rich library support which makes it easy to code complex logics

Python3 doesn't provide backward compatibility to Python2 programs

print "Hello" -- valid in Python2 but invalid in Python3
long data type present in Python2 but not available in Python3

"""

import math  # math is called a module which is basically a group of functions, variables and classes
from random import *
import keyword as kw

print("Hello world in Python")
a, b = 10, 20
print(f"Sum of the {a} and {b} is :- {a + b}")
a, b, c, d, e = 100, 200, 300, 400, 500
print(f"Sum of the variables declared on the same line is :- {a + b + c + d + e}")
print(f"The type of the variable 'a' is :- {type(a)}")
a = True  # we can make the variable a point to a different type of value which is completely fine in Python
print(f"The value of the variable 'a' after assigning the 'True' value to it is :- {type(a)}")

print(f"square root of 10 is :- {math.sqrt(10)}")

# using the randint function present in random module to generate a four digit random number

for i in range(5):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep='')

"""

Identifiers :-
--------------
Any name in a Python program is called identifier
It can be a variable name, class name, function name etc.,

Rules to define an identifier :-
--------------------------------
1. The only allowed symbols are alphabets (both upper case and lower case), digits(0-9) and underscore(_)
2. Identifiers should not start with a digit
3. Python identifiers are case sensitive. total and TOTAL are two different variables
4. We can not use reserved words like if, else etc., as identifiers
5. There is no length limit for Python identifiers 

"""

total = 20
TOTAL = 200
print(f"total = {total}, TOTAL = {TOTAL}")

# If the identifier starts with underscore symbol it indicates that it is private
# If the identifier starts with two underscore symbols then it is strongly private
# If the identifier starts and ends with two underscore symbols then it is language specific identifier

print(f"All the keywords present in the current version of Python is :- {kw.kwlist}")

x = 10
print(f"The value of the variable x before deletion is {x}")
del x  # deleting the variable x so that it is eligible for garbage collection
# print(f"The value of the variable x after deletion is {x}")  # NameError: name 'x' is not defined
