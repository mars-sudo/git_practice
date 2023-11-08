# Reading an Entire File
with open('pi_digits.txt') as file_object:
    contents = file_object.read().replace("ÿþ", "")
print(contents.rstrip())

# To do any work with a file, even just printing its content
# you first need to open the file to access it. 
# The open() function needs one arguement: the name of the file you want to open. 
# The open() function returns an object representing pi_digits.txt. 
# Python assigns this object to file_object.
# The keyword with closes the file once access to it is no longer needed. 

# with open('text_files/filename.txt') as file_object

# file_path = '/Users/Temp/filename.txt'
# with open(file_path) as file_object:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Make a List of Lines from a File
with open (filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# Working with File's Contents 
with open (filename) as file_object:
    lines = file_object.readlines()

pi_string = '' # To use this as a number you'll need to use the int() or float () function
for line in lines:
    int(pi_string)
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# answer = int(first_number) / int(second_number)


