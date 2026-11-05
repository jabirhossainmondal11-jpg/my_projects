# ou can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative indexing means start from the end.
#-1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Range of indexes--

#You can specify a range of indexes
#  by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new tuple with the specified items.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#By leaving out the start value, the range will start at the first item:

#This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#By leaving out the end value, the range will go on to the end of the tuple:
thistuple =  ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])



#Specify negative indexes if you want to start the search from the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#This example returns the items from index -4 (included) to index -1 (excluded)


#Check if item exists
#To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple.")
    