def my_function():
    print("Hello from a function")


my_function()

#you can call the same function multiple times:

temp1 = 77
celsius1 = (temp1 - 32) * 5/9 
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5/9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5/9
print(celsius3)




#with function - reusable code:
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheit_to_celsius(77))    
print(fahrenheit_to_celsius(95))    
print(fahrenheit_to_celsius(50))    


#A funtion that returns a value:
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

#using the return value directly:
def get_greeting():
    return "Hello from a funtion"

print(get_greeting())

#function defination cannot be empty.If you need to create a function placeholder without any code,use pass statement.
def my_function():
    pass