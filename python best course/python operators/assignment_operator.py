"""
Operator          Example                         Same As
=	              x = 5	                          x = 5	
+=	              x += 3	                      x = x + 3	
-=	              x -= 3	                      x = x - 3	
*=	              x *= 3	                      x = x * 3	
/=	              x /= 3	                      x = x / 3	
%=	              x //= 3	                      x = x // 3	
**=	              x **= 3	                      x = x ** 3	
&=	              x &= 3	                      x = x & 3	
|=	              x |= 3	                      x = x | 3	
^=	              x ^= 3	                      x = x ^ 3	
>>=               x >>= 3	                      x = x >> 3	
<<=	              x <<= 3	                      x = x << 3	
:=	              print(x := 3)	                  x = 3
                                                  print(x)
"""





#Python 3.8 introduced the := operator, known
#  as the "walrus operator". **It assigns values to variables 
# as part of a larger expression:**

#The count variable is assigned in the if statement, and given the value 5:
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 10:
    print(f"List has {count} elements")





