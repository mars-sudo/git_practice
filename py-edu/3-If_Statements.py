# When you want to do the same action with every item in a list, you can use Python's for loop
book_genre = ['biology', 'history', 'math']
for book in book_genre: 
    print(f"{book}")
    print(f"{book.upper()}, is a typical book used in school.")
    print(f"In you first year of college, you will need a {book.title()} book.")

print("Get ready for your first day of class!") # Lines of code after the for loop are not indented are executed once. 

# IMPORTANT - Don't forget the Colon on the for loop

# MAKING NUMERICAL LISTS
# Lists are ideal for storing sets of numbers (temperatures, distances, population sizes, latitude and longitude values, etc.)

# The range() function makes it easy to generate a series of numbers
for value in range(1, 6):
    print(value)

# Here we make a list of the numbers by converting the range() function list()
numbers = list(range(1, 6))
print(numbers)

# Here the range() functions starts with the value of 2 and then adds 2 to that value repeatedly until it reaches or passes the end value of 11. 
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Create an empty list with the variable named 'squares'; for the variable named 'value' in a range() function between 1 and 11, create a variable named 'square' 
# and make this variable equal the variable 'value' to the exponent of 2. Create another variable named 'squares', and append the value of 'square' to this variable. 
# Lastly, print the variable 'squares'. So 1 to the power of 2 eqauls 1,2 to the power of 2 equals 4, etc.
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# A more concise version of the above code. 
squares_concise = []
for value in range(1,11):
    squares_concise.append(value**2)

print(squares_concise)

# Using list comprehensions
squares_list_comprehensions = [value**2 for value in range(1,11)]
print(squares_list_comprehensions)

digits =[1,2,3,4,5,6]
print(min(digits))
print(max(digits))
print(sum(digits))

# Lists Practice - Page 60
numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers)

millions =[million for million in range(1,1000001)]
print(min(millions))
print(max(millions))
print(sum(millions))

odd_numbers =[odd for odd in range(1, 20, 2)]
print(odd_numbers)

threes = [three for three in range(3, 30, 3)]
print(threes)

cubes = [cube**3 for cube in range(1,11)]
print(cubes)

empty_list = []
for value in range(1,4):
    exponent = value**2
    empty_list.append(exponent)
print(empty_list)

# Slicing a list is specifying which elements of the which you are calling
players = ['heather','jonathan','peter','alicia','dakota']
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[1:]) 
# You can include a third value in the brackets indicating a slice. If a thrid value is included, this tells
# Python how many items to skip between items in the specified range.
fruits = ['apples','bananas','strawberries','blueberries','grapes']
print(fruits[0:1]) 
print(fruits[0:2])
print(fruits[0::2])
print(fruits[0::3])
print(fruits[1::3])

# Looping through a slice
veggies = ['broccoli','parsnip','radish','peas','cauliflower']

print("\n Here are the veggies you will need for the curry:")
for veggies in veggies[:3]:
    print(veggies.title())

# Copying a list
my_foods = ['pizza','burgers','chips']
friend_foods = my_foods[:] # To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). 
print("My favorite foods are:") 
print(my_foods)

print("\n My friends favorite food is:")
friend_foods.append('burritos')
print(friend_foods)

# Slice Exercises page 65
books = ['linux bible','pen testing','learning python','atomic habits','skin in the game']
print("\t\n The first three books to read of my book list are:")
print(books[:3])

print("\t\t\n The middle three books I need to read are:")
print(books[1:4])

print("\t\t\n The last three books I need to read are:")
print(books[2::])

nachos = ['chips','fries','poutine','casserol']
nachos.append('dip')
gourmet_nachos = nachos[:]

print("\n\t My favorite nacho types are:")
nachos.append('pasta')
print(nachos)

print("\n\t The professionals make nacho types like:")
gourmet_nachos.append('cheese')
print(gourmet_nachos)

temperature = [temp for temp in range(1,21)]
print(temperature)
print(temperature[0:3])
print(temperature[1:4])

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




