print(f"This is an user defined module")

x = 777
y = 8880


def add_num(a, b):
    print(f"The sum of {a} and {b} is : {a + b}")
    print("Completed sum")


def product_num(a, b):
    print(f"The product of {a} and {b} is : {a * b}")
    print(f"Completed product")


def f1():
    if __name__ == "__main__":
        print(f"The code executed directly as a program")
        print(f"The value of the variable __name__ is : {__name__}")
    else:
        print(f"The code executed indirectly as a module from some other program")
        print(f"The value of the variable __name__ is : {__name__}")


f1()
