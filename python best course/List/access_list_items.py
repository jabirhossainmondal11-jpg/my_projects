# List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Negative indexing means start from the end
# NOTE- -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# Range of Index-
# You can specify a range of indexes by specifying where to start and where to end the range.
# NOTE When specifying a range, the return value will be **a new list** with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# return the third, fourth and fifth item:
print(thislist[2:5])

# NOTE: The search will start at index 2 (included) and end at index 5 (not included).


# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to, but NOT including, "kiwi"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])



#By leaving out the end value, the range will go on to the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#This example returns the items from "cherry" to the end:
print(thislist[2:])


#Specify negative indexes if you want to start the search from the end of the list:


#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])



#Check if Item Exists--
#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, \"apple\" is in the fruits list.")