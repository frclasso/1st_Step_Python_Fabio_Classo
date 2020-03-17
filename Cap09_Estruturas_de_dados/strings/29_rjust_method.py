#!/usr/bin/python3

"""The rjust() method returns the string right justified in a string of length width. Padding 
is done using the specified fillchar (default is a space). The original string is returned if 
width is less than len(s).
"""

str = "this is string example....wow!!!"
print (str.rjust(50, '*'))
print()

print('foo'.rjust(10))
print('foo'.rjust(10, '-'))