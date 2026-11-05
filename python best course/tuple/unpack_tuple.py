# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Packing a tuple:
fruits = ("apple", "banana", "cherry")


# But, in Python, we are also allowed to extract
#  the values back into variables. This is called "unpacking":

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# NOTE-  The number of variables must match the number of values in the tuple,
#  if not, you must use an asterisk to collect the remaining values as a list.


# using Asterisk*:
# If the number of variables is less than the number of values, you can add * to the
#  variable name and the values will be assigned to the varibles as a list:

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# If the asterisk is added to another variable name than the last,
#     Python will assign values to the variable until the number of values
#      left matches the number of variables left.


# Add a list of values to the "topic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *topic, red) = fruits

print(green)
print(topic)
print(red)
