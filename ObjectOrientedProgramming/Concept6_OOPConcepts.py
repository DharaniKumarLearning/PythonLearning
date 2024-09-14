"""
How can we use members of one class inside another class:
    1. By using composition (Has-A relationship)
    2. By using inheritance (Is-A relationship)
"""


class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def get_car_info(self):
        print(f"Car name : {self.name}, Car color : {self.color}, Car model : {self.model}")


class Employee:
    def __init__(self, employee_num, employee_name, employee_car: Car):
        self.employee_num = employee_num
        self.employee_name = employee_name
        self.car = employee_car

    def get_employee_info(self):
        print(f"Employee number : {self.employee_num}")
        print(f"Employee name : {self.employee_name}")
        print(f"Employee car details")
        self.car.get_car_info()


c = Car("Tata", "Punch", "Red")
e = Employee(100, "John", c)
e.get_employee_info()

# In the above example Employee has a Car object created which will give us the functionality to use car features


class X:
    a = 10

    def __init__(self):
        self.b = 888
        print("Parent class constructor")

    def m1(self):
        print(f"Parent class instance method executed and the value of instance variable b is {self.b}")

    @classmethod
    def m2(cls):
        print(f"Parent class class method got executed and the value of static variable a is {cls.a} ")

    @staticmethod
    def m3():
        print("Parent class static method got executed")


class Y(X):  # this is called inheritance
    pass


# Once we create a child class using inheritance all the methods, variables and constructors also will be available for child class
y = Y()  # If no constructor defined in child class this will call the parent class constructor
# If constructor defined in child class then that constructor is called
print(y.a)  # Accessing the static variable 'a' of the parent class using child class object reference 'y'
y.m1()  # calling the instance method of parent class using child class object reference
y.m2()  # calling the class method of parent class using child class object reference
y.m3()  # calling the static method of parent class using child class object reference
print(f"The instance variable value of 'b' is {y.b}")


class Parent:
    a = 10

    def __init__(self):
        self.b = 777
        print("Parent class constructor invoked")

    def m1(self):
        print(f"Parent class instance method invoked : {self.b}")


class Child(Parent):
    a = 100

    def __init__(self):
        super().__init__()  # calling the parent class constructor
        self.c = 30
        print(f"Child class constructor invoked")
        print(f"The value of the variable a in super class is : {super().a}")

    def m1(self):
        super().m1()  # calling the parent class m1 method
        print(f"Child class instance method invoked : {self.c}")


c = Child()
print(f"The value of the static variable a in child class is : {c.a}")
c.m1()  # If the child class doesn't contain m1 method then the parent class m1 method will get executed
# If the child class contains the m1 method then the child class method gets the highest preference
# If the child class has a constructor then it is called otherwise parent class constructor will get called
# same goes with the destructor as well



