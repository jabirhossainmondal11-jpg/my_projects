fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping through a string
for x in "banana":
    print(x)

# Break statement
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# Continue statement--
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Range() funtion--
for x in range(6):
    print(x)

# using starting parameter
for x in range(2, 6):
    print(x)

# using the increment
for x in range(2, 30, 3):
    print(x)


#Else in for loop--
'''
The else keyword in a for loop specifies a block of code 
to be executed when the loop is finished:
'''    
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#NOTE: The else block will NOT be executed if the loop is stopped by a break statement.  
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")    


#Nested loops--

#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":

adj =["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)


#Pass statement--
'''
for loops cannot be empty, but
 if you for some reason have a for loop with no content, 
 put in the pass statement to avoid getting an error.
'''
for x in [0, 1, 2]:
    pass


