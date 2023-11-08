# Handling the FileNotfoundError Exception

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# the variable f represents a file_object
# use the encoding arguement when your system's default encoding doesn't match
# the file that's being read

# the string method split() can build a list of words from a string
title = "Discours de la methode"
print(title.split())

file = 'descartes.txt'
try:
    with open(file, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {file} has about {num_words} words.")
