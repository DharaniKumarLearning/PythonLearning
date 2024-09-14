"""
Executing several tasks simultaneously is called multitasking
In general in ay programming language there are two types of multitasking
    1. Process based multitasking -- Executing several tasks simultaneously where each task is a
            separate independent process. Very rarely used mainly used by OS
    2. Thread based multitasking -- Executing several tasks simultaneously where each task is a
            separate independent part of same program.
            Each independent part of the program is called a Thread
    We can reduce execution time and improve performance because of the above multitasking types

Every Python program by default contains one thread which is called Main Thread
"""

import threading


def display():
    for x in range(10):
        print(f"This code got executed by :- {threading.current_thread().getName()}")


print(f"This code executed by {threading.current_thread().getName()}")  # To know the name of the current thread that is executing

# There are 3 ways to create to created Thread in Python
# 1. Creating a thread without using any class
# 2. Creating a thread by extending Thread class
# 3. Creating a thread without extending Thread class

t = threading.Thread(target=display)  # Main Thread creates the child thread objects
# child thread object is responsible to execute the display method
t.start()  # MainThread starts child thread

for i in range(10):
    print(f"This code executed by {threading.current_thread().getName()}")


# In the above program we can't predict the output since both the threads gets executed simultaneously

# One sample output
"""
This code executed by MainThread
This code got executed by :- Thread-1
This code got executed by :- Thread-1
This code got executed by :- Thread-1
This code got executed by :- Thread-1
This code got executed by :- Thread-1
This code got executed by :- Thread-1
This code got executed by :- Thread-1
This code executed by MainThread
This code executed by MainThread
This code got executed by :- Thread-1
This code got executed by :- Thread-1This code executed by MainThread
This code executed by MainThread
This code executed by MainThread
This code executed by MainThread
This code executed by MainThread
This code executed by MainThread
This code executed by MainThread
This code got executed by :- Thread-1

This code executed by MainThread
"""