"""
The below program explains about Tuple data structure
If we want to represent group of values as a single entity which is immutable where
    1. insertion order is preserved
    2. duplicates are allowed
    3. heterogeneous objects are allowed
then we should use tuple data structure
Tuples are represented using parentheses.
Read only version of list is tuple
"""

tuple1 = (10, 20, 30, 40)
print(f"The type of the variable tuple1 is {type(tuple1)} and the value is {tuple1}")
print(f"Accessing first element of tuple using +ve index :- {tuple1[0]}")
print(f"Accessing last element of tuple using -ve index :- {tuple1[-1]}")
sliced_tuple = tuple1[1:3]
print(f"sliced tuple = {sliced_tuple}")

print(f"Accessing the elements of a tuple using for loop")
for element in tuple1:
    print(element)

# tuple1[0] = 100 # TypeError: 'tuple' object does not support item assignment
print(f"The repetition operator on tuple1 is {tuple1 * 2}")

tuple1 = 10, 20, 30, 40, 50  # we are not required to pass the elements in parentheses for tuple
print(f"The type of the variable tuple1 is {type(tuple1)} and the values in it are :- {tuple1}")

tuple1 = (10)  # this is not treated as tuple instead it is treated as int
print(f"The type of the variable tuple1 is {type(tuple1)} and the value of it is :- {tuple1}")

tuple1 = (10,)  # the syntax to represent one valued tuple
print(f"The type of the variable tuple1 is {type(tuple1)} and the value of it is :- {tuple1}")

tuple1 = ()  # to create an empty list just open and close the parentheses
print(f"The type of the variable tuple1 is {type(tuple1)} and the value of it is :- {tuple1}")

# tuple function can be used to convert other sequences to tuple
print(f"tuple('dharani') = {tuple('dharani')}")
print(f"tuple([10,20,30,40]) = {tuple([10,20,30,40])}")
print(f"tuple(range(1,11,2) = {tuple(range(1,11,2))}")

# Important functions/methods of tuple
'''
1. len(tuple) -- to know the number of elements present in the tuple
2. t.count(element) -- to know the number of occurrences of the element in the tuple
3. t.index(element) -- to know the first index of the specified element in the tuple
                       If the specified element doesn't exist it will return ValueError
4. sorted(tuple) -- to sort the elements in the tuple
5. min(tuple) -- return the minimum element in the tuple
6. max(tuple) -- return the maximum element in the tuple
'''

tuple1 = (10,20,30,40,50,10)
print(f"The number of elements present in the tuple {tuple1} is : {len(tuple1)}")
print(f"The number of occurrences of the element 10 in the tuple1 is : {tuple1.count(10)}")
print(f"The number of occurrences of the element 90 in the tuple1 is : {tuple1.count(90)}")

search_element = 10
try:
    print(f"The index of the element {search_element} in the tuple1 is : {tuple1.index(search_element)}")
    search_element = 100
    print(f"The index of the element {search_element} in the tuple1 is : {tuple1.index(search_element)}")
except ValueError:
    print(f"The element {search_element} is not present in the tuple")

sorted_tuple = tuple(sorted(tuple1))  # since sorted method returns a list we are converting to tuple
print(f"sorted_tuple is : {sorted_tuple}")

sorted_tuple_desc = tuple(sorted(tuple1,reverse=True))
print(f"sorted_tuple_desc is : {sorted_tuple_desc}")

print(f"The minimum value element in the tuple is : {min(tuple1)}")
print(f"The maximum value element in the tuple is : {max(tuple1)}")

# Tuple packing and unpacking
a = 10
b = 20
c = 30
d = 40
t = a, b, c, d  # this is called tuple packing
print(f"The type of the variable t is {type(t)} and the value is {t}")

p, q, r, s = t # this is called tuple unpacking
print(f"The value of the variables p is {p}, q is {q}, r is {r} and s is {s}")

# we can apply packing and unpacking on any type of sequence

# Tuple comprehension is not supported
t = (x * x for x in range(1,11))
print(f"The type of the value t is {type(t)}")  # here the return type if generator not tuple
for x in t:
    print(x)

# Tuples can be used as keys for dictionary