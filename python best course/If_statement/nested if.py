#You can have if statements inside if statements. This is called nested if statements.
x = 41
if x > 10:
    print("Avobe ten,")
    if x > 20:
        print("and aslo above 20!")
    else:
        print("but not avobe 20.")    
#In this example, the inner if statement only runs if the outer condition (x > 10) is true.

#Each level of nesting creates a deeper level of decision-making.
#  The code evaluates from the outermost condition inward.
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
         print("You need a license")
else:
    print("You are too young to drive")             


#Multiple Levels of Nesting-
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")    



 # Nested If vs Logical Operators-
'''
Sometimes nested if statements can be simplified 
using logical operators like and. The choice depends on your logic.
'''
#by nested if
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#by logical operator    
