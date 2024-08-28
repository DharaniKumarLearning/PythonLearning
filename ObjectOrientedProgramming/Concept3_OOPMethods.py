class ClassTest:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def weight_add(self):
        return self.weight + 100

    # Instance methods are mostly used when you want to produce an action that uses data inside the object
    def instance_method(self):  # Every method that has self as an argument is an instance method
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):  # creating a class method the parameter is the class variable
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static method")

    @classmethod
    def hardcover(cls, name, weight):
        return ClassTest(name, cls.TYPES[0], weight)

    @classmethod
    def paperback(cls, name, weight):
        return ClassTest(name, cls.TYPES[1], weight)

    def __str__(self):
        return f"ClassTest object with {self.name}, {self.book_type}, {self.weight} got created successfully"


test = ClassTest("Harry potter", "hardcover", 1500)
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()  # calling the class method
ClassTest.static_method()  # calling the static method
print(ClassTest.TYPES)  # Accessing the class variables
print(test.name)
test_1 = ClassTest.hardcover("Hardcover book - 1", 1400)
print(test_1)
test_2 = ClassTest.paperback("Paperback book-1", 1390)
print(test_2)


