# Example code from python Documentation Interactive Mode¶
 
# the_world_is_flat = True
# if the_world_is_flat:
#     print("Be Careful not to fall Off!")


# Comments in Python --> Basically it is used to write like what code do or you can write anything
# but it is not part of code basically 
# it starts with # 

# like this Some example
# this is the first comment 
# spam = 1 # and this is second comment
#         #   and this is third.....

# text = "# This is not comment because it's inside quotes"




# Using Python as a Calculator
# Numbers
# print(2+2)
# print(50 - 5*6)
# print((50 - 5*6) / 4)
# print(8/5)  # division always returns a floating-point number
 
# print(17 / 3) # classic division returns a float
# print(17 // 3) # if you want the divisible return a integer number then use //
# print(17 % 3) # the % operator returns the remainder of the division
# print(5 * 3 + 2)  # floored quotient * divisor + remainder


# With Python, it is possible to use the ** operator to calculate powers 

# print(5**2)   # 5 squared
# print(2**7)   # 2 to the power of 7

# # The equal sign (=) is used to assign a value to a variable. Afterwards, no result is 
# # displayed before the next interactive prompt:
# width = 20
# height = 5 * 9
# print(width * height)



# If a variable is not “defined” (assigned a value), trying to use it will give you an error:
# n 
# print(n)


# There is full support for floating point; operators with mixed type operands 
# convert the integer operand to floating point:

# print(4 * 3.75 - 1)



# Text 
# Python can manipulate text (represented by type str, so-called “strings”) as well as numbers. 
# This includes characters “!”, words “rabbit”, names “Paris”, sentences “Got your back.”, etc. “Yay! :)”. 
# They can be enclosed in single quotes 
# ('...') or double quotes ("...") with the same result 


print('spam eggs')    # single quotes
print("Paris rabbit got your back :)! Yay!")   # double quotes
print('1975')    # digits and numerals enclosed in quotes are also strings


print('doesn\'t')    # use \' to escape the single quote...
print("doesn't") # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t, they said.')



s = "First line.\nSecond line."  # \n means newline
print(s)

print('C:\this\name')  # here \t means tab space, \n means newline
print(r'C:\this\name')  # note the r before the quote
# In this row means r in initial print statment when we use this the \t \n cannot work

# String literals
# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. 
print("""\ 
Usage: thingy [OPTIONS]
    -h                         Display this usage message
    -H hostname                Hostname to connect to
""")


# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'ium')
    
print('Py' 'thon')