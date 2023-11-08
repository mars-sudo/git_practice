filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline().replace("ÿþ", "")
print(lines)

# To write text to a file, you need to call open() with a second argument
# telling Python that you want to write to the file. 

file = 'programming.txt'
with open(file, 'w') as new_file:
    new_file.write("I am always learning programming.\n")
    new_file.write("It is a journey, not a destination.\n")

# In read mode open('filename', 'r')
# In write mode open('file', 'w')
# In append mode open('file' , 'a') - when you open in append, Python doesn't erase the contents from before
# To read and write open('file', 'r+')

with open(file, 'a') as new_file:
    new_file.write("I like programming.\n")
    new_file.write("It is a fun challenge with big rewards.\n")


