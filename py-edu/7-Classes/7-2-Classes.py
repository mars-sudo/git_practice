class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Attributes can be defined without being passed as a parameter. 

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self): # This is a new method
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles # Original initialized attribute from method
    
my_new_car = Car('audi', 'a4', '2023')
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer() # This is a Method Call

## You can modify the attribute (self.odometer_reading) three ways
## First: change the value directly through an instance
## Second: set the value through a method
## Third: increment the value through a method

my_new_car.odometer_reading = 100 # change the value directly through an instance (notice the attribute)
my_new_car.read_odometer()

my_new_car.update_odometer(120) # the value was set in the method above, then updated in the method call
my_new_car.read_odometer()

my_new_car.increment_odometer(100) # increment the value through a method
my_new_car.read_odometer()

 
## When one class inherits from another, it takes on attributes and methods of the first class. 
## The original class is called the parent class, and the new class is the child class.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__ (self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year) 
        self.battery_size = 75
# The super() function is a special function that allows you to call a method from the parent class. 
# This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance 
# all the attribues defined in that method. 

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_electric_car = ElectricCar('toyota','prius', 2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()



my_electric_car.battery.describe_battery()


