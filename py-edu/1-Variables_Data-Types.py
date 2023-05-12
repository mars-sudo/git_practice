print("Hello world!")

message_1 = "Hello Python World"
print(message_1)

name = "godfrey winiferd"
print(name.title()) # A method is an aciton that Python can perform on one piece of data
print(name.upper())
print(name.lower()) # A method is followed by a set of parentheses

first_name = "juan"
last_name = "hernadez"
full_name = f"{first_name} {last_name}"
print(full_name)

message_2 = f"Hello, {full_name.title()}"
print(message_2)

language = ' python '
print(language.strip())
print(language.lstrip())
print(language.rstrip())

# Integers & Float - Python defaults to float
add = 2+3
sub = 3-2
multiply = 3*2
divide = 3/2
exponent = 3**2
modulus = 3%2
float_1 = 0.2+0.3
float_2 = 0.2 * 5
big_num = 500_000_000
x,y,z = 1,2,3


print(add)
print(sub)
print(multiply)
print(divide)
print(exponent)
print(modulus)
print(float_1)
print(float_2)
print(big_num)
print(x,y,z)