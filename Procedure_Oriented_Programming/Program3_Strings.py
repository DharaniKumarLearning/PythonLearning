"""
The below program explains about strings in detail.
String is a sequence of characters
Slice operator is used to extract substring from original string

In Python strings will have two indexes.
 + ve index -- from left to right
 - ve index -- from right to left

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

s = 'Dharani'
print(f"original string :- {s}")
print(f"sorted(s) = {sorted(s)}")  # returns a list
print(f"chr(97) = {chr(97)}")
print(f"ord('a') = {ord('a')}")

# Slice operator

"""

syntax :- s[begin:end:step]
step value can be either positive or negative
The default value of step is 1

If the step value is positive the slice operator will move in forward direction from begin to end - 1 index
In forward direction the default value of begin is 0 and the default value of end is length of the string

If the step value is negative the slice operator will move in backward direction from begin to end + 1 index
In backward direction the default value of begin is -1 and the default value of end is -(length_of_the_string + 1)
In the backward direction if the end value is -1 the result is always an empty string

"""

s = '0123456789'

print(f"The original string is :- {s}")
print(f"s[1:5] = {s[1:5]}")  # will return the characters starting from index 1 to 4
print(f"s[:4] = {s[:4]}")  # since the default value of begin is 0 it will return characters from index 0 to 3
print(f"s[2:] = {s[2:]}")  # since the default value of end is the length of the string it will return characters from index 2 to end - 1
print(f"s[:] = {s[:]}")  # will return a copy of the original string
print(f"s[-1:-4] = {s[-1:-4]}")  # since we can not go from index -1 to -5 in forward direction it will return an empty string
print(f"s[-4:-1] = {s[-4:-1]}")  # will return characters from -4 to -2
print(f"s[100:] = {s[100:]}")  # slice operator won't give any IndexError instead it returns an empty string
print(f"s[1:7:2] = {s[1:7:2]}")  # will return every second character starting from index 1 to 6

print(f"s[::-1] = {s[::-1]}")  # will return the string in reverse order
print(f"s[2:8:-1] = {s[2:8:-1]}")  # since we can not go from index 2 to 9 in backward direction it returns an empty string
print(f"s[8:2-1] = {s[8:2:-1]}")  # 876543
print(f"s[-1:-6:-1] = {s[-1:-6:-1]}")  # 98765
print(f"s[2:-5:1] = {s[2:-5:1]}")  # 234
print(f's[1:6:-2] = {s[1:6:-2]}')  # empty string
print(f's[0:-5:-5] = {s[0:-5:-5]}')  # empty string
print(f's[:0:-1] = {s[:0:-1]}')  # 987654321
print(f's[-1::-1] = {s[-1::-1]}')  # 9876543210
print(f's[-5:0:-9] = {s[-5:0:-9]}')  # 5
print(f's[2:-1:-1] = {s[2:-1:-1]}')  # since the end value is -1 in the backward direction it will always return empty string

# Program to print string in reverse order
s = 'Dharani Kumar Gopavaram'
print(f"The reverse of the string is :- {s[::-1]}")  # one way is using slice operator
print(f"The reverse of the string is :- {''.join(reversed(s))}")  # 2nd way is using reversed function with join

# 3rd way by writing the code
reversed_s = ''
for pos in range(len(s) - 1,-1,-1):
    reversed_s += s[pos]
print(f"The reverse of the string is :- {reversed_s}")

# Input :- Dharani Kumar Gopavaram
# Output :- Gopavaram Kumar Dharani

s = 'Dharani Kumar Gopavaram'
print(f"The input is :- {s}")
print(f"Output is :- {' '.join(s.split(' ')[::-1])}")  # using slice operator with join
print(f"Output is :- {' '.join(reversed(s.split()))}")  # using reversed with join

# Input :- Durga Software Solutions
# Output :- agruD erawtfoS snoituloS

s = 'Durga Software Solutions'
print(f"The input is :- {s}")
print(f"Output is :- {' '.join([word[::-1] for word in s.split()])}")  # here we are using list comprehension

# Print the characters at even and odd position
s = 'Dharani Kumar Gopavaram'

# using slice operator
print(f'The characters at even position are :- {s[::2]}')
print(f'The characters at odd position are :- {s[1::2]}')

# without using slice operator
even_chars = odd_chars = ''
for i in range(0,len(s),2):
    try:
        even_chars += s[i]
        odd_chars += s[i + 1]
    except IndexError:
        pass

print(f'The characters at even position are :- {even_chars}')
print(f'The characters at odd position are :- {odd_chars}')

# Input :- B4A13D
# Output :- ABD134

s = 'B4A13D'
print(f"Input :- {s}")
only_nums = only_chars = ''
for c in s:
    if c.isdigit():
        only_nums += c
    else:
        only_chars += c

print(f"Output :- {''.join(sorted(only_chars)) + ''.join(sorted(only_nums))}")

# Input :- ab10cd5
# Output :- ababababababababababcdcdcdcdcd

s = 'ab10cd5'

print(f"Input :- {s}")
found_digit = False
digits = chars = result = ''
for c in s:
    if c.isdigit():
        found_digit = True
        digits += c
    else:
        if found_digit:
            result += chars * int(digits)
            found_digit = False
            chars = c
            digits = ''
        else:
            chars += c

if found_digit:
    result += chars * int(digits)
else:
    result += chars

print(f"Output is :- {result}")

# Input :- s1 = 'RAVI', s2 = 'RAMAKRISHNA'
# Output :- RRAAVMIAKRISHNA

s1 = 'RAVI'
s2 = 'RAMAKRISHNA'
max_length = max(len(s1),len(s2))
result = ''
for i in range(max_length):
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[i]
print(f"Output :- {result}")

# Program to remove duplicates from string

s = 'aaabbbbaaaddccc'
print(f"The original string is :- {s}")

# using set
print(f"The string without duplicates is :- {''.join(set(s))}")  # once we convert to set the order will be lost

# writing the code

result = ''
for c in s:
    if c not in result:
        result += c

print(f"The string without duplicates is :- {result}")

# Print the number of occurrences of every character in the string
s = 'aaabbbbaaaddccc'
d = {}

print(f"The original string is :- {s}")
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

for k,v in d.items():
    print(f"{k} -> {v} times in the string")









