"""
Function is a group of statements which can be reused
It is the best reusable component of a program
Even functions are objects in Python
"""

from functools import reduce


def wish():  # we need to use def keyword to define a function
    print("Good Evening")


wish()  # calling the wish function
wish()  # once we define the function we can call the function any number of times


def wish(name):  # we can define a function which accepts parameters
    print(f"Hello {name}, Good Morning!")


wish("Dharani")  # calling the function by passing one argument
wish("Shiv")


# Python doesn't have overloaded functions


def square_it(num):  # Here num is called the formal parameter of a function
    print(f"The square of the number {num} is {num * num}")


square_it(10)  # here 10 is called the actual argument to the function
print(square_it(100))  # The default return value of a function is None


def add_numbers(a, b):  # defining a function with return keyword
    return a + b


print(f"add_numbers(100, 200) = {add_numbers(100, 200)}")
print(f"add_numbers(1000, 2000) = {add_numbers(1000, 2000)}")


# Write a function to find the factorial of a given number


def factorial(n):
    factorial_result = 1
    while n >= 2:
        factorial_result *= n
        n -= 1
    return factorial_result


for i in range(5, 15):
    print(f"The factorial of the number {i} is {factorial(i)}")


# In Python a function can return multiple values


def sum_sub(a, b):  # defining a function which returns multiple values
    return a + b, a - b


x, y = sum_sub(10, 20)
print(f"The sum of the numbers is : {x}")
print(f"The subtraction of the numbers is : {y}")


def calculator(n1, n2):
    num_sum = n1 + n2
    num_sub = n1 - n2
    num_mul = n1 * n2
    num_div = n1 // n2
    return num_sum, num_sub, num_mul, num_div


t = calculator(100, 50)  # the return value of a function are stored in a tuple
print(f"The type of the variable t is : {type(t)}")
print(f"The values returned from the function are : ", end='')

for x in t:
    print(x, end=',')
print()

# Types of argument to a functions

"""
    1. Positional arguments :- default arguments where order is important
    2. Keyword arguments :- where order is not important
    3. Default arguments
    4. Variable length arguments
    5. Keyword variable length arguments
"""


def wish(name, msg="Hi"):  # defining a function which have a default argument
    print(f"{msg}, {name}")


wish("Dharani", "Hello")  # positional arguments
wish(msg="Hi", name="Dharani")  # keyword arguments order is not important
wish("Dharani", msg="Bye")  # We can add both positional and keyword arguments at the same time


# If we are passing both positional and keyword arguments then positional arguments should come first
# wish(name="Dharani", "Hi")  # SyntaxError: positional argument follows keyword argument
# wish("Dharani", name="Dharani")  # TypeError: wish() got multiple values for argument 'name'


def sum_num(n1, n2=0, n3=0):  # default arguments should be defined at the end of the function
    return n1 + n2 + n3


print(f"sum_num(10, 20, 30) = {sum_num(10, 20, 30)}")
print(f"sum_num(10) = {sum_num(10)}")
print(f"sum_num(100, 30) = {sum_num(100, n3=30)}")


# Variable length arguments


def sum_multiple_num(*num):
    print(f"The type of the variable num is : {type(num)}")  # The var-args variable is a tuple
    return sum(num)


print(f"Calling the sum_multiple_num function with no arguments : {sum_multiple_num()}")
print(f"Calling the sum_multiple_num function with one argument : {sum_multiple_num(10)}")
print(f"Calling the sum_multiple_num function with two arguments : {sum_multiple_num(10, 20)}")
print(f"Calling the sum_multiple_num function with five arguments : {sum_multiple_num(100, 200, 300, 400, 500)}")


def multiply(n1, n2, n3):
    return n1 * n2 * n3


sample_list = [10, 20, 30]
print(f"calling multiply function : {multiply(*sample_list)}")
# expanding the values in a dictionary to pass it to a list

sample_dict = {"n1": 10, "n2": 20, "n3": 30}
print(f"calling the multiply function by passing dictionary : {multiply(**sample_dict)}")
# while passing a dictionary to a function the parameters to the function and the keys of the dictionary should be same


def student_sum(*marks, name):
    print(f"The sum of the marks of the student {name} is : {sum(marks)}")


student_sum(10, 20, 30, 40, name="Dharani")
student_sum(100, 200, 300, 400, name="Kavya")


# keyword variable length arguments


def display(**student_details):
    print(f"The type of the variable student_marks is : {type(student_details)}")
    for k, v in student_details.items():
        print(f"{k} -> {v}")


display(name="Dharani", age=30, marks=98)
display(name="Shiv", age=45, marks=100, gender='Male')

# A module is a group of classes, functions and variables saved to a file
# A group of modules saved inside a folder is called package
# A group of packages is called Library

# Types of variables in Python
# Global variables :- Variables defined outside a function are called global variables.
#   Global variables are accessible to all the functions in the module
# Local variables :- Variables defined inside a function are called local variables
#   We can not access local variable defined inside one function in another function

global_var = 10


def f1():
    global global_var  # If we specify like this from now on it will be a global variable
    # We are not required to have a global variable defined while using global keyword
    global_var = 777  # changing the value of the global variable
    print(f"The global variable value is : {global_var}")


def f2():
    global_var = 888  # this is local variable
    print(f"The local variable value global_var is : {global_var}")
    print(f"The global variable value global_var is : {globals()['global_var']}")
    # In the above line we are accessing global variable using globals() dictionary


f2()
f1()
f2()

# Anonymous functions
# Sometimes we can define functions without name such type of nameless functions are called anonymous functions
# Syntax of anonymous function :- lambda input_parameter_list : expression
# Anonymous functions are useful when we want to pass functions as arguments to another function
# Some examples of function which accept functions as arguments are :- filter(), map(), reduce()

print(f"Using the anonymous function to know the square of a number : {(lambda n: n * n)(99)}")
print(f"Using the anonymous function to know the double of a number : {(lambda n : n * 2)(87)}")
print(f"Using the anonymous function to know the largest of two numbers : {(lambda n1, n2 : n1 if n1 > n2 else n2)(100,20)}")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Syntax of filter() function :- filter(lambda function, sequence)

# filter() using normal function as an argument
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Filtering out the even values in the sequence : {list(filter(is_even, sample_list))}")

# filter() function using anonymous function
print(f"Filtering out the even values in the sequence : {list(filter(lambda n: n % 2 == 0, sample_list))}")

# map() function using anonymous function
print(f"Doubling the values in the sequence using map function :- {list(map(lambda n: n * 2, sample_list))}")

sample_words_list = ["package1", "shiv", "ravi"]
print(f"Returning a tuple using map function :- {list(map(lambda w: (w.title(), len(w)), sample_words_list))}")

# We can apply map function on multiple sequences
# map function will automatically terminate when all the values in any sequence are completed

sample_list_1 = [10, 20, 30, 40, 50, 60, 70]
sample_set_1 = {10, 20, 30, 40, 60}
print(f"map function on multiple sequences :- {list(map(lambda n1, n2: n1 + n2, sample_list_1, sample_set_1))}")

# reduce function
result = reduce(lambda n1, n2: n1 + n2, sample_set_1)
print(f"The result of the reduce function with anonymous function is : {result}")


def add_num(n1, n2):
    return n1 + n2


result = reduce(add_num, sample_set_1)
print(f"The result of the reduce function with normal function is : {result}")

# Function aliasing


def original_func(name):
    print(f"Hello {name}")


duplicate_func = original_func  # creating the alias for the original func
print(f"The address of the variable original_func is : {id(original_func)}")
print(f"The address of the variable duplicate_func is : {id(duplicate_func)}")
print(f"Calling the duplicate_func function")
duplicate_func("Dharani")

del original_func  # If the object has any variable pointing to it and even if we delete the variable the object will still be there
duplicate_func("Dharani")

# Nested functions
# Function inside a function is known as nested function


def outer():
    print("Outer function execution started")

    def inner(num1, num2):
        print("Inner function execution started")
        print(f"The sum of the two numbers is : {num1 + num2}")
        print(f"The product of the two numbers is : {num1 * num2}")
        print("Inner function execution completed")

    inner(100, 200)
    inner(1000, 2000)
    inner(10000, 20000)

    print("Outer function execution completed")


outer()  # calling the outer function

# A function can return another function as well


def outer_func():
    print("Outer function execution started")

    def inner_func():
        print("Inner function got executed")

    print("Outer function returning inner function")
    return inner_func


return_func = outer_func()  # calling the outer function
return_func()  # calling the inner function

# Function decorators :- Used to extend the functionality of the existing function
# without changing the function logic if you want to play with function parameters then we can use decorators.
# Decorators provide a clean and reusable way to extend the functionality of the function without modifying the function code directly


# Let's say for the below greet function if Sunny is passed as a parameter we should print different output
def greeting_decor_func(func):
    def inner_decor_func(func_param: str) -> None:
        if func_param == "Sunny":
            print(f"Hello Sunny Bad Morning")
        else:
            func(func_param)
    return inner_decor_func


@greeting_decor_func  # implicitly calling the decorator of the greet function
def greet(name: str) -> None:
    print(f"Hello {name} Good morning")


greet('Dharani')
greet('Sunny')
greet('Bunny')


# Explicitly calling the decorator function
def sum_of_two_number_decor(func):
    def inner_sum_decor(func_param_1: int, func_param_2: int):
        if func_param_1 > 100:
            return -1
        else:
            return func(func_param_1, func_param_2)
    return inner_sum_decor


def sum_of_two_numbers(a: int, b: int) -> int:
    return a + b


print(f"calling sum_of_two_numbers function normally = {sum_of_two_numbers(101, 200)}")
decor_func = sum_of_two_number_decor(sum_of_two_numbers)
print(f"calling sum_of_two_numbers function through a decorator = {decor_func(101, 200)}")


# one more example of using decorators
def smart_division(func):
    def inner_smart_decor(fp1: int, fp2: int):
        if fp2 == 0:
            print("Hello Stupid how can you divide with zero")
            return -1
        else:
            return func(fp1, fp2)
    return inner_smart_decor


@smart_division
def division(a: int, b: int) -> int:
    return a // b


print(f"calling division function with parameters 100 and 10 : {division(100, 10)}")
print(f"calling division function with parameters 100 and 0 : {division(100, 0)}")


# We can have multiple decorators for a single function this is called decorator chaining
def sample_function_decor_2(func):
    def inner_decor_2(fp: str):
        print("sample_function_decor_2 execution started")
        func(fp)
        print("sample_function_decor_2 execution completed")
    return inner_decor_2


def sample_function_decor_1(func):
    def inner_decor_1(fp: str):
        print("sample_function_decor_1 execution started")
        func(fp)
        print("sample_function_decor_1 execution completed")
    return inner_decor_1


@sample_function_decor_2  # This decorator will get executed at last
@sample_function_decor_1  # This decorator will get executed first and the result is passed to next decorator
def sample_function(name):
    print(f"Hello {name} Good Morning")


sample_function("Dharani")
# The execution of multiple decorators is like this : sample_function_decor_2(sample_function_decor_1(sample_function))
