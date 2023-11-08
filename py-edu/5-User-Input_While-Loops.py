# Use the input() functions to accept user input
# the input() function pauses your program and waits for the user to enter some text. 

name = input("Please enter your name: ")
print(f"\nHello, {name}")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?" 
# the operator += takes the string that was assigned to prompt and adds the new string onto the end
name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you? ")
age = int(age) # You can have an int method or a float method
if age > 18:
    print("You're older than 18!")

number = input("Enter a number, and a I'll you if it's even or odd: ")
number = int(number)

if number % 2 == 0: # Modulo just tells you what the remainder is.
    print(f"\nThe number {number} is even.") 
# Even numbers are always divisible by 2, if the modulo of a number is two or zero then the number is even.
else:
    print(f"\nThe number {number} is odd.")

#############################################################################################################
# While loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # shorthand for current_number + 1

##########################################################################################


########################################################################################
# Using Break to Exit a loop
# To exit a while loop immediatley without running any remaining code in the loop, regardless of the results of any conditional test,
# use the break statement. 
# The break statement directs the flow of your program; you can use it to control which lines of code are executed and which
# aren't, so the program only executes code that you want it to, when you want it to. 

prompt_3 = "\nPlease enter the name of a city you have visited:"
prompt_3 += "\n(Enter 'quit' when you are finished.)"

while True: # A loop that starts with While True will run forever unless it reaches a break statement. 
    city = input(prompt_3)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

######################################################################################################
# Avoid infite loops
# this loop runs forever!
# x = 1
# while x <= 5:
#   print(x)
# Now the value of x will start at 1 but never change. 
# As a result, the conditional test x <= 5 will always evaluate to True and the while loop will run forever printing 1's


# this loop counts to 5
x = 1
while x<=5:
    print(x)
    x +=1 # This loop is counting from 1 to 5


########################################################################################################
# Moving items from one list to another
# Consider a list of newly registered but unverified users of a website. 
# After we verify these users, how can we move them toa separate list of confirmed users?

# Start with users that need to be verified, and an empty list ot hold confirmed users. 
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# Verify each user until there are no more confirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


##################################################################################
responses ={}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which emotion do you feel most frequently? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climate {response}.")







