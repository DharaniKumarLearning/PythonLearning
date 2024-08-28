import math
import os as o  # giving alias name for the imported module
import random
import UserDefinedModule.dharani_math_module as dmm  # a module will be imported only once no matter how many times you import it
import time
from importlib import reload

print(f"Using sqrt function present in math module to get the sqrt of 10 : {math.sqrt(10)}")
print(f"Getting the value of by accessing the pi variable present in math module : {math.pi}")
print(f"Checking whether a file exists or not using function present in os module")
print(o.path.exists("/Users/dharanikumar/Downloads/check.txt"))

print(f"dmm.x = {dmm.x}")
print(f"dmm.y = {dmm.y}")
dmm.add_num(100, 200)
dmm.product_num(100, 200)

print("Program entering into sleep for 2 seconds")
time.sleep(2)
reload(dmm)  # If your user defined module has new changes you can use reload function present in importlib module
print(f"dmm.x = {dmm.x}")
print(f"dmm.y = {dmm.y}")

print(f"The members in the current module is {dir()}")  # will return the members present in the current module
print(f"The members present in the math module is : {dir(math)}")  # will return the members present in the math module
print(f"The detailed description of every method present in the math module can be viewed using help method")
help(math)

# use of the special variable __name__
# __name__ variable will help us figure out how the function call got executed
# Is it directly as a file or as a module from some other program

dmm.f1()

# some important functions present in math module
print(f"math.sqrt(4) = {math.sqrt(4)}")  # returns floating point value
print(f"math.ceil(10.1) = {math.ceil(10.1)}")  # returns the next integer value
print(f"math.floor(10.9) = {math.floor(10.9)}")  # returns the previous integer value
print(f"math.fabs(-10.1) = {math.fabs(-10.1)}")  # returns the absolute value which will ignore the sign
print(f"math.fabs(10.1) = {math.fabs(10.1)}")  # fabs means float absolute value

# working with functions present in random module.
# random module contain several function which are useful to generate random numbers

print(f"random.random() = {random.random()}")  # will generate random float number between 0 and 1 (not inclusive)
print(f"random.randint(1, 100) = {random.randint(1, 100)}")
# randint function will randomly generate integer b/w the numbers we pass(inclusive)
print(f"random.uniform(1, 2) = {random.uniform(4, 9)}")
# uniform function will generate random float numbers b/w the numbers we pass (not inclusive)

print(f"random.randrange(10) = {random.randrange(10)}")  # will generate random integer number b/w 0 and 9
print(f"random.randrange(30,45) = {random.randrange(30, 45)}")  # will generate random int b/w 30 and 44
print(f"random.randrange(1, 11, 2) = {random.randrange(1, 11, 2)}")
# The above print statement will return random number picked from 1, 3, 5, 7, 9

sample_list = [10, 20, 30, 40, 'Dharani']
print(f"sample_list = {sample_list}")
print(f"Using choices method present in the random module : {random.choices(sample_list)}")
# the return type of the choices method is list

print(f"random element in the list is : {random.choice(sample_list)}")
print(f"random element in the string is : {random.choice('Dharani')}")
# We can not pass set to choice method because set objects are not indexed

# generate random password of length 6 where 1, 3, 5 are characters and 2, 4, 6 are digits
for i in range(6):
    print(chr(random.randrange(65, 90)), random.randint(0, 9), chr(random.randrange(65, 90)),
          random.randint(0, 9), chr(random.randrange(65, 90)), random.randint(0, 9), sep='')
