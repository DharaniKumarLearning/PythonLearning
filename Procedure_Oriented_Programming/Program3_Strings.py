"""
The below program explains about strings in detail.
String is a sequence of characters
Slice operator is used to extract substring from original string

In Python strings will have two indexes.
 + ve index -- from left to right
 - ve index -- from right to left

String Methods :-

    The lstrip, rstrip and strip methods doesn't remove in between spaces

"""

s = "Dharani Kumar Gopavaram"  # String index starts from 0
print(f'Accessing value at index 0 from the string "{s}" which is :- {s[0]}')
print(f'Accessing value at index 3 from the string "{s}" which is :- {s[3]}')
print(f'Accessing last element of the string "{s}" using negative index and the value is :- {s[-1]}')

# If we try to access index which doesn't exist we get IndexError
# print(f'Accessing index which does not exist :- {s[100]}')  # IndexError: string index out of range

# Printing the positive and negative index of every character in the string

position = 0
for char in s:
    print(f'The character {char} is present at +ve index {position} and -ve index {position - len(s)}')
    position += 1

# String Methods

# len -- to know the length of the string i.e. number of characters
# lstrip -- to remove the left side spaces of the string
# rstrip -- to remove the right side spaces of the string
# strip -- to remove both left and right side spaces of the string

s = '   Dharani Kumar Gopavaram    '
print(f'Original string :- {s}')
print(f's.lstrip() = {s.lstrip()}')
print(f's.rstrip() = {s.rstrip()}')
print(f's.strip() = {s.strip()}')

# Methods to know the position of the substring -- find, rfind, index, rindex
# find -- to know the position of the substring in the original string.
#           If the substring is not available it will return -1
# The find method is overloaded it has 3 forms
# find(substring) -- will search for the substring from beginning to the end of the string
# find(substring,begin) -- will search from begin index we specify to the end of the string
# find(substring,begin,end) -- will search for substring from begin to end - 1 index we specify

s = 'durgasoftdurgasoft'
print(f'Original string :- {s}')
print(f"s.find('soft') = {s.find('soft')}")
print(f"s.find('soft') = {s.find('soft', 6)}")
print(f"s.find(5,8) = {s.find('soft', 5, 8)}")  # will search between indexes 5 - 7
# The above line returns -1 since the substring we are searching is not present between index 5 and 7

# rfind -- same as find method but will search for substring in the reverse direction
print(f"s.rfind('soft') = {s.rfind('soft')}")

# index method is same as find method the only difference is if the substring is not available index method returns ValueError
substring = ''
try:
    print(f"The index of the substring 'soft' using index method is :- {s.index('soft',6)}")
    substring = 'dharani'
    print(f"The index of the substring 'dharani' using index method is :- {s.index(substring)}")
except ValueError: # If there is an exception it will get handled by the except block
    print(f"The substring '{substring}' is not present in the string '{s}"'')

# Program to display all the occurrences of a substring in the given string
substring = 'soft'
start = 0
while True:
    pos = s.find(substring,start)
    if pos == -1:
        break
    else:
        print(f"The substring {substring} is present at index {pos} in '{s}'")
        start = pos + 1

if start == 0 and pos == -1:
    print(f'The substring {substring} you are searching is not present ')

# s.count(substring) -- to know the number of occurrences of the passed substring in the main string
# s.count(substring, begin) -- will return the number of occurrences starting from begin index we specify
# s.count(substring, begin, end) -- will return the number of occurrences starting from begin to end -1 index

print(f"Original string :- {s}")
print(f"s.count('soft') = {s.count('soft')}")
print(f"s.count('soft', 6) = {s.count('soft', 6)}")
print(f"s.count('soft', 5, 8) = {s.count('soft', 5, 8)}")

# s.replace(old_string, new_string) -- To replace old_string with new_string in the string
# s.replace(old_string, new_string, count) -- count parameter will tell how many times we want to replace old_string with new_string

print(f"s.replace('a','z') = {s.replace('a','z')}")
print(f"s.replace('a','z', 1) = {s.replace('a','z', 1)}")

# s.upper() -- To convert all the characters to uppercase
# s.lower() -- To convert all the characters to lowercase
# s.swapcase() -- convert uppercase to lowercase and vice-versa
# s.title() -- first character of every word in the string starts with uppercase
# s.capitalize() -- first character of the string starts with uppercase rest all the characters are lowercase
# s.startswith(substring) -- To know whether our string is starting with a particular substring or not
# s.endswith(substring) -- To know whether our string is ending with a particular substring or not

# isalnum() -- check whether the string contains only alphanumeric characters or not(a-z, A-Z, 0 to 9)
# isalpha() -- checks whether the string contains only alphabet characters or not
# isdigit() -- checks whether the string contains only digits or not
# islower() -- checks whether the string contains only lower alphabet symbols or not
# isupper() -- checks whether the string contains only upper alphabet symbols or not
# istitle() -- checks whether the string contains words in title case or not
# isspace() -- checks whether the string contains only space or not

# s.split(separator) -- default separator is space -- returns a list of strings
# s.split(separator, count) -- count indicates how many times you want to perform the split
# s.rsplit(separator, count) - same like split but will do the splitting in the reverse direction

s = 'Dharani,Kumar,Gopavaram'
print(f"s.split(',') = {s.split(',')}")
print(f"s.split(',', 1) = {s.split(',', 1)}")
print(f"s.rsplit(',', 1) = {s.rsplit(',', 1)}")

# separator.join(l) -- join method is used to create a string out of a collection
sample_list = ["Dharani", "Kumar", "Gopavaram"]
print(f"sample_list = {sample_list}")
print(f"Creating a string without using delimiter for the collection : {''.join(sample_list)}")
print(f"Creating a string using space as a delimiter for the collection : {' '.join(sample_list)}")
print(f"Creating a string using comma as a delimiter for the collection : {','.join(sample_list)}")

# sorted(s) -- sort the characters in the string and returns list
# chr(int) -- will return the character present in the ASCII value we passed
# ord(character) -- will return the ASCII value of the character we passed