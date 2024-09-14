"""

In Python programmer is responsible to create object and GC will take care of destroying the object
GC will remove unwanted/useless objects from memory
If objects doesn't have any reference variable then it is eligible for gc
We have a module named gc to customise garbage collection in our program

Destructor : named with __del__
Garbage collector will call destructor before destroying the object to perform some cleanup activities

"""

import sys
import time


class Test:
    def __init__(self, param):
        self.param = param

    def __del__(self):
        print("Destructor got executed")


t = Test("Ram")
print(f"The number of references for the object is : {sys.getrefcount(t)}")
# The above statement will return reference count as 2 because of the implicit self variable pointing to the object
t = None  # Once we assign t to None the Test() object previously created is eligible for GC
# Before destroying the object the destructor will get executed
print("sleeping for 10 seconds")
time.sleep(10)
print("End of application")
