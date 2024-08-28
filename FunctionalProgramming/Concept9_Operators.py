"""
Different types of operator in Python.
    1. Arithmetic operator (+, -, *, /, &, %, //(floor division operator), **(exponential operator)
    2. Relational or comparison operator (>, <, >=, <=, ==, !=)
    3. Logical operators (and, or, not)
    4. Bitwise operators (&, |, ^, ~, <<, >>)
    5. Assignment operators (+=, -=, *= ...)
    6. Special operator (is, is not, in, not rin)
"""

print(f"Normal division operator : 10 / 3 = {10 / 3}")  # normal division operator will always return the result in float only
print(f"Floor division operator : 20 // 3 = {20 // 3}")  # floor division operator will return int if both the numbers are int
print(f"Floor division operator : 20.0 // 3 = {20.0 // 3}")  # floor division operator will return float if either number is float
print(f"Exponential operator : {2 ** 10}")  # 2 ^ 10 = 1024

# + operator can be applied on strings when applied on strings it is called concatenation operator
# both the arguments to + operator should be string if any of the argument is not string we get TypeError

print(f"'Dharani ' + 'Kumar' = {'Dharani ' + 'Kumar'}")
# print('Dharani' + 3)  # TypeError: can only concatenate str (not "int") to str
print(f"String repetition operator : {'Dharani' * 3}")

# We can apply relational operators on strings as well
# When we apply relational operators on string they work based on alphabetical order

a = 'package1'
b = 'kavya'
print(f"{a} > {b} = {a > b}")
print(f"{a} < {b} = {a < b}")
print(f"{a} >= {b} = {a >= b}")
print(f"{a} <= {b} = {a <= b}")

# print(10 > "Dharani")  # TypeError: '>' not supported between instances of 'int' and 'str'
# Logical operators on non-boolean types
# 0 means False, non-zero means True, empty string is false

# x and y if evaluates to False result is x else result is y
print(f"10 and 20 = {10 and 20}")
print(f"'' and 'Dharani' = {'' and 'Dharani'}")

# x or y -- if x evaluates to True result is x else result is y
print(f"10 or 20 = {10 or 20}")
print(f"0 or 20 = {0 or 20}")
print(f"10 or 10 / 0 = {10 or 10 / 0}")  # here 10 / 0 is not evaluated because the first expression determines the result
# Logical operators are short-circuited meaning if the first expression determines the result the second one is not evaluated

print(f"not 10 = {not 10}")
print(f"not '' = {not ''}")

# Bitwise operators
# & -- if both bits are 1 then 1 else 0
# | -- if any bit is 1 then 1 else 0
# ^ -- if both bits are different then 1 else 0
# << -- bitwise left shift operator
# >> -- bitwise right shift operator

print(f"4 & 5 = {4 & 5}")
print(f"4 | 5 = {4 | 5}")
print(f"4 ^ 5 = {4 ^ 5}")
print(f"4 << 2 = {4 << 2}")
print(f"10 >> 2 = {10 >> 2}")

# There are no increment (++x, x ++) and decrement (--x, x--) operators in Python

# Ternary operator syntax in Python
# x = firstValue if condition else secondValue

x = 10 if 20 > 30 else 40
print(f"The value of the variable x determined using ternary operator is : {x}")

y = 30 if 10 < 20 else 50
print(f"The value of the variable y determined using ternary operator is : {y}")

# is operator is used to perform address comparison of two variables

a = (10, 20, 30)
b = (10, 20, 30)
print(f"id(a) = {id(a)}, id(b) = {id(b)}")
print(f"a is b = {a is b}")
print(f"a is not b = {a is not b}")

# in operator is used to check whether an element is present in the collection or not

sample_list = [10, 20, 30, 40]
print(f"sample_list = {sample_list}")
print(f"10 in sample_list = {10 in sample_list}")
print(f"100 in sample_list = {100 in sample_list}")
print(f"100 not in sample_list = {100 not in sample_list}")
print(f"'s' in 'python' = {'s' in 'python'}")
