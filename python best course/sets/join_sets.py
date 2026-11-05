# Join sets

# There are several ways to join two or more sets in python.---
'''
The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.


'''

# Union
# The union() method returns a new set with all items from both set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)


# you can use the | operator instead of the union() method, and you wil get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


# Join Multiple Sets-
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
# Join multiple sets with the union() method:
myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
# use | to join multiple sets
myset = set1 | set2 | set3 | set4
print(myset)


# Join a Set and a Tuple--
# NOTE-the union() method allows you to join a set with othe rdata types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# NOTE-he  | operator only allows you to join sets with sets,
# and not with other data types like you can with the  union() method.

# update
# The update() method inserts all items from one set into another.
# The update() changes the orginal set, and does not return a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# NOTE: Both union() and update() will exclude any duplicate items.

# intersection

# The intersecton() method will return a new set, that only contains the items that are
#  present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and uou will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)


'''
Note: The & operator only allows you to join sets with sets, 
and not with other data types like you can with the intersection() method.
'''


# NOTE-The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)



'''
The difference() method will return a new set 
that will contain only the items from the first set 
that are not present in the other set.
'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#You can use the - operator instead of the difference() method, 
# and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#NOTE: The - operator only allows you to join sets with sets, 
# and not with other data types like you can with the difference() method.



#Use the difference_update() method 
# to keep only the items from the first set that are not present in the other set:


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)



#The symmetric_difference() method 
# will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)


#You can use the ^ operator
#  instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)



#The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)
