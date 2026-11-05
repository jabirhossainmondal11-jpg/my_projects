# If you have only one statement to execute, you can put it on the same line as the if statement.
a = 5
b = 2
if a > b:
    print("a is greater than b")


# Short Hand If ... Else
a = 2
b = 300
print("A") if a > b else print("B")
# This is called a conditional expression (sometimes known as a "ternary operator").


# You can also use a on-line if/else to choose a value and assign it to a variable.
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# multiple conditions on one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print(
    "B")  # important block code


# setting a default value:
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
