# range data type represents a sequence of numbers which are always immutable

r = range(1, 10)
print(f"The type of the variable r is {type(r)} and it's value is : {r}")

# We can access the values in range data type using index, slice operator, for loop
print(f"Accessing the 4th element in the range data type using index 3 : {r[3]}")
sliced_range = r[0:5]
print(f"sliced_range : {sliced_range}")

# r[0] = 10  # TypeError: 'range' object does not support item assignment

for i in r:
    print(i, end=',')
print()

# If we want range of values from different start and end you need to pass two arguments to range function

print("Second form of range function")

r1 = range(11, 21)
for i in r1:
    print(i, end=',')
print()

print("Third form of range function")

r2 = range(10, 101, 5)  # print every 5th value in between the range we specify
for i in r2:
    print(i, end=',')
print()

r3 = range(10, 0, -1)  # If we pass negative value to step function it will print the values in reverse order
for i in r3:
    print(i, end=',')
print()

