"""
The below program explains about list data structure.
If we want to represent group of values as a single entity which is mutable where

    1. Insertion order is preserved
    2. Duplicates are allowed
    3. Heterogeneous objects are allowed(meaning different types of objects)

then we should use list data structure
"""

list1 = []  # Lists are represented using square brackets
print(f"The type of the variable list1 is : {type(list1)}")
list1.append(10)  # append method is used to add an element to list
list1.append(20)
list1.append(30)
list1.append('dharani')  # appending different type of object to list
print(f"The elements in the list after appending values is :- {list1}")
list1[0] = 999  # since list objects are mutable we can change the values like this

# We can access the elements of the list using index and slice operator
print(f"Accessing the first element of the list using index :- {list1[0]}")
print(f"Accessing the last element of the list using negative index :- {list1[-1]}")
print(f"Applying slice operator on lists :- {list1[1:3]}")

print(f"The repetition operator on lists :- {list1 * 2}")

sample_num_list = list(range(100,0,-5))  # we can use list function to create a list out of any sequence
print(f"sample_num_list = {sample_num_list}")

sample_string_list = list('Dharani')  # string is also a sequence
print(f"sample_string_list = {sample_string_list}")

nested_list = [10,20,[30, 40]]
print(f"Accessing nested list element :- {nested_list[2]}")
print(f"Accessing second element in the nested list element using index :- {nested_list[2][1]}")

# We can use for loop and while loop to traverse through the elements of the list
list1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
for i in range(len(list1)):  # len function can be used to know the number of elements in the list
    print(f"The element {list1[i]} is present at +ve index {i} and negative index {i - len(list1)}")

# Important functions and methods of list
# len(list) -- to know the number of elements in the list
# l.count(element) -- to know the number of occurrences of the element we passed inside the list

list1 = [10, 20, 30, 40, 50, 10, 10, 10, 30]
print(f"The number of elements in the list :- {list1}")
print(f"The number of times the element 10 is present in the list :- {list1.count(10)}")
print(f"The number of times the element 90 is present in the list :- {list1.count(90)}")

# l.index(element) -- return the first index of the element we specify. If the element doesn't exist it returns ValueError

print(f"The element 30 is present at index {list1.index(30)}")

search_element = 90

try:
    print(f"The element 90 is present at index {list1.index(search_element)}")
except ValueError:
    print(f"The {search_element} is not present in the list {list1}")

# l.insert(index, element) -- to add an element at the specified index
# If the index we specify is greater than length of the list it will get added as the last element.
# insert method accepts negative index as well

list1.insert(3, 50)  # adding element 50 at index 3
print(f"list1 after adding element 50 at index 3 is :- {list1}")

list1.insert(50,99)  # since the index 50 doesn't exist the element get added to the end of the list
print(f"list1 after trying to add the element at index 50 is :- {list1}")

list1.insert(-4,999)  # the element will get added to the index -5
print(f"list1 after trying to add the element at index -4 is :- {list1}")

# list1.extend(list2) -- add all the elements in list2 to list1. We can pass any sequence to extend method

list2 = ["Ram", "Robert", "Rahim"]
list1.extend(list2)
print(f"list1 after using extend method :- {list1}")

s = 'Dharani Kumar Gopavaram'
list1.extend(s)
print(f"list1 after using extend method again :- {list1}")

# l.remove(element) -- to remove the specified element from the list
# If the specified element doesn't exist it returns ValueError

list1.remove('Ram')
print(f'list1 after removing the element "Ram" is :- {list1}')

remove_element = 'Sita'

try:
    list1.remove(remove_element)
except ValueError:
    print(f"The element {remove_element} doesn't exist in the list")

# l.pop() -- to remove and return the last element in the list.
# If we run pop method on empty list we get IndexError: pop from empty list

print(f"Removing the last element in the list :- {list1.pop()}")
print(f"list1 after pop :- {list1}")

# l.pop(index) -- remove the return the element at the specified index
# If the specified index doesn't exist we get IndexError: pop index out of range

print(f"Popping the 5th element in the list :- {list1.pop(4)}")
print(f"list1 after popping the 5th element :- {list1}")

# l.reverse() -- to reverse the elements in the list

list1.reverse()  # list is mutable all these methods won't return a new list object
print(f"list1 after reversing :- {list1}")

# l.sort() -- To sort the elements in list
# l.sort(reverse=True) -- to sort the elements in descending order
# If we want to apply sort method the list should contain only homogenous elements

list2 = [98, 76, 45, 12, 90, 65]
print(f"list2 before sorting :- {list2}")
list2.sort()
print(f"list2 after sorting :- {list2}")
list2.sort(reverse=True)
print(f"list2 after sorting in descending order :- {list2}")

x = [10, 20, 30, 40]
y = x  # this is called aliasing
y[1] = 999  # changes to the variable y will get reflected to variable x because list is mutable
print(f"id(x) = {id(x)}, id(y) = {id(y)}")
print(f"x = {x}")

# Never do aliasing when working with mutable objects. Instead, create a copy of the mutable object and perform operations
# l.copy() -- to create a copy of the list object

x = [100, 200, 300, 400]
y = x.copy()
y[1] = 9999  # here the variable x won't get reflected because we created a copy of the list object
print(f"id(x) = {id(x)}, id(y) = {id(y)}")
print(f"x = {x}, y = {y}")

print(f"+ operator on lists :- {x + y}")

# l.clear() -- to clear all the elements in the list

print(f"list1 before clearing the elements :- {list1}")
list1.clear()
print(f"list1 after clearing the elements :- {list1}")

print(f'Printing the values in nested list')
list1 = [[10,20,30], [40,50,60], [70,80,90]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end=' ')
    print()

# List comprehensions
# Let's say if we want to create a list with the squares of first 10 numbers

# we will usually write code like below and do it

squares_list = []
for i in range(1,11):
    squares_list.append(i * i)

print(f"squares list :- {squares_list}")

# with the help of list comprehension we can easily do it
squares_list = [x * x for x in range(1,11)]
print(f"squares list using list comprehension is :- {squares_list}")

even_squares_list = [x * x for x in range(1,11) if x % 2 == 0]
print(f"even_squares_list = {even_squares_list}")

words_list = ["Bat", "Not", "At", "Cat"]
first_char = [x[0] for x in words_list]
print(f"first_char = {''.join(first_char)}")

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
list3 = [ x for x in list1 if x not in list2 ]
print(f"list3 = {list3}")

sentence = "the quick brown fox jumps over lazy dog"
words = sentence.split()
content = [ (w.title(),len(w)) for w in words ]
print(f"content :- {content}")

# Program to print all the vowels present in a sentence
vowels = "aeiou"
vowels_list = []

for char in sentence:
    if char in vowels:
        if char not in vowels_list:
            vowels_list.append(char)

vowels_list.sort()
print(f"The vowels present in the sentence {sentence} are :- {''.join(vowels_list)}")

# Lists can not be used as keys in a dictionary