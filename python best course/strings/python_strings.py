#Strings
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
#You can display a string literal with the print() function:

print("Hello")
print('Hello')

#Quotes Inside Quotes
#You can use quotes inside a string, as long as they don't match
#  the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#Assign String to a Variable
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)



#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print(a)


#Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#note: in the result, the line breaks are inserted at the same position as in the code.

