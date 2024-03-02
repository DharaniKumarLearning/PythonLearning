"""

Some theory about Python Programming Language :-
------------------------------------------------

When compared with other programming languages Python is very easy to learn
Python is a general purpose high level programming language
General purpose :- can be used to develop data analysis applications, web-application, desktop applications etc.,
Human understandable languages are high level programming languages

Python was developed by Guido Van Rossam in 1989 while working at National Research Institute in netherlands
Officially Python was made available to public in Feb 20th, 1991

C and Java are statically typed programming language (the variable type should be declared before using it)
Python is dynamically typed programming language (no need to declare type of variable before using it)
    Based on the value we assign to the variable the type of the variable will be determined

Features of Python :-
---------------------

1. Simple and easy to learn
2. Freeware(no need to pay anything to use the software) and open source(we can see the
source code of the functions and customise it if we want to)
3. Python is both procedure oriented and object-oriented programming language
4. Python is interpreted programming language
5. Python has rich library support which makes it easy to code complex logics

Python Versions :-
-------------------

Python 1.0 introduced in Jan 1994
Python 2.0 introduced in October 2000
Python 3.x introduced in December 2008 -- highly recommended to use this version

In general any new s/w version should provide backward compatibility for older version programs.
Python 3.x doesn't provide backward compatibility for older version programs.

print "Hello" -- valid in Python 2.0 but invalid in Python 3.x
long data type is present in Python 2 but not available in Python 3.x

"""

import math  # math is called a module which is basically a group of functions, variables and classes
from random import *
import keyword

print('Hello World in Python')
a, b = 10, 20  # we can declare multiple variables on the same line
print(f'Sum of {a} and {b} is :- {a + b}')
a, b, c, d, e = 100, 200, 300, 400, 500
print(f'Sum of the variables declared in the same line is : {a+ b + c + d + e}')

print(f'The type of the variable a is : {type(a)}')
a = True  # we can make a variable point to a different point of object which is perfectly fine
print(f'The type of the variable after pointing to a different type of object is : {type(a)}')

print(f'Square root of the number 90 is :- {math.sqrt(90)}')
print(f'Using randint function to generate six digit random number')

for i in range(1,10):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
          , randint(0, 9), randint(0, 9), sep='')

"""

Identifiers in Python :-
------------------------

Any name in Python program is called identifier.
It can be a variable name, function name, class name etc.,

Rules to define an identifier :-
--------------------------------

1. The only allowed symbols are alphabets(both uppercase and lowercase), digits(0-9) and underscore(_).
2. Identifiers should not start with a digit.
3. Python identifiers are case sensitive. total and TOTAL are two different variables.
4. We can not use keywords(reserved words) like if, else ,def, class etc., as identifiers.
5. There is no length limit for Python identifier.

"""

total, TOTAL = 100, 200
print(f'The value of the total is {total}')
print(f'The value of the TOTAL is {TOTAL}')

# If the identifier starts with underscore symbol it indicates that it is private
# If the identifier starts with two underscore symbols then it is strongly private
# If the identifier starts and ends with two underscore symbols then it is language specific identifie

print(f'All the keywords present in the current version of Python are :- {keyword.kwlist}')

x = 10
print(f'The value of x is {x}')
del x  # deleting the variable so that it is eligible for garbage collection
# print(f'The value of x after deletion is {x}')  # NameError: name 'x' is not defined
