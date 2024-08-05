"""
If we want to represent group of values as a single entity which is mutable where
    1. Insertion order is not preserved
    2. duplicates are not allowed
    3. Heterogeneous objects are allowed
then we should use set data structure
Sets are represented using curly braces
"""

sample_set = {30, 20, 10, 10, 30, 40, 30}  # even though we add duplicates they are not considered
print(f"The type of the variable sample_set is {type(sample_set)} and it's value is : {sample_set}")

# We can not access the elements of set using index
# print(sample_set[0]) # TypeError: 'set' object is not subscriptable
# since the order is not preserved in sets slicing and indexing is not applicable
# Using for loops we can traverse through the elements of the set

print(f"Accessing the elements in the set using for loop : ", end='')
for data in sample_set:
    print(data, end=',')
print()

sample_set.add("Dharani")  # add method is used to add an element to set
print(f"The elements in set after using add method is : {sample_set}")

sample_set.remove(10)  # remove method is used to remove an element from set
print(f"The elements in set after using remove method is : {sample_set}")

sample_char_set = set("Dharani")  # we can use set function to create set from a collection
print(f"The set created using set function by passing string is : {sample_char_set}")
print(f"The set created using set function by passing range is : {set(range(10, 101, 5))}")

sample_num_list = [10, 20, 10, 30, 10]
print(f"The set created using set function by passing list is : {set(sample_num_list)}")

# Important methods of set
# len(sample_set) -- to know the number of elements in the set
# sample_set.add(element) -- to add an element to set
# sample_set.update(sequence) -- to add all the elements in the sequence to set

sample_set = set()  # to create an empty set we should use set function
print(f"The number of elements in the sample_set is : {len(sample_set)}")
sample_set.add(10)
sample_set.add(20)
sample_set.add(30)
sample_set.add(40)
print(f"The elements in sample_set after adding elements is : {sample_set}")
sample_list = [100, 200, 300, 400, 500]
sample_set.update(sample_list)  # adding all the elements in sample_list to sample_set
print(f"The elements in sample_set after using update method with single collection is : {sample_set}")
sample_tuple = (-1, -2, -3, -4)
name = "Dharani"
sample_set.update(sample_tuple, name)  # update method can accept multiple sequences as well
print(f"The elements in sample_set after using update method with multiple collection is : {sample_set}")

# sample_set.copy() -- to create a copy of the entire set object
# sample_set.pop() -- return and removes some random element from the set
# sample_set.remove(element) -- removes the element we specified from the set
#       If the specified element doesn't exist in set we get KeyError

print(f"Removing some random element from sample_set : {sample_set.pop()}")
print(f"Removing some random element from sample_set : {sample_set.pop()}")
print(f"The sample_set after using pop method is : {sample_set}")

remove_element = -1
try:
    sample_set.remove(remove_element)
    print(f"The sample_set after removing {remove_element} is : {sample_set}")
    remove_element = 99
    sample_set.remove(remove_element)
    print(f"The sample_set after removing {remove_element} is : {sample_set}")
except KeyError:
    print(f"The element '{remove_element}' doesn't exist in the {sample_set}")

# sample_set.discard(element) -- discard method is same as remove but doesn't throw any error if the specified element doesn't exist

sample_set.discard("Dharani")
sample_set.discard(-2)
sample_set.discard('D')
print(f"The sample_set after removing elements is : {sample_set}")

# sample_set.clear() -- clear method is used to clear all the elements in the set

sample_set.clear()
print(f"The elements in the set after using clear method is : {sample_set}")

# Mathematical operations on set
# s1.union(s2) or s1 | s2 -- wil combine all the elements in both s1 and s2
# s1.intersection(s2) or s1 & s2 -- will return the common elements in both s1 and s2
# s1.difference(s2) os s1 - s2 -- will return the elements present in s1 but not in s2
# s1.symmetric_difference(s2) or s1 ^ s2 -- except common elements will return everything in both the sets

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(f"s1 = {s1}, s2 = {s2}")
print(f"s1.union(s2) = {s1.union(s2)}")
print(f"s1 | s2 = {s1 | s2}")
print(f"s1.intersection(s2) = {s1.intersection(s2)}")
print(f"s1 & s2 = {s1 & s2}")
print(f"s1.difference(s2) = {s1.difference(s2)}")
print(f"s1 - s2 = {s1 - s2}")
print(f"s1.symmetric_difference(s2) = {s1.symmetric_difference(s2)}")
print(f"s1 ^ s2 = {s1 ^ s2}")

# set comprehension

s1 = {x * x for x in range(1, 10)}
print(f"The set created using set comprehension is : {s1}")

# Program to print all the vowels present in a given string using sets
vowels = "aeiou"
sentence = "The quick brown fox jumps over lazy dog"
print(f"The vowels present in the '{sentence}' are : {''.join(set(vowels) & set(sentence))}")

# frozenset is same as set the only difference is frozenset is immutable whereas set is mutable

s = {10, 20, "Dharani", 40}
fs = frozenset(s)
print(f"The type of the variable fs is {type(fs)} and the value of it is : {fs}")

# We can not add or remove elements from frozenset
# fs.add("D")  # AttributeError: 'frozenset' object has no attribute 'add'
