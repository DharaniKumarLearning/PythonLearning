"""

If we want to represent group of values as a single entity which is mutable where

    1. insertion order is preserved
    2. duplicates are allowed
    3. heterogeneous objects are allowed meaning different type of objects

then we should use List data structure
Lists are represented using square brackets

"""

sample_list = []
print(f"The type of the variable sample_list is : {type(sample_list)}")
sample_list.append(10)  # append method is used to add element to the end of the list
sample_list.append(20)
sample_list.append("Dharani")
sample_list.append(30)
sample_list.append(10)
print(f"The sample_list after adding elements : {sample_list}")
sample_list[0] = 999  # since lists are mutable we can modify the elements if we want
print(f"The sample_list after modifying elements : {sample_list}")
print(f"Accessing the first element of the list using index 0 : {sample_list[0]}")
print(f"Accessing the last element of the list using index -1 : {sample_list[-1]}")
sliced_list = sample_list[0:3]  # we can use slice operator on lists
print(f"sliced_list : {sliced_list}")
sample_list.remove(30)  # remove method can be used to remove an element from list
print(f"sample_list after removing the element 30 : {sample_list}")
print(f"The repetition operator on lists : {sample_list * 2}")

sample_num_list = list(range(10))  # we can use list function to create a list out of any sequence
print(f"sample_num_list created using list function : {sample_num_list}")

sample_char_list = list("Dharani")
print(f"sample_char_list created using list function : {sample_char_list}")

nested_list = [10, 20, [30, 40]]
print(f"Accessing nested element in the list using index : {nested_list[2]}")
print(f"Accessing second element in the nested list element using index : {nested_list[2][1]}")

# Traversing through elements of list
# We can use for loops and while loops to traverse through elements of the list

for i in range(len(sample_num_list)):
    print(f"The element {sample_num_list[i]} is present at +ve index {i} and -ve index {i - len(sample_num_list)}")

# Important functions and methods of list

# len(list) -- to know the number of elements in the list
# l.count(element) -- to know the number of times the element we passed is present in the list
# l.index(element) -- returns the first index of the element we specify. If the specified element doesn't exist we get ValueError

sample_list = [10, 20, 30, 40, 50, 10, 10, 10, 30]
print(f"The number of elements present in the list {sample_list} is : {len(sample_list)}")
print(f"The numer of times the element 10 is present in the list {sample_list} is : {sample_list.count(30)}")
print(f"The numer of times the element 90 is present in the list {sample_list} is : {sample_list.count(90)}")

search_element = 30
try:
    print(f"The first index of the element {search_element} in the list {sample_list} is : {sample_list.index(search_element)}")
    search_element = 90
    print(f"The first index of the element {search_element} in the list {sample_list} is : {sample_list.index(search_element)}")
except ValueError:
    print(f"The {search_element} doesn't exist in the list : {sample_list}")

# l.append(element) -- to add an element to the end of the list
# l.insert(index, element) -- To add an element at the specified index
#       If the index we specify to the insert method is greater than the length of the list the element will get added as the last element
#       We can pass negative index as well to the insert method

sample_list.append("Dharani")
print(f"The list after using append method : {sample_list}")
sample_list.insert(3, "John")
sample_list.insert(100, "Ram")  # the element will get added as the last element of the list
sample_list.insert(-3, "Ravi")  # the element will actually get added at the index -4
print(f"The list after using insert method 3 times is : {sample_list}")

# list1.extend(list2) -- to add all the elements in the list2 to list1
#   We can pass any sequence to extend method

sample_list.extend(sample_char_list)
sample_list.extend(range(11, 21))
print(f"The list after using extend method : {sample_list}")

# l.remove(element) -- remove method is used to remove the occurrence of element from list
#       If the specified element doesn't exist in the list we get ValueError

remove_element = "Dharani"
try:
    sample_list.remove(remove_element)
    print(f"The list after removing the element {remove_element} is : {sample_list}")
    remove_element = "Zebra"
    sample_list.remove(remove_element)
    print(f"The list after removing the element {remove_element} is : {sample_list}")
except ValueError:
    print(f"The element '{remove_element}' doesn't exist in the list : {sample_list}")

# l.pop() -- to remove and return the last element from the list
#   If we run pop on empty list we get IndexError: pop from empty list
# l.pop(index) -- to remove and return the element at the specified index
#   If we specify incorrect index we get IndexError: pop index out of range

sample_list.pop()
sample_list.pop()
print(f"The elements in the list after using pop method is : {sample_list}")

pop_index = 10
try:
    sample_list.pop(pop_index)
    print(f"The element in list after popping the element at index {pop_index} is : {sample_list}")
    pop_index = 100
    sample_list.pop(pop_index)
    print(f"The element in list after popping the element at index {pop_index} is : {sample_list}")
except IndexError:
    print(f"The list doesn't have the index {pop_index}")

# l.reverse() -- to reverse the elements in the list
sample_list.reverse()  # since list is mutable all the list methods doesn't return a new list it modifies the list in place
print(f"The list after using reverse method is : {sample_list}")


# l.clear() -- to clear all the elements in the list
sample_list.clear()
print(f"The list after using clear method : {sample_list}")

# l.sort() -- to sort the elements of the list in ascending order
# l.sort(reverse=True) -- to sort the elements of the list in descending order
# To apply the sort method the list should contain homogenous elements only

range_list = [98, 76, 45, 12, 90, 65]
print(f"The list before sorting : {range_list}")
range_list.sort()
print(f"The list after sorting in ascending order : {range_list}")
range_list.sort(reverse=True)
print(f"The list after sorting in descending order : {range_list}")

x = [10, 20, 30, 40]
y = x  # this is called aliasing
y[1] = 999  # changes to variable y will get reflected to x because list is mutable
print(f"id(x) = {id(x)}, id(y) = {id(y)}")
print(f"x = {x}, y = {y}")

# If we want to create a copy of the list object we can use slice operator or copy method
x = [10, 20, 30, 40]
y = x.copy()  # copy method is used to create a copy of the list object
y[1] = 999
print(f"id(x) = {id(x)}, id(y) = {id(y)}")
print(f"x = {x}, y = {y}")  # here the changes won't get reflected to x because we create a copy of the list object

print(f"+ operator on lists : {x + y}")
print(f"Printing the values in nested list")
nested_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for col in nested_list:
    for row in col:
        print(row, end=' ')
    print()

# List comprehension
# Let's say if we want to create a list with the squares of first 10 numbers
# we will usually write code like this

squares_list = []
for i in range(10):
    squares_list.append(i * i)
print(f"squares_list without using list comprehension : {squares_list}")

# with the help of list comprehension we can easily do this

squares_list_comp = [i * i for i in range(10)]  # the length of the code will reduce drastically
print(f"squares_list_comp using list comprehension : {squares_list_comp}")

double_list = [i + i for i in range(10)]  # we can perform any operation we want
print(f"double_list using list comprehension :  {double_list}")

even_squares_list = [num * num for num in range(1, 11) if num % 2 == 0]  # we can specify if condition like this
print(f"even_squares_list using list comprehension : {even_squares_list} ")

words = ['Bat', 'Not', 'At', 'Cat']
first_char_list = [w[0] for w in words]
print(f"first_char_list using list comprehension is : {first_char_list}")

sentence = "the quick brown fox jumps over lazy dog"
content_list = [(s.title(), len(s)) for s in sentence.split()]
print(f"content_list using list comprehension is : {content_list}")

# Program to print all the vowels in a given sentence

vowels = "aeiou"
vowels_list = []

for c in sentence:
    if c in vowels:
        if c not in vowels_list:
            vowels_list.append(c)

print(f"The vowels present in the sentence {sentence} are : {''.join(vowels_list)}")

# Lists can not be used as keys in a dictionary
