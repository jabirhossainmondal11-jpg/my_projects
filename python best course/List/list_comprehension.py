# List comprehension offers a shorter syntax
#  when you want to create a new list based on the values of an existing list.

'''
Example:

Based on a list of fruits, you want a new list,
 containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to 
write a for statement with a conditional test inside:
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# NOTE - with list comprehension you can do all with only line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# THE SYNRAX--
# newlist = [expression for item in iterable if condition == True]
# [কী রাখব for কোথা থেকে নেব if শর্ত]

# The condition is like a filter that only accepts the items that evaluate to True.

newlist = [x for x in fruits if x != "apple"]
print(newlist)
# The condition if x != "apple"  will return True
#  for all elements other than "apple",
#  making the new list contain all fruits except "apple.

# The condition is optional and can be omitted:
newlist = [x for x in fruits]  # With no if statement:


# Iterable--
# The iterable can be any iterable object, like a list, tuple, set etc.

# you can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

# same example with a condition:
newlist = [x for x in range(10) if x < 5]
print(newlist)


# Expression--
# The expression is the current item in the iteration, but is is aslo the outcome, which you
# manipulate before it ends up like a list list item in the new list:
newlist = [x.upper() for x in fruits]
print(newlist)


# You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]
print(newlist)


# The expression can also contain conditions,
#  not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
