#using *args to accept any number of arguments:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Email", "Tobias", "Linus") 

#The *args parameter allows a function to accept any number of positonal argments.
def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function("Email", "Tobias", "Linus")    


#using *args with Regular Arguments
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Email", "Tobias", "Linus")



#A function that calculates the sum of any number of values:
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


#using *kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")    

#accessing values from **Kwargs:
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)


my_function(name = "tobias", age = 30, city = "bergen")


def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)



