
#Operator precedence describes the order in which operations are performed.

"""
Parentheses has the highest precedence,
 meaning that expressions inside parentheses must be evaluated first
"""
print((6 +3) - (6 - 3))



#Multiplication * has higher precedence than addition +,
#  and therefore multiplications are evaluated before additions:
print(100 + 5 * 3)




#Precedence Order
#The precedence order is described in the table below, 
# starting with the highest precedence at the top:

"""
operators                        description

()	                               Parentheses	

**	                               Exponentiation	

+x  -x  ~x	                       Unary plus, unary minus, and bitwise NOT

*  /  //  %	                       Multiplication, division, floor division, 
	                                floor division, and modulus

+  -	                           Addition and subtraction	

<<  >>	                           Bitwise left and right shifts

&	                               Bitwise AND	

^	                               Bitwise XOR	

|	                               Bitwise OR	

==  !=  >  >=  <  <=  is  	       Comparisons, identity, and membership operators	
is not  in  not in

not	                               Logical NOT	
and	                               AND	
or	                               OR	

"""

