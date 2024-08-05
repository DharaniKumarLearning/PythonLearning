"""
argv is the variable which holds all the command line arguments
The type of the variable argv is list
The argv variable is present in sys module
The first value of the argv variable is the filename where we write our code
If you want to make a command line argument with space as a single argument then enclose the
    command line argument with double quotes single quotes won't work in this case
"""

from sys import argv

print(f"The type of the variable argv is : {type(argv)}")
print(f"The values present in argv variable is : {argv}")
print(f"The other command line arguments other than the filename are : {argv[1:]}")

cmd_args_sum = 0
for val in argv[1:]:
    cmd_args_sum += int(val)

print(f"The sum of the command line arguments is : {cmd_args_sum}")


