# Loop through a tuple
# you can loop through the tuple items by using a for loop.

# iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


# Loop through the index numbers:
# You can also loop through the tuple items by referring t their index number.
# Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])



#Using a while loop
# You can loop through the tuple items by using a while loop.
thistuple = ("apple", "banana", "cherry")   
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1