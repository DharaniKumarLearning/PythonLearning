"""
If our data is in the form of key/value pairs then we should use dict data structure
In dict the keys can not contain duplicates whereas values can contain duplicates
dict is also represented using curly braces only
"""

d = {100: "Dharani", 200: "Ram", 300: "Ravi"}
print(f"The type of the variable d is {type(d)} and the value of it is : {d}")
d[400] = "John"  # The key 400 and the value "John" will get added to the dictionary
print(f"The values in dictionary after adding one pair is : {d}")
d[300] = "Robert"  # Since the key 300 already exists in dictionary the value will get overridden
print(f"The values in dictionary after updating one pair is : {d}")

empty_dict = dict()  # we can use dict function as well to create an empty dictionary
print(f"The type of the variable empty_dict is {type(empty_dict)} and the value of it is : {empty_dict}")

sample_dict = {}  # If we just have curly brace open and close then by default it is treated as dict only
print(f"The type of the variable sample_dict is {type(sample_dict)} and the value of it is : {sample_dict}")

sample_dict[100] = "Dharani"
sample_dict[200] = "Kumar"
sample_dict[300] = "Gopavaram"
print(f"The values in dictionary after adding elements is : {sample_dict}")

# We can access the value of a key by specifying the key in square brackets
access_key = 100

try:
    print(f"The value of the key {access_key} in the dictionary is : {sample_dict[access_key]}")
    access_key = 500
    print(f"The value of the key {access_key} in the dictionary is : {sample_dict[access_key]}")
except KeyError:
    print(f"The key {access_key} doesn't exist in dictionary {sample_dict}")

# We can traverse through the elements of the dictionary using for loop

for key in sample_dict:  # if we are using for loop like this then by default sample_dict will return keys
    print(f"{key} -> {sample_dict[key]}")

delete_key = 200

try:
    del sample_dict[delete_key]  # deleting a key from dictionary
    print(f"The dictionary after deleting a key is : {sample_dict}")
    delete_key = 400
    del sample_dict[delete_key]
    print(f"The dictionary after deleting a key is : {sample_dict}")
except KeyError:
    print(f"The key {delete_key} doesn't exist in dictionary {sample_dict}")

sample_dict.clear()  # to delete all the key/value pairs in dictionary
print(f"The dictionary after using clear method is : {sample_dict}")

multi_values_dict = {100: [10, 20, 30], 200: {"Dharani", "Kumar", "Gopavaram"}}
print(f"The dictionary which contains multiple elements for a key is : {multi_values_dict}")

# We can create a dictionary using dict method from a tuple of tuples
sample_dict = dict(((100, "Dharani"), (200, "Shiva"), (300, "Ravi")))
print(f"The dictionary created from tuple of tuples is :- {sample_dict}")
print(f"The number of key/value pairs in dictionary is :- {len(sample_dict)}")

print(f"The value of the key 100 using get method :- {d.get(100)}")
print(f"The value of the key 500 using get method :- {d.get(500)}")  # If the key doesn't exist get method returns None
print(f"The value of the key 500 using get method with default value is :- {d.get(500, 'Not found')}")  # get method accepts a default value as well

delete_key = 100
try:
    print(f"Removing and returning the value associated with the key {delete_key} : {sample_dict.pop(delete_key)}")
    delete_key = 400
    print(f"Removing and returning the value associated with the key {delete_key} : {sample_dict.pop(delete_key)}")
except KeyError:
    print(f"The key {delete_key} doesn't exist in the dictionary {sample_dict}")

print(f"Removing and returning some random key/value pair in dict :- {sample_dict.popitem()}")
print(f"Removing and returning some random key/value pair in dict :- {sample_dict.popitem()}")
# print(f"Removing and returning some random key/value pair in dict :- {sample_dict.popitem()}")
# KeyError: 'popitem(): dictionary is empty'

print(f"The values in dictionary are :- {sample_dict}")

sample_dict = dict(((100, "Dharani"), (200, "Shiva"), (300, "Ravi")))
print(f"The keys in dictionary are :- {sample_dict.keys()}")
print(f"The values in dictionary are :- {sample_dict.values()}")

for k, v in sample_dict.items():
    print(f"{k} -> {v}")

copy_dict = sample_dict.copy()
copy_dict[400] = "Kumar"
print(f"The key/value pairs in copy_dict are :- {copy_dict}")

sample_dict.setdefault(400, "Gopavaram")  # If the key doesn't exist in dictionary adds the key/value pair to dictionary
sample_dict.setdefault(100, "John")  # If the key is present in the dictionary it doesn't override the value
print(f"The key/value pairs in dictionary after using setdefault method is : {sample_dict}")

marks_dict = {600: "Ram", 700: "Jacob"}
sample_dict.update(marks_dict)  # To add multiple values to dictionary
print(f"The key/value pairs in dictionary after using update method is : {sample_dict}")

sample_dict = {'Ravi': 100, 'Shiva': 98, 'Ram': 90}
print(f"The key/value pairs in dictionary are : {sample_dict}")
print(f"The sum of values present in the dictionary is : {sum(sample_dict.values())}")

# Program to print the occurrence of every character present in the string

s = "mississippi"
output_dict = {}
for char in s:
    output_dict[char] = output_dict.get(char, 0) + 1

for k, v in output_dict.items():
    print(f"{k} -> {v} times")

# Program to print the occurrence of every vowel present in the string

s = "How are you"
vowels = "aeiou"
vowels_present = set(s) & set(vowels)
output_dict = {}
for v in vowels_present:
    output_dict[v] = s.count(v)

for k, v in output_dict.items():
    print(f"{k} -> {v} times")

# dictionary comprehension

squares = {x: x * x for x in range(1, 11)}
print(f"squares dictionary using dictionary comprehension : {squares}")

doubles = {x: x * 2 for x in range(1, 11)}
print(f"doubles dictionary using dictionary comprehension : {doubles}")
