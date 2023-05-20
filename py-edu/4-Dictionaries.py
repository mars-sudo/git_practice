# A Dictionary is a collection of key-value pairs.
# Each key is connected to a value and you can use a key to access the value associated with that key.
# A key-value is a set of values associated with each other. 

house_0 = {'location':'seattle', 'size':'900 sqft','bedrooms':'2'}
print(house_0)
print(house_0['location'])
print(house_0['size'])
del house_0['bedrooms'] # Be aware that the deleted key-value pair is removed permanently. 
print(house_0)

new_house = house_0['size']
print(f"The new house size is {new_house}.\n")

house_0['amenities'] = 'pool'
house_0['neigborhood']='downtown'
print(house_0)

house_1 ={}
house_1['location']='austin'
house_1['size']='2,000 sqft'
print(f"the current location of this house 1 is in {house_1['location'].title()}\n")

house_1['location']='toronto'
print(f"the new location of this house 1 is in {house_1['location'].title()}\n")

print(f"Original position of house 0 is : {house_0['location'].title()}.\n")

#########################################################################################################

# You can also use a dictionary to store one kind of information about many objects. 
# For example, say you want to poll a number of people and ask them what their favorite programming language is. 
# A dictionary is useful for storing the resultes of a simple poll.
favorite_languages ={
    'lucy':'c',
    'reina':'go',
    'keisha':'php',
    'david':'python'
}

language = favorite_languages['keisha'].title()
print(f"Keisha's favorite language is {language}.\n")
print(f"{favorite_languages['reina'].title()}\n")

# create names for the two variables that will hold the key and value in each key-value pair.
# you can choose any names you want for these two variables. 

# SYNTAX - for k, v in dictionary.items():
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ['reina','david']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'claude' not in favorite_languages.keys():
    print(f"Claude, please take the poll.")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, is now in a sorted list.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.lower())

for language in set(favorite_languages.values()):  
    print(language.upper())
# When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list
# and builds a set from those items. 


# For dictionaries you can use get() method to set a default value that will be retured if the requested key doesn't exist
alien_1 = {'color': 'green','speed':'slow'}
point_value = alien_1.get('points','No point value assigned.')
print(f"\n{point_value}\n")

# You can loop through all of a dictionary's key-value pairs, through its keys, or through its values. 
user_0 ={
    'username':'mkalapana',
    'first':'mike',
    'last':'kalapana'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


###########################################################################
# Modify values in Dictionary
alien_0 ={'x_position':0, 'y-position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}.\n")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed. 
if alien_0['speed'] =='slow':
    x_increment = 1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The new position is: {alien_0['x_position']}.\n")
################################################################################################

# Nesting 

## A List of Dictionaries

npc_0 = {'color':'red','points':'3'}
npc_1 = {'color':'green','points':'2'}
npc_2 = {'color':'blue','points':'1'}

npcs =[npc_0,npc_1,npc_2]

for npc in npcs:
    print(npc)

# Make an empty list for storing npc's
npcs = []

# Make 30 red npc's
for npc_number in range(30):
    new_npc = {'color':'red','points':'5'}
    npcs.append(new_npc)

# Show the first 5 npc's
for npc in npcs[:5]:
    print(npc)

print("...")

for npc in npcs[:3]:
    if npc['color'] =='red':
        npc['color'] = 'orange'
        npc['points'] = '8'
    print(npc)

# A List in a Dictionary
pizza = {
    'crust':'thick',
    'toppings' : ['mushrooms','olives'],
}

print(f"You ordered a {pizza['crust']} -crust pizza with the following toppings")
for topping in pizza['toppings']:
    print("\t" + topping)

examples = {
    'person_1':['english','spanish'],
    'person_2':['french','swedish'],
    'person_3':['hindi','mandarin'],
}

for name, languages in examples.items():
    print(f"\n{name.title()}'s languages are:")
    for language in languages:
        print(f"\t{language.upper()}")