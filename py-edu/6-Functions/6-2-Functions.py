# When you pass a list to a function, the function gets direct access to the contents of the list
def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    

usernames = ['hannah','amanda','james']  # remember [] is a list, while {} is a dictionary
greet_user(usernames)

# When you pass a list to a function, the function can modify the list
# Any changes made to the list inside the funciton's body are permanent,
# allowing you to work efficiently even when you're dealing with large 
# amounts of data. 

def print_models(unprinted_designs, completed_models):
    """ 
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'mug', 'architecural landscape']
completed_models =[] # Send completed models to an empty list

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(size, *args): # The *toppings parameter collects as many arguments as the calling provides. the *param must be at the end.
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch piza with the following toppings:")
    for arg in args:
        print(f" -{arg}")

make_pizza(12,'supreme','pepperoni','anchovies')
make_pizza(24, 'sausage')

def build_profile(first, last, **user_info): # Often see parameter name **kwargs used to collect non-specific keyword arguments.
    """ Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstien',location='princeton',field='physics')
print(user_profile)

