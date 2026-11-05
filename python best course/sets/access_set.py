
#Access items
# You cannot access items in a set by referring to an index or key.
# but you can loop through the set items using a for loop, or ask if a specified value is
# present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# check if "banana" is NOT in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#NOTE -Once a set is created, you cannot change its items, but you can add new items.


