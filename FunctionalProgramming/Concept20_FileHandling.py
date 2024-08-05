"""
When we have less information, and we want to store that information for future reference then we should go for files.
Files are a permanent way to store the data.
Types of files :
    1. text files -- used to store text data
    2. binary files -- used to store image, video files

If you want to perform any operation with files first you have to open the file
While opening the file we need to specify the purpose for which we are opening the file

To open the file we need to use the python's built-in open() function
    f = open(filename, mode)

The allowed modes in Python are :-
----------------------------------

    1. r ==> open an existing for file for read operation. If the file is not present we get FileNotFoundError
    2. w => open a file for write operation. If the file already exists the data will be overwritten otherwise it
        will create a new file
    3. a => open a file for append operation. If the file already exists it will start appending the data.
        If the file doesn't exist it will create a new file
    4. r+ => To read and write data to the file. The previous data in the file won't be deleted.
        The file pointer always point to the beginning of the file
    5. w+ => To perform write and read operation. In this case the data in the file will be overwritten
    6. a+ => To perform append and read operation. The file data won't be overwritten
    7. x => To open a file in exclusive mode for write operation. If the file already is available it will return
        FileExistsError

All these modes are applicable for text files.
If we want to work on binary files for all these modes we need to suffix the mode with b
rb, wb, ab, r+b, w+b, a+b, xb

After performing all the operations we are required to close the file
    f.close()

Various properties of the file object :-
----------------------------------------

    1. f.name -- To know the name of the file
    2. f.mode -- In which mode we opened the file
    3. f.closed -- returns the boolean value which indicates whether the file is closed or not
    4. f.readable() -- Is the file readable or not
    5. f.writable() -- If the file writable or not

Reading data from the file :-
-----------------------------

read() -- To read total data from the file
read(n) -- To read n characters from the file
readline() -- To read only one line
readlines() -- To read all the lines in the file into a list

"""

import os.path
import csv

base_dir = "/Users/dharanikumar/PycharmProjects/PythonLearningProject/UserDefinedFiles"
file1 = open(f'{base_dir}/abc.txt', 'w')
print(f"Filename : {file1.name}")
print(f"Filemode : {file1.mode}")
print(f"Is file readable : {file1.readable()}")
print(f"Is file writable : {file1.writable()}")
print(f"File closed : {file1.closed}")
file1.write("Dharani\n")
file1.write("Kumar\n")
file1.write("Gopavaram\n")
print("Data successfully written to the file")
file1.close()
print(f"File closed : {file1.closed}")

file2 = None
try:
    file2 = open(f'{base_dir}/xyz.txt', 'r')
except FileNotFoundError:
    print(f"The specified file doesn't exist in the directory {base_dir}")
finally:
    if file2 is not None:
        file2.close()

file3 = None
try:
    file3 = open(f"{base_dir}/dharani.txt", "x")
    print(f"File name : {file3.name}")
    print(f"File mode : {file3.mode}")
    print(f"Is file readable : {file3.readable()}")
    print(f"Is file writable : {file3.writable()}")
    print(f"Is file closed : {file3.closed}")
except FileExistsError:
    print("Exclusive mode doesn't accept a file which already exists")
finally:
    if file3 is not None:
        file3.close()
        print(f"Is file closed : {file3.closed}")

file4 = open(f"{base_dir}/abc.txt", "a")  # append method won't overwrite the file
file4.write("John\n")  # If we want to write one line at a time we can use the write method
file4.write("Ram, ")  # If we don't specify \n at the end it will get appended to the same line
file4.write("Robert\n")
sample_list = ["Bunny\n", "Sunny\n", "Kumar"]
file4.writelines(sample_list)  # If we want to write multiple lines we need to use writelines method
# The writelines method accepts an iterator only
file4.close()
print("Data successfully appended to the file")

# reading data from the file

# read method

file5 = open(f"{base_dir}/abc.txt", "r")
data = file5.read()  # This will convert the entire file data to string
print(f"The type of the variable data is : {type(data)}")
print(f"The data in the file {base_dir}/abc.txt is :- ")
print(data)
file5.close()

# read(n) -- reading characters method

file6 = open(f"{base_dir}/abc.txt", "r")
first_5_char = file6.read(5)
print(f"The first 10 characters in the file is :- {first_5_char}")
file6.close()

# reading line by line

print(f"The first 3 lines in the file are :- ")
file7 = open(f"{base_dir}/abc.txt", "r")
print(file7.readline(), end='')
print(file7.readline(), end='')
print(file7.readline(), end='')
file7.close()

# reading the entire content of the file to list
print("Saving the entire content of the file to list")
file8 = open(f"{base_dir}/abc.txt", "r")
data_list = file8.readlines()
print(f"The type of the variable data_list is : {type(data_list)}")
for line in data_list:
    print(line, end='')
print()

# using with keyword to perform operations on the file which will automatically close the file once we are done
# with is also called context manager

with open(f"{base_dir}/practice.txt", "w") as f:
    f.write("Practice line-1\n")
    f.write("Practice line-2\n")
    f.write("Practice line-3\n")
    print(f"Is file closed :- {f.closed}")
print("came out of the with block")
print(f"Is file closed :- {f.closed}")

# tell() method is used to know the current position of the cursor

with open(f"{base_dir}/practice.txt", "r") as f:
    print(f.tell())  # The current position of the file pointer will be always zero
    print(f.readline(), end='')
    print(f.tell())  # Once we read some data the position of the file pointer will automatically move
    print(f.read(4))
    print(f.tell())

# seek() method is used to move the file pointer to a specific position

data = "All students are STUPIDS"
with open(f"{base_dir}/file_practice.txt", "w+") as f:
    f.write(data)  # writing the data to the file
    print("Data successfully written to the file")
    print("Reading data from the file")
    print(f.read(), end='')
    print(f"The current position of the cursor is : {f.tell()}")
    f.seek(17)  # Moving the file pointer to the 17th position
    print(f"The current position of the cursor is : {f.tell()}")
    f.write("GEMS!!!")  # overriding the data starting from 17th position
    f.seek(0)
    print("Data in the file after modification")
    print(f.read())


# Sample program to check whether a file exists or not
# If it is available read the content and display the number of lines, characters and words present in the file

filename = input("Enter the filename :- ")
correct_file_name = f"{base_dir}/{filename}"
if os.path.exists(correct_file_name):  # os module exists method help us to check whether a file exists or not
    with open(correct_file_name, "r") as f:
        line_count = word_count = character_count = 0
        for line in f:  # instead of using readline or readlines method we can directly use the file pointer to read the data
            line_count += 1
            word_count += len(line.split())
            character_count += len(line)
        print(f"The number of lines present in the file is :- {line_count}")
        print(f"The number of words present in the file is :- {word_count}")
        print(f"The number of characters present in the file is :- {character_count}")
else:
    print("The specified file doesn't exist")

# copy and paste an image using file handling

with open("/Users/dharanikumar/Desktop/image1.png", "rb") as f1:
    with open("/Users/dharanikumar/Desktop/image1_copy.png", "wb") as f2:
        for line in f1:
            f2.write(line)
        print("The image is successfully copied")


# working with csv data in Python
# We have an in-built csv module which will help us in easily reading, parsing, etc., with the csv files

with open(f"{base_dir}/sample_csv_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)  # creating a csv reader object we can optionally pass delimiter if the file is not comma separated
    next(csv_reader)  # next() method will help us to skip the header
    with open(f"{base_dir}/new_csv_data.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="-")
        # If there is a (-) in the data we are writing the writer method will insert a double quote for that data
        for line in csv_reader:  # The data in csv_reader will be lost once it is consumed
            csv_writer.writerow([line[0], line[2]])
        print("Data successfully written to the csv file")


with open(f"{base_dir}/sample_csv_data.csv", "r") as csv_file:
    csv_reader_2 = csv.DictReader(csv_file)
    with open(f"{base_dir}/dict_writer.csv", "w") as new_file:
        key_names = ['Series_reference', 'Period', 'Data_value', 'Suppressed', 'STATUS', 'UNITS', 'Magnitude','Subject', 'Group', 'Series_title_1', 'Series_title_2', 'Series_title_3', 'Series_title_4', 'Series_title_5']
        csv_writer_2 = csv.DictWriter(new_file, fieldnames=key_names, delimiter='\t')
        csv_writer_2.writeheader()
        for li in csv_reader_2:
            csv_writer_2.writerow(li)
        print("Data successfully written to the csv file")
