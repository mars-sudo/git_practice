# Now we'll write a program to greet a user whose name has already been stored.

import json

filename = 'username.json' # assign a variable to the json file

with open(filename) as f:
    username = json.load(f) # here we use json.load() to read the information stored in username.json
    print(f"Welcome back, {username}!")