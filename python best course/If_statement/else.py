#NOTE: The else statement must come last. You cannot have an elif after an else.

#checking even or odd numbers:
number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Complete if elif else chain
temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside!")
elif temperature > 10:
    print("It's cool outside!")
else:
    print("It's cold outside!")


#Else as Fallback--
# The else statement acts as a fallback that executes
#  when none of the preceding conditions are true. 
# This makes it useful for error handling, validation, and providing default values.  
Username =input("username:")

if len(Username) > 0:
    print(f"Welcome, {Username}!")
else:
    print("Error: Username cannot be empty")    

