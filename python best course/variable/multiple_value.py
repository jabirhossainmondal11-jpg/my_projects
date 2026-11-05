# Many values to multiple varibles
# Python allows you to assign values to multiple variables in one line:
x, y, z = "orange", "banana", "cherry"
# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# one value to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
"""if you have a collection of values in a list, tuple etc. Python allows you 
to extract the values into variables. This is called unpacking."""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
