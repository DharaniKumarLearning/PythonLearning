"""
Class : blueprint or plan or design
Object : Physical existence of a class is an object
Reference variable : The variable which is used to access or operate an object is called reference variable
Class can contain some attributes which are defined using variables
Class can contain some actions or behaviors which are defined using methods
"""


class Student:
    """This is the student class which contains all the variables and methods related to student objects"""

    student_college = "Engineering College"
    # the above line declares a static variable which is available across all objects

    def __init__(self, sno, name, marks):  # this is a constructor which is used to initialise an object
        self.sno = sno  # here we are declaring an instance variable
        self.name = name  # anything that starts with self is an instance variable
        self.marks = marks

    # If we don't write any constructor then Python by default will generate a constructor.
    # constructor will be executed automatically when we are creating the object
    # constructor will be executed only once per object
    # constructor will be executed to declare and initialise instance variables of an object

    def display(self):  # self is a reference variable to the current object
        print(f"Student_number : {self.sno}, Student_name : {self.name}, Student_marks : {self.marks}")

    # self can be used to access instance variables and instance methods
    # self is the first parameter in constructor and instance methods


s1 = Student(1, "John", 98)
s2 = Student(2, "Ram", 96)

print(f"The type of the variable s1 is {type(s1)}")
print(f"The name of the s1 student is : {s1.name}")

print(s1.sno, s1.name, s1.marks)
print(s2.sno, s2.name, s2.marks)
# Instead of printing the values present in the instance variables like this
# We can create an instance method in the class

s1.display()
s2.display()

print(Student.__doc__)  # We can access the docstring of the class using __doc__
help(Student)

print(Student.student_college)  # we can use class name to access static variable
print(s1.student_college)  # we can use object reference as well to access static variable


class Test:
    def __init__(self, n='', m=0):  # this way of declaring constructor will help us to create objects in different ways
        self.var1 = n
        self.var2 = m

    def display(self):
        print(f"Hi {self.var1}")
        print(f"You have {self.var2} score")


t1 = Test()  # calling constructor with no arguments
t1.display()

t2 = Test("Dharani")  # calling constructor with one argument
t2.display()

t3 = Test("John", 100)  # calling constructor with two arguments
t3.display()



