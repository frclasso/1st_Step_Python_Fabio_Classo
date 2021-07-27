#!/usr/bin/python3

"""The isalpha() method checks whether the string consists of alphabetic characters only"""

str = "this"  # No space & digit in this string
print(str.isalpha())
str = "this is string example....wow!!!"
print(str.isalpha())
print()

print('ABCDEFabcdef'.isalpha())
print('ABCDEFabcdef12345'.isalpha())


