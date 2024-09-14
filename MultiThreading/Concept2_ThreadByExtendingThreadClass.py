import threading


class MyThread(threading.Thread):  # Inheritance
    def run(self):   # overriding the run method in Thread class
        for i in range(10):  # The code in run method will get executed by the Thread
            print(f"This code got executed by thread : {threading.current_thread().getName()}")


t = MyThread()  # MainThread creating the child thread object
t.start()  # MainThread starting child thread

for x in range(10):
    print(f"This code executed by thread : {threading.current_thread().getName()}")