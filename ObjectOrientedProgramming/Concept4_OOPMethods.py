"""
1. instance methods:
    Instance methods are object related methods
    Inside method body if we are accessing instance variables then that method talks about a particular
        object such type of methods are called instance methods.
    Instance methods should be called by using object reference
    Getter and Setter methods are also instance methods which are helpful in setting and getting value of instance variables
    Normally we should not access variables outside class instead we should use getter and setter methods to set and get instance variables
    Getter methods are also known as accessor methods
    Setter methods are also known as mutator methods

2. Class methods:
    These methods are very rarely used
    Inside method body if we are using only static variables then that method is called class method

3. Static methods:
    If we are not using any instance or static variables then that methods are called static methods
    These methods just take a set of parameters and perform some business logic on it
    These methods are also known as general utility methods
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Hi {self.name}")
        print(f"Your marks are {self.marks}")

    def grade(self):
        if self.marks >= 65:
            print("You passed in first grade")
        elif self.marks >= 50:
            print("You passed in second grade")
        elif self.marks >= 35:
            print("You passed in third grade")
        else:
            print("You failed")


s1 = Student("Ram", 36)
s2 = Student("Sunny", 90)
s1.display()
s1.grade()
s2.display()
s2.grade()

# Instead of using constructor we can use getter and setter methods to access and create instance variables


class Police:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category


p1 = Police()
p1.set_name("Robert")
print(p1.get_name())
p1.set_name("Sunny")
print(p1.get_name())
p1.set_category("DCP")
print(p1.get_category())
print(p1.__dict__)


class Animal:
    legs = 4

    @classmethod
    def walk(cls, name):
        print(f"{name} walks with {cls.legs}")


Animal.walk("Cat")
Animal.walk("Dog")

# Program to know the number of objects created for class


class Village:
    count = 0

    def __init__(self):
        Village.count += 1

    @classmethod
    def no_of_objects(cls):
        print(f"The total number of objects for the class village is : {cls.count}")
        print(f"The total number of objects for the class village is : {Village.count}")


v1 = Village()
v2 = Village()
Village.no_of_objects()


class SomeMath:
    @staticmethod
    def add_num(x, y):  # this is a static method
        print(f"The sum is {x + y}")

    @staticmethod
    def product_num(x, y):  # We are not using any static or instance variables inside this method
        print(f"The product is {x * y}")


SomeMath.add_num(10, 20)
SomeMath.product_num(10, 20)

# Passing members of one class to another class


class Employee:
    def __init__(self, employee_num, employee_name, employee_sal):
        self.employee_num = employee_num
        self.employee_name = employee_name
        self.employee_sal = employee_sal

    def display(self):
        print(f"The employee {self.employee_name} has the employee number {self.employee_num}"
              f"and he is earning {self.employee_sal} salary per month")


class Manager:
    @staticmethod
    def modify_employee(emp: Employee):  # this method is taking parameter as an employee object and calling its methods
        emp.employee_sal += 1000  # Incrementing the salary of employee by 1000
        emp.display()  # calling the display method of the employee class


e = Employee(100, "Ram", 10000)
Manager.modify_employee(e)  # passing the employee object to the modify_employee method

