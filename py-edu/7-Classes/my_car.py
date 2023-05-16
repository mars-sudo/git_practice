# Importing a Single Class

from car import Car 
# from car import ElectricCar
# from car import Car, ElectricCar 
# import car 
# from car import ElectricCar as EC

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Importing classes is an effective way to program. 

# my_prius = Car('toyota', 'prius', 2022) - Car is the class and 'toyota' is the attributes
# print(my_prius.get_description_name()) - my_prius is the instance, get_descriptive name is the method

# my_corrola = car.Car('toyota','corrola', 2013)

# Class names should be written in CamelCase.
# Captitalize the first letter of each word in the name and don't use underscores
# Instance and module names in lowercase with underscores between words
# Every class should have a docstring immediatley following the class definition. 
