# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)


# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)


# The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)  # before the change

car["color"] = "white"
print(x)
print(car)



#The values() method will return a list of all the values in the dictionary.
x = 