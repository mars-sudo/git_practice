# Making an object from a class is called an instatntation
# You work with instances of a class. 
# You store classes in modules and import classes. 

## A function that's a part of a class is a method. 
## The __init__() method requires the self paramter and it must come first. 
## The self parameter must be included in the defenition
## because when Python calls this method later, the method will pass the self argument. 
## It gives the individual instance access to the attributes and methods in the class. 
## Variables that are accessible through instances are called attribues. 
## The below class has two methods defined:sit() and roll_over().

class Dog:
    """A simple attemt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

## A Class is a set of instructions for how to make an instance. 
my_dog = Dog('Holly','6') # This is a single instance. We assign instances to the variable 

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

## Naming Conventions
# Capitalized name like Dog refers to a class
# lowercass name like my_dog referes to a single instance created from a class
# To access the attributes from an instance we use dot notation my_dog.name
# We use dot notation to call any method defined in Dog.
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Rufus', '3') # This is the second instance.
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()