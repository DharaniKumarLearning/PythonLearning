import threading


class MyThread:
    def __init__(self):
        self.a = 10

    def display(self):
        for i in range(10):
            print(f"This code executed by {threading.current_thread().getName()} and the value of "
                  f"instance variable a is {self.a}")


m = MyThread()

# Creating multiple threads
t1 = threading.Thread(target=m.display)  # passing the target as instance method to Thread
t2 = threading.Thread(target=m.display)
t3 = threading.Thread(target=m.display)
t4 = threading.Thread(target=m.display)

# starting all the threads
t1.start()
t2.start()
t3.start()
t4.start()

for x in range(10):
    print(f"This code executed by {threading.current_thread().getName()}")