class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # str method is used to print the objects in a neat form
        return f"Person object {self.name}, {self.age} years old created successfully"

    def __repr__(self):  # used to create unambiguous representation of the object
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Dharani", 30)
print(bob)  # <__main__.Person object at 0x102adc1c0> before implementing the __str__ method
print(bob.__repr__())
