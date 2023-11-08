# Conditional Tests
emotions = ['grateful','sad','hopeful','grief']

for emotion in emotions:
    if emotion == 'grief':
        print(emotion.upper())
    else:
        print(emotion.lower())


requested_breakfast = 'oatmeal'
if requested_breakfast != 'bagels': # The check for inequality is !=
    print("Do you have any eggs?")


lunch =['poke','saimin','pad thai']
print('poke' in lunch) 
# To find out whether a particular value is already in a list, use the keyword in

banned_users = ['vince','john','stacey']
user ='rashid'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expression
game_active = True
can_edit = False

# Syntax
# if conditional_test:
#   do something

# == equals
# != doesn't equal
# < less than
# <= less than or equal too
# > greater than
# >= greater than or equal too 

age = 35
if age >= 30:
    print("You have more life to live!")
else:
    print("This is another great year to be here!")

# Admission for anyone under age 4 is free
# Admission for anyone between the ages of 4 and 18 is $25
# Admission for anyone age 18 or older is $40

client_age = 12
if client_age <4:
    print("Your admission is $0.")
elif client_age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# or
 
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age == 35:
    price = 38.5
elif age >= 65:
    price = 40
print(f"Your admission cost is ${price}.")

# The else block is a catchall statement. It matches any condition that wasn't matched 
# by a specific if or elif test. 
# If you have a specific findal condition you are testing for, consider using a final elif block 
# and omit the else block. 

dinner_carbs = ['rice','noodles','potatoes']

if 'rice' in dinner_carbs:
    print("Adding rice.")
if 'noodles' in dinner_carbs:
    print("Adding noodles.")
if 'bread' in dinner_carbs:
    print("Adding bread.")

print("\nDinner Carbs are ready!")

for dinner_carb in dinner_carbs:
    if dinner_carb == 'potatoes':
        print("Sorry, we've run out of potatoes right now.")
    else:
        print(f"\nAdding {dinner_carb}.")


available_veggies = ['cabbage','carrots','broccoli']
dinner_veggies =['cabbage']

for dinner_veggie in dinner_veggies:
        if dinner_veggie in available_veggies:
            print(f"Adding {dinner_veggie}.")
else:
    print("Are you sure you don't want another veggies?")