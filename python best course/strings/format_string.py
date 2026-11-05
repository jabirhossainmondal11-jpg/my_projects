# STRING FORMAT
# But we can combine strings and numbers by using f-strings or the format() method!

# F-STRING
'''F-String was introduced in Python 3.6,
 and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal,
 and add curly brackets {} as placeholders for variables and other operations.'''


age = 36
txt = f"My name is John, I am {age}."
print(txt)


# PLACEHOLDER AND MODIFIER---
# A placeholder can contain variables, operations,
# functions, and modifiers to format the value----

# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

# a placeholder can include a modifier to format the value.
"""A modifier is included by adding a colon : followed by a legal formatting type, like
 .2f which means fixed point number with 2 decimals:"""
price = 59
txt = f"The price is {price:.2f} dollers."
print(txt)


# A placeholder can contain python code, like math operations.

# perform a math operation in the placeholder, and return the result:
txt = f"The price is {20*50} dollers."
print(txt)
