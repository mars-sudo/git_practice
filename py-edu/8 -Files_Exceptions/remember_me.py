# Saving data with json is useful when you're working with user-generated data
# because if you don't store you user's informaiton somehow,
# you'll lose it when the program stops running. 

import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it. 


username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")


