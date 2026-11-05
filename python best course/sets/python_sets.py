# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# * NOTE: Set items are unchangeable, but you can remove items and add new items.

# sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)
# NOTE: Sets are unordered, so you cannot be sure in which order the items will appear.


# SET ITEMS -
# set items are unordered, unchangeable, and do not allow dublicate values.


# UNORDERED -
# unordered means that the items in a set do not have a defined order.
# set items can appear in different order every tiem you use them, and cannot be referred
# to by index or key


# UNCHANGEABLE --
# Set items are unchangeable,
#  meaning that we cannot change the items after the set has been created.

# NOTE -Once a set is created, you cannot change its items,
#  but you can remove items and add new items.


# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# NOTE: The values True and 1 are considered the same value in sets,
#  and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


# NOTE: The values False
#     and 0 are considered the same value in sets, and are treated as duplicates:


thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# set items can be any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


# A set can contain different data types:
set1 = {"abc", 34, True, "male"}


# from python's perpective, sets are defined as objects with the data type 'set':
# <class 'set'>

myset = {"apple", "banana", "cherry"}
print(type(myset))


# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry"))
print(thisset)

