"""
Python has the below flow control statements

    1. Conditional statements :- if, else, elif
    2. Iterative statements :- for, while
    3. Transfer control statements :- break, continue, pass

"""

name = input("Enter your name : ")
if name == "Dharani":
    print("Hello Dharani! Good Morning")
elif name == "Kavya":
    print("Hello Kavya! Good Morning")
else:
    print("Hello Guest Good Morning")
print("How are you?")

# for loop is used when we know the number of iterations in advance

s = "Dharani Kumar Gopavaram"
total_char_count = 0
for c in s:
    print(f"The character {c} is present at the +ve index {total_char_count}")
    total_char_count += 1
print(f"The total number of characters in the string is : {total_char_count}")

# while loop is used when we don't know the number of iterations in advance

i = 0
while i < len(s):
    print(f"The character at index {i} is : {s[i]}")
    i += 1

# Nested for loops

for i in range(4):
    for j in range(4):
        print(f"i = {i}, j = {j}")

# for loops with break and continue

for i in range(10):
    if i == 4:
        continue  # continue will skip the current iteration
    elif i == 6:
        break  # break will force the transfer to come out of loop
    print(f"The value of i is {i}")

# for loop with else
# The statements in else block will get executed if the break statement didn't get executed in the for loop

for i in range(10):
    if i == 6:
        break
    print(f"The value of i is : {i}")
else:
    print(f"The break statement didn't get executed in the for loop")

# else means loop without break
# syntactically in our Python program if we require a block that doesn't do anything we can use pass keyword
