#!/usr/bin/python3


"""The islower() method checks whether all the case-based characters (letters) of the string
are lowercase.
"""

str = "THIS is string example....wow!!!"
print(str.islower())

str = "this is string example....wow!!!"
print(str.islower())
print()

print('abcdef'.islower())
print('abcde$f'.islower())
print('Abcde$f'.islower())