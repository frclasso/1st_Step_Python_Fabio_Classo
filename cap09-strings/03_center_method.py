#!/usr/bin/python3

"""The method center() returns centered in a string of length width. Padding is done using
the specified fillchar. Default filler is a space.

Syntax
str.center(width[, fillchar])

Parameters
 -width - This is the total width of the string.
 -fillchar - This is the filler character.
"""

str = "this is string example....wow!!!"
print ("str.center(40, 'a') : ", str.center(40, 'a'))
print()

print('foo'.center(10))
print('bar'.center(10, '-'))