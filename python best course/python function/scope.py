def my_func():
    x = 300
    print(x)

my_func()

#The local variable can be accessed from a function within the funcion:
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()


#Global Scope
x = 300

def myfunc():
    print(x)

my_func()
print(x)


#You can create a global varible in a local scope by using global keyword.
def myfunc():
    global x
    x = 300

my_func()

print(x)

#you can also change the value of a global variable by using global keyword.
x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)    

# if you use the nonlocal keyword, the varible will belong to the outer function:
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2() 
    return x

print(myfunc1())


#python use LEGB Rule:
#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


