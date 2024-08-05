"""
Preventing the abnormal termination of a program is called exception handling
There are two types of errors.
    1. syntax error
    2. Runtime error also known as exceptions
Some unwanted, unexpected event which disturbs the normal execution flow of the program is called Exception
The purpose of exception handling is graceful termination of the program
Defining an alternate way to continue the rest of the program normally is the meaning of exception handling
Every exception in Python is a class
All exception classes are child class of BaseException directly or indirectly
"""

print("Hello")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Stupid how can you divide with zero")
print("Hi")

# Printing the exception information
try:
    print(10 / 0)
except ZeroDivisionError as msg:
    print(f"An exception got raised and its description is : {msg}")

# try with multiple except blocks
try:
    print(10 / 2)
    print(int("ten"))
except ZeroDivisionError:
    print("ZeroDivisionError exception occurred")
except ValueError:
    print("ValueError occurred")

# When we have multiple except blocks the execution order will be from top to bottom
# It means if we specify parent exception class first the bottom child class won't get executed

try:
    print(10 / 0)
    print(int("ten"))
except Exception:
    print("Some Exception occurred")
except ZeroDivisionError:
    print("ValueError occurred")

# the above code snippet will every time go into Exception class as it is the parent class for both
# ZeroDivisionError and ValueError

# single except block can handle multiple exceptions
try:
    print(10 / 2)
    print(int("ten"))
except (ZeroDivisionError, ValueError) as msg:
    print(f"{msg} exception occurred")

# default except block
try:
    print(10 / 1)
    print(int("ten"))
except ZeroDivisionError:
    print("ZeroDivisionError exception occurred")
except:
    print("Some exception occurred")

# The default except block must be specified at last otherwise we will get syntax error

# finally block
# If you want to execute some statement whether exception is occurred  or not then finally block is the best
# Even when the exception is not handled finally block will get executed

try:
    try:
        print(int("ten"))
    except ZeroDivisionError as msg:
        print(f"{msg} error occurred")
    finally:  # In this scenario where exception is not handled as well finally block will get executed
        print("Successfully completed the execution of the code snippet")
except ValueError:  # The internal exception is handled by the outer except block
    print("Internal exception is handled by the outside except block")

# situation where finally block won't get executed is when the python interpreter shuts down

# Nested try except block

try:
    print("Statement 1")
    print("Statement 2")
    print("Statement 3")
    try:
        print("Statement 4")
        print("Statement 5")
        print("Statement 6")
    except ZeroDivisionError:
        print("Statement 7")
    finally:
        print("Statement 8")
    print("Statement 9")
except ValueError:
    print("Statement 10")
finally:
    print("Statement 11")
print("Statement 12")

"""

case 1 :- If there is no exception then statements 1, 2, 3, 4, 5, 6, 8, 9, 11 and 12 will get executed with normal termination
case 2 :- If exception raised at statement 2 and the corresponding except block matched
          then statements 1, 10, 11, 12 will get executed with normal termination
case 3 :- If exception raised at statement 2 and the corresponding except block not matched then
          statements 1, 11 will get executed with abnormal termination
case 4 :- If exception raised at statement 5 and the corresponding inner except block matched then 
          statements 1, 2, 3, 4, 7, 8, 9, 11, 12 will get executed with normal termination
case 5 :- If exception raised at statement 5 and the corresponding inner except block not matched but the outer
          except block matched then statements 1, 2, 3, 4, 8, 10, 11, 12 will get executed with normal termination
case 6 :- If exception raised at statement 5 and the corresponding inner and outer except block not matched then 
          statements 1, 2, 3, 4, 8, 11 with abnormal termination
case 7 :- If exception raised at statement 7 and the corresponding outer except block matched then statements
          1, 2, 3, 4, 8, 10, 11, 12 will get executed with normal termination
case 8 :- If exception raised at statement 7 and the corresponding outer except block not matched then statements
          1, 2, 3, 4, 8, 11 with abnormal termination
case 9 :- If exception raised at statement 8 and the corresponding outer except block matched then statements
          1, 2, 3, 4, 5, 6, 10, 11, 12 will get executed with normal termination
case 10 :- If exception raised at statement 8 and the corresponding outer except block not matched then statements
          1, 2, 3, 4, 5, 6, 11 will get executed with abnormal termination
case 11 :- If exception raised at statement 9 and the corresponding except block matched then statements
           1, 2, 3, 4, 5, 6, 8, 10, 11, 12 with normal termination
case 12 :- If exception raised at statement 9 and the corresponding except block not matched then statements
           1, 2, 3, 4, 5, 6, 8, 11 with abnormal termination
case 13 :- If exception raised at statement 10 then statements 1, 11 will get executed with abnormal termination 
    
"""

# else block with try-except-finally
# else block will get executed when there is no exception
# finally block will get executed when there is an exception handled or not handled

try:
    print("try")
    print(10 / 1)
except ZeroDivisionError as msg:
    print(f"The exception {msg} occurred")
else:
    print("No exception occurred")
finally:
    print("Finally came here")

print(f"Various combinations of try/except/else/finally blocks")

"""
    1. try without except or finally is always invalid
    2. without try only except block is always invalid
    3. only else block is always invalid
    4. only finally block is always invalid
    5. try-except is always valid
    6. try-finally is always valid
    7. try-except-else is always valid
    8. try-else is always invalid. We can not have else block without except
    9. try-else-finally is always invalid
   10. try with multiple except blocks is always valid
   11. try-except-else-else is always invalid. We can have only one else block
   12. try-except-finally-finally is always invalid. We can have only one finally block
"""

"""
    There are two types of exceptions
        1. Predefined or inbuilt exceptions -- The exceptions raised by Python automatically
        2. User defined exceptions
"""

# Defining user defined exceptions


class TooYoungException(Exception):  # We are defining TooYoungException class as child class of Exception
    def __init__(self, arg):  # This is a constructor
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter your age : "))
if age > 60:
    raise TooOldException("You crossed the age to get married")
elif age < 18:
    raise TooYoungException("You are too young to get married")
else:
    print("Your age is correct...All the best")
