#A function with one argument:
def my_function(frame):
    print(frame + " Refsnes")

my_function("Email")
my_function("Tobias")
my_function("Linus")

#parameters vs Arguments
def my_function(name): #name is parameter
        print("Hello", name)

my_function("Email") #"Email" is an argument


#Number of arguments
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Email", "Refsnes")
#If you try to call the function with the wrong number of arguments, you will get an error:

#Default parameter values
#You can assign default values to parameters. If the function is called without an argument, it uses the default value
def my_function(name = "friend"):
    print("Hello", name)

my_function("Email")    
my_function("Tobias")    
my_function()    
my_function("Linus")



#Keyword Arguments--
#You can send arguments with the key = value syntax.
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
#this way, with keyword arguments, the order of the argument does not matter.
my_function(name = "buddy", animal = "dog")

#positional arguments--
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
#Positional arguments must be in the correct order.


#Passing different data types
#list-
def my_function(fruits):
    for i in fruits:
        print(i)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#dict-
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


#return values
def my_function(x, y):
    return x + y

result = my_function(5, 3)
print(result)    


#returning different data types
#A functions that returns a list:
def my_function():
    return["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#A function that returns tuple:
def my_function():
    return(10, 20)

x, y = my_function()
print("x :", x)    
print("y :", y)  



#you can combine both argument types in the same function.
def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)    