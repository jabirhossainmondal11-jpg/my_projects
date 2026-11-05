#Python has two built-in methods that you can use on tuples.

'''

Method             	Description

count()	           Returns the number of times a specified value occurs in a tuple

index()	           Searches the tuple for a specified value and returns
                   the position of where it was found
'''


mytuple = ("apple", "banana", "apple", "cherry", "apple")

print(mytuple.count("apple"))
#কোনো value কতবার আছে সেটা গুনে দেয়


mytuple = ("apple", "banana", "cherry", "orange")

print(mytuple.index("cherry"))
#কোনো value প্রথম কোথায় আছে তার position/index দেয়।

