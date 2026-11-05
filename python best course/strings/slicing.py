#slicing
#You can return a range of characters by using the slice syntax.
#specify the start index and the end index, separated by a colon, to return a part of the string.


b = "Hello, World"
print(b[2:5]) # use variable name and start index and end index #first character has index 0

#By leaving out the start index, the range will start at the first character:

b = "Hello, World"
print(b[:5])

#By leaving out the end index, the range will go to the end:
b = "Hello, World"
print(b[2:])


"""Negative Indexing"""
#Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])

name = "Jabir Hossain"
print(name[-7:-1])