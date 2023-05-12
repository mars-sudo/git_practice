cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car =="bmw":  
        print(car.upper())
    else:
        print(car.title())

# This can also be called a conditional test, for example if a username is unique as both a upper and lowercase. 
# Equality Operator - ==
# Inequality Operator - !=

requested_topping ='mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age = 23
age < 25 # The age is less than 25 --> True
age <= 25 # The age is less than or equal too 25 --> True
age > 25 # The age is greater than 25 --> False
age >= 25 # The age is greater than or equal to 25 --> FALSE

temp_0 = 70
temp_1 = 90
if (temp_0 >= 50) and (temp_1 >= 90):
    print("Both temperatures are greater than 50.")

temp_2 = 75
temp_3 = 88
if (temp_2 <= 70) or (temp_3 <= 88):
    print("One or both temperatures are greater than 50.")