#!/usr/bin/python3

"""The split() method returns a list of all the words in the string, using str as the separator 
(splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
"""

str = "this is string example....wow!!!"
print(str.split( ))
print (str.split('i',1))
print(str.split('w'))

print()
print('www.realpython.com'.split('.', maxsplit=1))
print('www.realpython.com'.rsplit('.', maxsplit=1))
