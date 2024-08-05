"""
String is sequence of characters
Slice operator is used to extract substring from the original string

In Python strings have two indexes
    +ve index --> from left to right
    -ve index --> from right to left
"""

s = "Dharani Kumar Gopavaram"
print(f"Accessing the first character in the string {s} using the index 0 : {s[0]}")
print(f"Accessing the third character in the string {s} using the index 2 : {s[2]}")
print(f"Accessing the last character in the string {s} using negative index -1 : {s[-1]}")

# If we try to access index that doesn't exist we get IndexError
access_index = 99
try:
    print(f"Accessing the character at index 99 :- {s[access_index]}")
except IndexError:
    print(f"The index {access_index} doesn't exist in the string {s}")

# printing the positive and negative index of every character in the string

positive_index = 0
for c in s:
    print(f"The character {c} is present at +ve index {positive_index} and -ve index {positive_index - len(s)}")
    positive_index += 1

# String methods
# len -- to know the length of the string i.e. the number of characters
# s.lstrip() -- to remove left side spaces of the string
# s.rstrip() -- to remove right side spaces of the string
# s.strip() -- to remove both left and right side spaces of the string

s = "  Dharani  "
print(f"The original string before applying strip method :- {s}")
print(f"The string after applying lstrip method :- {s.lstrip()}")
print(f"The string after applying rstrip method :- {s.rstrip()}")
print(f"The string after applying strip method :- {s.strip()}")

# Methods to know the position of the substring -- find, rfind, index, rindex
# find -- to know the position of the substring in the main string. If the substring is not present it returns -1
# find method is overloaded it has 3 forms
# s.find(substring) -- will search for substring from the beginning to the end of the string
# s.find(substring, begin) -- will search for substring from begin index we specify to the end of the string
# s.find(substring, begin, end) -- will search for substring from begin to end - 1 index

s = 'durgasoftdurgasoft'
search_string = 'soft'

print("Using find method to know the position of the substring")
print(f"The position of the substring '{search_string}' in the string '{s}' is : {s.find(search_string)}")
print(f"The position of the substring '{search_string}' in the string '{s}' "
      f"starting from index 6 is : {s.find(search_string, 6)}")  # returns the second occurrence
print(f"The position of the substring '{search_string}' in the string '{s}' "
      f"between index 5 and 8 is is : {s.find(search_string, 5, 8)}")
# The above print statement will return -1 because the complete substring is not present b/w the indexes we specify

# index method is same as find method the only difference is index method ValueError when the substring is not present

print("Using index method to know the position of the substring")
try:  # risky code is placed in try block
    print(f"The position of the substring '{search_string}' in the string '{s}' "
          f"between index 5 and 9 is is : {s.index(search_string, 5, 9)}")
    print(f"The position of the substring 'z' in the string '{s}' is : {s.index('z')}")
except ValueError:  # If the risky code raises exception it will get handled here
    print(f"The substring is not present")
else:  # the else block will get executed if the code didn't reach except block
    print("The substring you are searching is present")

# Program to display all the occurrences of a substring in the given string

s = 'durgasoftdurgasoft'
search_string = 'soft'
first_pos = s.find(search_string)

while first_pos != -1:
    print(f"The substring is present at index : {first_pos}")
    first_pos = s.find(search_string, first_pos + 1)

# count method is used to know number of occurrences of the substring in the main string
# count method is also overloaded it has 3 forms
# s.count(substring) -- return the number of occurrences of substring from beginning to the end of the string
# s.count(substring, begin) -- return the number of occurrences of substring from begin index we specify to the end of the string
# s.count(substring, begin, end) -- return the number of occurrences of substring from begin to end - 1 index

print("Using the count method to know the number of occurrences of the substring in the main string")
print(f"The number of times the '{search_string}' in the string '{s}' is : {s.count(search_string)}")
print(f"The number of times the '{search_string}' in the string '{s}' starting from index 6 is : {s.count(search_string, 6)}")
print(f"The number of times the '{search_string}' in the string '{s}' b/w the indexes 5 and 8 is : {s.count(search_string, 5, 8)}")

# s.replace(old_string, new_string) -- replaces old_string with new_string
# s.replace(old_string, new_string, count) -- count indicates how many times we want to perform the replace operation

print(f"The original string s : {s}")
print("Using the replace method on the original string")
print(f"s.replace('soft','software') : {s.replace('soft', 'software')}")
print(f"s.replace('soft','software', 1) : {s.replace('soft', 'software', 1)}")  # Replace only the first occurrence

# split method is used to split strings based on a separator
# s.split() -- the default separator is space -- returns a list of strings
# s.split(separator, count) -- count indicates how many times you want to perform the split operation
# s.rsplit(separator, count) -- same as split but will do the splitting in reverse direction

print("Using split method to split the strings based on a separator")

s = "Dharani Kumar Gopavaram"
print(f"The original string s : {s} ")
print(f"s.split() : {s.split()}")

s = "Dharani,Kumar,Gopavaram"
print(f"The original string s : {s} ")
print(f"s.split(',') : {s.split(',')}")
print(f"s.split(',', 1) : {s.split(',', 1)}")  # will perform the split operation only once
print(f"s.rsplit(',', 1) : {s.rsplit(',', 1)}")

# join method is used to create a string out of a collection
# separator.join(collection) is the syntax

sample_list = ["Dharani", "Kumar", "Gopavaram"]
print(f"Creating a string out of a list :- {'|'.join(sample_list)}")

# s.upper() -- To convert all the characters to uppercase
# s.lower() -- To convert all the characters to lowercase
# s.swapcase() -- convert uppercase to lowercase and vice-versa
# s.title() -- first character of every word in the string starts with uppercase
# s.capitalize() -- first character of the string starts with uppercase rest all the characters are lowercase

s = 'package1 Kumar Gopavaram'
print(f"Original string : {s}")
print(f"s.lower() : {s.lower()}")
print(f"s.upper() : {s.upper()}")
print(f"s.swapcase() : {s.swapcase()}")
print(f"s.title() : {s.title()}")
print(f"s.capitalize : {s.capitalize()}")

# s.startswith(substring) method can be used to know whether a string is starting with the substring we specified or not
# s.endswith(substring) method can be used to know whether a string is ending with the substring we specified or not

s = "package1 kumar gopavaram"
print(f"Original string : {s}")
print(f"s.startswith('package1') : {s.startswith('package1')}")
print(f"s.endswith('gopavaram') :  {s.endswith('gopavaram')}")

# s.isalnum() -- check whether the string contains only alphanumeric characters or not(a-z, A-Z, 0 to 9)
# s.isalpha() -- checks whether the string contains only alphabet characters or not
# s.isdigit() -- checks whether the string contains only digits or not
# s.islower() -- checks whether the string contains only lower alphabet symbols or not
# s.isupper() -- checks whether the string contains only upper alphabet symbols or not
# s.istitle() -- checks whether the string contains words in title case or not
# s.isspace() -- checks whether the string contains only space or not

s = "dharani123kumar"
print(f"Original string : {s}")
print(f"s.isalnum() : {s.isalnum()}")
print(f"s.isalpha() : {s.isalpha()}")
print(f"s.isdigit() : {s.isdigit()}")
print(f"s.islower() : {s.islower()}")
print(f"s.isupper() : {s.isupper()}")
print(f"s.istitle() : {s.istitle()}")
print(f"s.isspace() : {s.isspace()}")

# sorted(s) -- sort the characters in the string and returns list
# chr(int) -- returns the character at passed ASCII value we passed
# ord(character) -- will return the ASCII value of the passed character

s = 'debacle'
print(f"The original string : {s}")
print(f"The original string after sorting is : {sorted(s)}")  # sorted method returns a list
print(f"The character at the ASCII value 100 is : {chr(100)}")
print(f"The ASCII value of the character 'd' is : {ord('d')}")

# slice operator -- used to extract substring from the main string
# syntax :- s[begin : end : step]
# step value can be either positive or negative
# If the step value is positive the slice operator will move from left to right from begin to end - 1 index
# In forward direction the default value of begin is 0 and the default of end is the length of the string
# If the step value is negative the slice operator will move from right to left from begin to end + 1 index
# In the backward direction the default value of begin is -1 and the default value of end is -(length_of_the_string + 1)
# If the end in backward direction is -1 then the result is always empty

s = '0123456789'
print(f"The original string : {s}")
print(f"s[1:5] : {s[1:5]}")  # will return all the characters starting from index 1 to 4
print(f"s[:4] : {s[:4]}")  # will return all the characters starting from index 0 to 3
print(f"s[2:] : {s[2:]}")  # will return all the characters starting from index 2 till end of the string
print(f"s[:] : {s[:]}")  # will return a duplicate copy of the original string
print(f"s[-1:-4] : {s[-1:-4]}")  # since we can't go from -1 to -4 in forward direction it returns empty string
print(f"s[-4:-1] : {s[-4:-1]}")  # will return all the characters from -4 to -2 index
print(f"s[100:] : {s[100:]}")  # slice operator won't throw any error even when the index doesn't exist in string it just returns empty string
print(f"s[1:7:2] : {s[1:7:2]}")  # will return every second character starting from index 1 to 6

print(f"s[::-1] : {s[::-1]}")  # will print the string in reverse order
print(f"s[2:8:-1] : {s[2:8:-1]}")  # we can't go in reverse direction from index 2 to 9 hence it returns empty string
print(f"s[8:2:-1] : {s[8:2:-1]}")  # 876543
print(f"s[-1:-6:-1] : {s[-1:-6:-1]}")  # 98765
print(f"s[2:-5:1] : {s[2:-5:1]}")  # 234
print(f"s[1:6:-2] : {s[1:6:-2]}")  # empty string
print(f"s[0:-5:-5] : {s[0:-5:-5]}")  # empty string
print(f"s[-1::-1] : {s[-1::-1]}")  # 9876543210
print(f"s[:0:-1] : {s[:0:-1]}")  # 987654321
print(f"s[-5:0:-9] : {s[-5:0:-9]}")  # 5
print(f"s[2:-1:-1] : {s[2:-1:-1]}")  # since the end in reverse direction is -1 the result is always empty

# Program to print the string in reverse order

s = "Dharani Kumar Gopavaram"

# 1st way is using slice operator

print(f"The reverse of the string {s} is : {s[::-1]}")

# 2nd way is to use the reversed function

print(f"The reverse of the string {s} is : {''.join(reversed(s))}")

# 3rd way by writing code

pos = len(s) - 1
reversed_s = ''
while pos >= 0:
    reversed_s += s[pos]
    pos -= 1

print(f"The reverse of the string {s} is : {reversed_s}")

# Input :- Dharani Kumar Gopavaram
# Output :- Gopavaram Kumar Dharani

s = "Dharani Kumar Gopavaram"
print(f"The input is : {s}")
print(f"The output is : {' '.join(s.split()[::-1])}")

# Input :- Durga Software Solutions
# Output :- agruD erawtfoS snoituloS

s = "Durga Software Solutions"
print(f"The input is : {s}")
print(f"The output is : {' '.join([word[::-1] for word in s.split()])}")

# Print the characters at even and odd position

s = "Dharani Kumar Gopavaram"

# using slice operator
print(f"The characters at even position are : {s[::2]}")
print(f"The characters at odd position are : {s[1::2]}")

# without using slice operator
even_char = odd_char = ''
for i in range(0, len(s), 2):
    try:
        even_char += s[i]
        odd_char += s[i + 1]
    except IndexError:
        break

print(f"The characters at even position are : {even_char}")
print(f"The characters at odd position are : {odd_char}")

# Input :- B4A1D3
# Output :- ABD134

s = "B4A1D3"
print(f"The input is : {s}")
chars = digits = ''
for c in s:
    if c.isdigit():
        digits += c
    else:
        chars += c

print(f"The output is : {''.join(sorted(chars)) + ''.join(sorted(digits))}")

# Input :- a20b3
# Output :- aaaaaaaaaaaaaaaaaaaabababa

s = "a20b3"
print(f"The input is : {s}")

found_digits = found_chars = output = ''

for c in s:
    if c.isdigit():
        found_digits += c
    else:
        if len(found_digits) > 0:
            output += found_chars * int(found_digits)
            found_digits = ''
            found_chars = c
        else:
            found_chars += c

if len(found_digits) > 0:
    output += found_chars * int(found_digits)
else:
    output += found_chars

print(f"The output is : {output}")

# Remove duplicate characters from the string

s = 'abbccdd'
print(f"The input is : {s}")

# using set but the order will be lost
print(f"The string without duplicate characters is : {''.join(set(s))}")

# by writing the code
no_duplicate_string = ''

for c in s:
    if c not in no_duplicate_string:
        no_duplicate_string += c

print(f"The string without duplicate characters is : {no_duplicate_string}")  # order won't be lost

# Print the number of occurrences of every character in the string

s = 'abbccdd'
d = {}

for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

for k, v in d.items():
    print(f"{k} -> {v} times")
