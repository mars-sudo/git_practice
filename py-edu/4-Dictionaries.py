# Variables
print("Hello World")
name = "mars"
print(f"Hello {name.title()}")
math = 2 + 5
print(f"{math}\t\n")

# Lists
feelings =['peace','joy','clarity','optimisim']
print(feelings)
print(feelings[0])
print(f"Today I am feeling lots of {feelings[0].upper()}!")

feelings.append('grief')
print(feelings)
del feelings[1]
print(feelings)

# For Loops
empty_list = []
for value in range(1,5):
    multiple_of_two = value*2
    empty_list.append(multiple_of_two)
print(empty_list)

empty_list_2 = []
for value_2 in range(1,5):
    empty_list_2.append(value_2*2)
print(empty_list_2)

empty_list_3 = [value_3*2 for value_3 in range(1,5)]
print(empty_list_3)

# Slicing
print(feelings)
print(feelings[0:2])
print(feelings[0:3])
print(feelings[1::2])

# Tuples
# Tuples are lists that are immutable, the value cannot change. 
# A tuple uses parentheses instead of square brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping over Tuples
for dimension in dimensions:
    print(dimension)

# Pg 68
foods = ('ramen','korean-bbq','poke','thai','local')
for food in foods:
    print(food)

#foods[0]=('sushi')
#print (food)

foods = ('chinese','fast-food','ramen','korean-bbq','poke','thai','hawaiian')
for food in foods:
    print (f"\n{food}")






