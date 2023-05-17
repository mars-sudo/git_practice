# Whatever the focus of the program, it'll store the information users provide
# in data structures such as lists and dictionaries. 
# When users close a program, you'll want to save the information they entered.
# A simple way to do this involves storing your data using the json module. 
#json - javascript object notation

# json.dump() functions takes two arguements: 
# a piece of data to store
# a file object it can use to store the data

import json

numbers = [2,3,5,7,11,13] # list of numbers

filename = 'numbers.json'
with open(filename, 'w') as f: # the variable f is used to represent file_objects
    json.dump(numbers, f) # numbers is the data store, f is the file object to store the data

