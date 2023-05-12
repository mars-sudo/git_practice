# A list is a collection of itemes in a particular order
food = ['pizza', 'burgers', 'hotdog','ramen']
print(food)
print(food[2])
print(food[1].title())
print(food[-1])

food_message = f"It is unhealthy to eat {food[1].title()} all the time."
print(food_message)

food[0] = 'sushi'
print(food)

food.append('shwarma')
print(food)

authors = []
authors.append('illouz')
authors.append('kahneman')
authors.append('nassim')
authors.append('matthes')
print(authors)

del authors[0]
print(authors)

popped_authors = authors.pop() #removes the last item from the list
print(f"The last author I read was {popped_authors.title()}.")

current_authors = authors.pop(0)
print(f"The current author I'm reading is {current_authors.title()}.")

authors.remove('nassim')

wood = ['oak','cherry','walnut','cedar']
wood.sort()
print(wood)
wood.sort(reverse=True)
print(wood)
wood.reverse()
print(wood)

print(len(wood))

drinks = ['coffee','water','tea','smoothie']

for drink in drinks:
    print(f"It is refresshing to have a {drink.title()}!")
    print(f"I can't wait to have another {drink.title()}.\n")

print("the for loop has ended.\n")

for int in range(1,5):
    print(int)

num = list(range(1,6))
print(num)

even_numbers = list(range(2,11,2)) 
print(even_numbers)
# the range() function starts with the value of 2 and then adds 2 to that value. 
# it adds 2 repeatedly until it reaches or passes the end value, 11. 

squares =[]
for value in range(1,11):
    square = value **2
    squares.append(square)

print(squares)
# loop through the each value from 1 to 10 using range() function the square that value. 

math = [numbers**2 for numbers in range (1,11)]
print(math)

digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

scents =['orange','lavendar','hazelnut','vanilla']
print(scents[0:3])
print(scents[1:4])
print(scents[0:4])
print(scents[-2:])

for scent in scents[:3]:
    print(scent.title())

smells = scents[:] # copy the list
print(smells)

scents.append('sandlewood')
smells.append('rose')
print(scents)
print(smells)

# Tuples are lists that cannot change. 
dimensions =(200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions =(300,60) # You can write over tupeles but can't change them like lists. 
print(dimensions)

