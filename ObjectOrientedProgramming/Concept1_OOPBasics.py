class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_1 = Student("Dharani", (90, 90, 89, 90, 78))  # when we create an object the __init__(constructor) method runs
print(student_1.name)  # accessing the field of an object
print(student_1.grades)
print(student_1.average())  # calling the average method of student object
print(Student.average(student_1))  # another way of calling the average method

student_2 = Student("Shiv", (80, 90, 100, 87, 85, 67))
print(student_2.name)
print(student_2.grades)
print(student_2.average())
print(Student.average(student_2))
