# Loop through a list
# you can loop through the list items by using a for loop.

# print all items through the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


#Loop Through the Index Numbers--
#you can also loop through the list items by referring to their index number.
#use the range() and len() funtions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)) :
    print(thislist[i])



#Using a While Loop---
#You can loop through the list items by using a while loop. 

#Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by referring to their indexes.

#Remember to increase the index by 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1



#Looping Using List Comprehension
#NOTE-List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist ]
