"""

If we want to represent group of values as a single entity which is immutable where

    1. insertion order is preserved
    2. duplicates are allowed
    3. heterogeneous objects are allowed

then we should use tuple data structure
Tuples are represented using parentheses
Read only version of list is tuple

"""

sample_tuple = (10, 20, 30, 40)
print(f"The type of the variable sample_tuple is : {type(sample_tuple)} and it's value is : {sample_tuple}")

# We can access the elements of the tuple using index, slice operator, for loop and while loop
print(f"Accessing the first element of the tuple using index 0 : {sample_tuple[0]}")
print(f"Accessing the last element of the tuple using index -1 : {sample_tuple[-1]}")
sliced_tuple = sample_tuple[0:3]
print(f"sliced_tuple : {sliced_tuple}")

# sample_tuple[1] = 100  # TypeError: 'tuple' object does not support item assignment
print(f"The repetition operator on tuple :- {sample_tuple * 2}")

no_paren_tuple = 10, 20, 30, 40, 50  # we are not required to pass the elements in parentheses for tuple
print(f"The type of the variable no_paren_tuple is : {type(no_paren_tuple)} and it's value is : {no_paren_tuple}")

not_a_tuple = (10)  # this is not considered as a tuple instead it is treated as int
print(f"The type of the variable not_a_tuple is : {type(not_a_tuple)} and it's value is : {not_a_tuple}")

single_val_tuple = (10,)  # The syntax to declare a one valued tuple
print(f"The type of the variable single_val_tuple is : {type(single_val_tuple)} and it's value is : {single_val_tuple}")

empty_tuple = ()  # To create an empty tuple just open and close parentheses like this
print(f"The type of the variable empty_tuple is : {type(empty_tuple)} and it's value is : {empty_tuple}")

# tuple function can be used to create a tuple out of other collections
print(f"tuple('Dharani') : {tuple('Dharani')}")  # converting string to tuple
print(f"tuple([10,20,30,40]) : {tuple([10, 20, 30, 40])}")  # converting list to tuple
print(f"tuple(range(1,11,2) : {tuple(range(1,11,2))}")

# Important methods of tuple
# len(tuple) -- to know the number of elements present in the tuple
# t.count(element) -- to know the number of occurrences of the element inside the tuple
# t.index(element) -- to know the first index of the specified element in the tuple
#       If the specified element doesn't exist the index method returns ValueError

sample_tuple = (10, 20, 30, 40, 50, 10)
print(f"The number of elements present in the tuple {sample_tuple} is : {len(sample_tuple)}")
print(f"The number of times the element 10 is present in the tuple {sample_tuple} is : {sample_tuple.count(10)}")
print(f"The number of times the element 90 is present in the tuple {sample_tuple} is : {sample_tuple.count(90)}")

search_element = 30
try:
    print(f"The index of the element {search_element} in the tuple is : {sample_tuple.index(search_element)}")
    search_element = 90
    print(f"The index of the element {search_element} in the tuple is : {sample_tuple.index(search_element)}")
except ValueError:
    print(f"The {search_element} is not present in the tuple {sample_tuple}")

# sorted function can be used to sort the elements in the list

sorted_tuple = sorted(sample_tuple)  # sorted method returns a list
print(f"sorted_tuple : {sorted_tuple}")

# min(tuple) -- returns the minimum value element of the tuple
# max(tuple) -- returns the maximum value element of the tuple

print(f"The minimum value element in the tuple is : {min(sample_tuple)}")
print(f"The maximum value element in the tuple is : {max(sample_tuple)}")

# Tuple packing and unpacking

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d  # this is called tuple packing
print(f"The type of the variable t is {type(t)} and its value is : {t}")

p, q, r, s = t  # this is called tuple unpacking
print(f"p : {p}, q : {q}, r : {r}, s : {s}")

m, n, _, p = t  # If you want to ignore any value from the tuple you can use underscore to ignore that value
print(f"m = {m}, n= {n}, p = {p}")


# we can apply this packing and unpacking on any type of sequence
# Tuple comprehension is not supported

t = (x * x for x in range(1, 10))
print(f"The type of the variable t is : {type(t)}")  # here the return type is generator not tuple
for val in t:  # printing the values in a generator
    print(val, end=',')
print()

# Tuple can be used as keys in a dictionary
