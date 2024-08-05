"""
Generators in Python are a powerful tool for creating iterators
They allow you to iterate over a potentially large sequence of data without creating the entire sequence in memory at once
This can be more memory-efficient and faster compared to traditional approaches, especially when dealing with large datasets
"""


# The below code will cause memory issues because the entire data gets saved in memory
# sample_list = [x * x for x in range(99999999999999999999999999)]


sample_generator = (x * x for x in range(99999999999999999999999999))  # does not cause memory issues
# The values are generated on the fly without using much memory
print(f"The type of the variable sample_generator is {type(sample_generator)}")

# yield keyword is used to return a generator from a function


def sample_function():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'


result = sample_function()
print(f"The type of the variable result is : {type(result)}")
print(f"The next value present in the result generator is : {next(result)}")  # next method can be used to retrieve next value

# We can use while loops like this to iterate over the generators

while True:
    try:
        print(f"The next value present in the result generator is : {next(result)}")
    except StopIteration:
        break

for value in result:  # this for loop doesn't print anything because the generator is already consumed
    print(value)
print("A generator is lost once it is consumed")


def count_down(num: int):
    while num >= 0:
        yield str(num)
        num -= 1


values = count_down(10)
print(f"The type of the variables values is : {type(values)}")
print(f"All the values returned by the count_down function are : {','.join(values)}")


# Program to print first 100 fibonacci numbers using generators
def fibonacci_series():
    a, b = 0, 1
    i = 0
    while i <= 100:
        yield a
        a, b = b, a + b
        i += 1


fb_series = fibonacci_series()
for val in fb_series:
    print(val)
