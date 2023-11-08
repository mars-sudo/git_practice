# Functions are named blocks of code that are designed to do one specific job. 
# Styling Functions
# Functions should have descriptinve names, and these names should use lowercase letters and underscores

# Every functions should have a comment that explains concisely what the function does

# def function_name(value_0, parameter_1='value')

# def function_name(
#                   parameter_0, parameter_1,
#                   parameter_2, parameter3  ):
#       function body

def greet_user():
    """Display a simple greeting."""
    print("Hello")

greet_user()

# Definition function name is greet_person - arguement 'username'.
def greet_person(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}") 
greet_person('Emmanual')
# Pass the parameter 'Emmanual' to function greet_person - value assigned to the arguement is username.


# Positional arguments - order matters
def describe_pet(animal_type, pet_name):
    """Display informaiton about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('hamster','ryan')
describe_pet('dog','eddie')

# Keyword arguguement are name-value pairs that you pass to a function - order doesn't matter.
def list_book(book_author,book_subject):
    """Display information about authors and books"""
    print(f"\nThe books author is {book_author}, subject is {book_subject}.")

list_book(book_subject='Learning', book_author='Jim Kwik')

# Default values
def func_0(arg_1,arg_2='default'):
    """Default value practice function"""
    print(f"\nThe first argument is an {arg_1}, the second is {arg_2}.")
func_0(arg_1='example')
func_0(arg_1='example2',arg_2='explicit argument')

# Positional arguements, keyword arguements and default values can all be used together
def func_1(positional,keyword,default='default'):
    print(f"\nThis is the {positional},this is the {keyword}, this is just {default}.")
func_1(positional='positional',keyword='keyword')

# A function can process data and then return a value or set of values, this is called return value.
def func_2(first_name,last_name):
    """Return full name"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician_0 = func_2('jimi','hendrix')
print(f"\n{musician_0}")  

# Optional Arguements
def get_formatted_name(first_name, last_name, middle_name=''): # To work without the middle_name arg, we set it to an empty string
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician_1 = get_formatted_name('stevie', 'wonder')
musician_2 = get_formatted_name('dolly','parton', 'marie')
print(f"\n{musician_1}")
print(f"\n{musician_2}")

# Return a Dictionary
# This functions takes in parts of a name and returns a dictionary representing a person.
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician_3 = build_person('van','halen')
print(f"\n{musician_3}")


def build_person_2(first_name, last_name, age=None): #In conditional tests None evaluates to False
    """Return a dictionary of information about a persion."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician_4 = build_person_2('jimi', 'hendrix', age=27)
print(musician_4)

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease Tell me your name:")
    print("(enter'q' at any time to quit)")

    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last Name: ")
    if last_name == 'q':
        break
    
    formatted_name = get_formatted_name(first_name,last_name)
    print(f"\nHello, {formatted_name}!")



