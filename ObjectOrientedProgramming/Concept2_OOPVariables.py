"""
1. Instance Variables :
    If the value of a variable varies from object to object such type of variables are called instance
        variables or object related variables
    For every object a separate copy of instance variables will get created
    In general instance variables are declared inside constructor using self
    Within the class we can access instance variables using self but outside the class we can access them using reference variable
    Instance variables can be declared inside instance method using self
    Instance variables can be declared outside the class using reference variables

2. Static Variables:
    If the value of a variable doesn't vary from object to object then we should declare such type of
        variable as a static variable
    Only one copy of static variable will get created for all the objects
    We can access static variable by using class name or object reference but highly recommended to use class name
    We can declare static variables inside constructor using class name
    We can declare static variables inside instance method by using class name
    We can declare static variables inside class method by using cls variable or class name
    We can declare static variables inside static method by using class name
    We can modify static variable either by using class name or by using cls variable if it is class method
    If we are trying to modify static variable value by using object reference then static variable value
        won't be modified instead it will create a new instance variable
    We can delete static variable by using del class_name.variable_name or del cls.variable_name if we try to delete
        using object reference or self we get error

3. Local variables:
    Local variables are variables which we declare inside a method for temporary purpose
    The scope of the local variable will be gone once the method execution is complete
"""


class Student:
    student_college = "Degree College"  # this is a static variable

    def __init__(self, student_no, student_name, student_marks):
        self.student_no = student_no  # declaring a instance variable
        self.student_name = student_name
        self.student_marks = student_marks

    def display(self):
        print(f"Student number : {self.student_no}")  # accessing instance variable inside class
        print(f"Student name : {self.student_name}")
        print(f"Student marks : {self.student_marks}")

    def m1(self, student_age, student_height):  # declaring instance variable inside instance method
        self.student_age = student_age
        self.student_height = student_height
        del self.student_no


s1 = Student(100, "John", 90)

print("Accessing instance variable outside class using reference variable")
print(f"Student name = {s1.student_name}")  # accessing instance variable outside class

print("All the instance variables present for the s1 object")
print(s1.__dict__)  # __dict__ shows all the instance variables an object has and the values associated with it

print("calling the display method to display all the instance variables present in the object")
s1.display()

s1.student_addr = "Hyd"  # creating one more instance variable outside class using reference variable
s1.m1(47, 6.3)  # After calling this method we will have two more instance variables for the s1 object
print(s1.__dict__)

del s1.student_name  # deleting an instance variable outside class using reference variable
print(s1.__dict__)

print(f"Accessing static variable using class name : {Student.student_college}")
Student.student_college = "Waste college"  # modifying the value of a static variable outside class using class name
print(f"Accessing static variable using object reference : {s1.student_college}")

s2 = Student(102, "Ram", 98)
print(f"The instance variables present for the object s2 is : {s2.__dict__}")
print(f"Student college = {s2.student_college}")

s2.student_name = "Sunny"  # If the instance variable already exists it will override the value
# If the instance variable doesn't exist it will create a new instance variable
print(f"The instance variables present in the object s2 is : {s2.__dict__}")

# Some examples of static variables


class Test:
    a = 10  # this is a static variable

    def __init__(self):
        self.b = 20
        Test.c = 30  # this declares a static variable
        print(f"self.a = {self.a}")
        print(f"Test.a = {Test.a}")

    def m1(self):  # Inside an instance method we can access static variables using self and class name
        self.d = 40  # this will create an instance variable
        Test.e = 50  # this will create a static variable
        print(f"self.a = {self.a}")
        print(f"Test.a = {Test.a}")

    @classmethod
    def m2(cls):  # This is a class method
        cls.f = 60
        Test.g = 70
        # Inside a class method we can access static variables using cls and class name
        print(f"cls.a = {cls.a}")
        print(f"Test.a = {Test.a}")

    @staticmethod
    def m3():  # this is a static method no cls or self as first argument
        Test.h = 80
        # inside a static method we can access static variables using class name
        print(f"Test.a = {Test.a}")


t1 = Test()
t2 = Test()
t1.m1()  # this method will create one more static variable and one instance variable
t2.m1()
Test.m2()  # this method will create two more static variables
Test.m3()  # calling the static method using class name
# We can call the static method and class method using object reference as well but highly recommended to use class name
print(f"The instance variables in t1 object is : {t1.__dict__}")
print(f"The static variables present in the class is : {Test.__dict__}")
Test.i = 90
print(f"t1 : {t1.a}, {t1.b}, {t1.c}, {t1.d}, {t1.e}, {t1.f}, {t1.g}, {t1.h}, {t1.i}")
print(f"t2 : {t2.a}, {t2.b}, {t2.c}, {t2.d}, {t2.e}, {t2.f}, {t2.g}, {t2.h}, {t2.i}")
Test.a = 888  # modifying the static variable using class name
Test.e = 999
t1.b = 999  # modifying the instance variable
print(f"t1 : {t1.a}, {t1.b}, {t1.c}, {t1.d}, {t1.e}, {t1.f}, {t1.g}, {t1.h}, {t1.i}")
print(f"t2 : {t2.a}, {t2.b}, {t2.c}, {t2.d}, {t2.e}, {t2.f}, {t2.g}, {t2.h}, {t2.i}")
print(f"The static variables present in the class is : {Test.__dict__}")
# We can view all the static variables on the class by calling __dict__ method on class name


class Check:
    a = 10

    def __init__(self):
        self.b = 20


c1 = Check()
c2 = Check()
c1.a = 888  # we can not modify static variable using object reference
# In the above statement we are creating new instance variable for c1 object
c1.b = 999
print(f"c1 : {c1.a}, {c1.b}")
print(f"c2 : {c2.a}, {c2.b}")
print(c1.__dict__)  # {'b': 999, 'a': 888} here the variable 'a' is an instance variable
print(c2.__dict__)


class Check1:
    a = 10

    def __init__(self):
        self.a = 888


c = Check1()
print(Check1.a)  # prints the static variable 'a' of the class Check1
print(c.a)  # prints the instance variable 'a' of object c


class Check2:
    a = 10

    def __init__(self):
        self.b = 20
        print(self)  # self always points to the current object

    @classmethod
    def m1(cls):
        cls.a = 888  # modifying the value of static variable 'a'
        cls.b = 999
        print(cls)  # cls always points to current class


c1 = Check2()
c2 = Check2()
c1.m1()
print(f"c1 : {c1.a}, {c1.b}")
print(f"c2 : {c2.a}, {c2.b}")
print(f"Check2 : {Check2.a}, {Check2.b}")






