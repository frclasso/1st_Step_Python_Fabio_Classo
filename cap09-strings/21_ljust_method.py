#!/usr/bin/python3

"""Description
The method ljust() returns the string left justified in a string of length width. Padding is
done using the specified fillchar (default is a space). The original string is returned if width
is less than len(s).

Syntax
    str.ljust(width[, fillchar])

Parameters
    -width - This is string length in total after padding.-
    -fillchar - This is filler character, default is a space.
"""


str = "this is string example....wow!!!"
print(str.ljust(50, '*'))
print()

print('foo'.ljust(10))
print('foo'.ljust(10, '-'))
