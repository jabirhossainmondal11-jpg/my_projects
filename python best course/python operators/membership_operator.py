#Membership operators are used to test if a sequence is presented in an object:

"""

opertor     description                                     Example

in 	    Returns True if a sequence with the                    x in y
        specified value is present in the object	

not      in	Returns True if a sequence with the specified
         value is not present in the object	                   x not in y


"""


#check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)


#checks if "pineapple" is Not present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)


#Membership in Strings
#The membership operators also work with string:

text = "Hello World"

print("H" in text)
print("Hello" in text)
print("z" not in text)


