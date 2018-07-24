#!/usr/bin/python3


"""The lstrip() method returns a copy of the string in which all chars have been stripped
from the beginning of the string (default whitespace characters).
"""

str = " this is string example....wow!!!"
print (str.lstrip())
str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))
print()

print('    foo bar baz  '.lstrip())
print('\t\nfoo\t\nbar\t\nbaz'.lstrip())
print('http://www.realpython.org'.lstrip('/:thp'))

