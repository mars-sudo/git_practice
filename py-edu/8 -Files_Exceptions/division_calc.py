# Using exceptions to prevent crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try: # This isthe use of an exception
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: # This is the use of an exception
        print("You can't divide by 0!")
    else:
        print(answer)

# The above will produce a traceback error, which is not a good idea for security. 
# You can't divide by zero. 