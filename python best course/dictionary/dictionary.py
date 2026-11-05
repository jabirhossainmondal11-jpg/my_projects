thisdic = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964    
}
#Dictionaries are used to store data values in key value pairs.
#A dictionary us a collection which is ordered changeable and do not allow dublicates.

#dictionary items are presented in key value pairs and can be referred to by using the key name.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])


#Dictionaries cannot have two items with the same key:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#To determine how many items a dictionary has, use the len() function:

print(len(thisdict))


#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#From Python's perspective, dictionaries are defined as objects with the data type 'dict.


#It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country ="Norway")
print(thisdict)