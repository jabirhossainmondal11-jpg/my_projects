# sort list Alphanumerically-

# List objects have a sort() method that will sort the list alphanumerically,
#  ascending, by default.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # alphabetically

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# sort decending
# To sort decending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# sort the list decending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Cutomize sort Funtion
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list
# (the lowest number first):


def myfunc(n):
    return abs(n - 50) #abs() negative number-কে positive করে।

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
#আর একটা গুরুত্বপূর্ণ ব্যাপার: এখানে key=myfunc() ❌ লিখবে না।
#কারণ sort() নিজেই পরে প্রয়োজন অনুযায়ী myfunc() call করবে।



#Case insensitive sort
#By default the sort() method is case sensitive, resulting in all capital letters being
# sorted before lower case letter
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)




#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

