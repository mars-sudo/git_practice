# Intro to Lists
# A list is a collection of items in a particular order, square brackets [] indicate a list. 
countries = ['usa', 'france', 'mexico', 'japan', 'korea']
print(countries)
print(countries[0])
print(countries[1].title())

message = f"The {countries[0].upper()} is country of my birth.\t\n"
print(message)

countries[0] = 'canada'
print(countries)
countries.append('usa')
print(countries)
countries.insert(0, 'colombia')
print(countries)
del countries[0]
print(countries)
# pop() method removes the last item in a list, but lets you work with that item after remove it. 
popped_countries = countries.pop()
print(countries)
print(popped_countries)

countries_visited = countries.pop(0)
print(f"I have visitied {countries_visited.title()}.")

countries.remove('japan')
print(countries)

# countries.sort() # The countries are now in alphabetical order, we can never revert to the original order. 
# countries.sort(reverse=True)
print(sorted(countries)) # the sorted functions lets you display your list but doesn't affect the actual order. 
print(countries)
print(len(countries)) # using the len() function we get the length of the list. 
# To access the last item in a list us the index -1
print(countries[-1])

