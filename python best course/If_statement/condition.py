#python suppports the usual logical conditions from mathematics:

'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to : a <= b
Greater than: a > b
Greater than or equal to : a <= b
'''


#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement " is written by using the if keyword.
'''
The if statement evaluates a condition (an expression that results in True or False). 
If the condition is true, the code block inside the if statement is executed. 
If the condition is false, the code block is skipped.

'''
a = 33
b = 200
if b > a:
    print("b is greater than a")


#checking  if a number is positive:
number = 15
if number > 0:
    print("The number is positive")
#indentation is important.python relies on indentation to define scope in the code.


#Multiple statements in if block
#you can have multiple statement inside an if block.All statements must be indented at the level.

age = 20 
if age >= 18:
    print("you are an adult")
    print("you can vote")
    print("you have full legal rights")



#Using variables in conditions--
# Boolean  variables can be used directly in if statements without comparison operators.

is_logged_in = True
if is_logged_in:
    print("Welcome back!")

#python can evaluate many types of values as True or Flase in an if statement.
'''
Zero (0), empty strings(""), None, and empty collections are treated as False. Everything else
 is treated as True.
 This includes positive numbers(5), negative numbers(-3), and non-empty strinf(even "False"
 is treated as True because it's a non-empty string.)
'''


