#!/usr/bin/python3

"""The index() method determines if the string str occurs in string or in a substring of string,
if the starting index beg and ending index end are given. This method is same as find(),
but raises an exception if sub is not found.
"""
str1 = "this is string example....wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2, 10))
#print(str1.index(str2, 20)) # ERRO: ValueError: substring not found
print()

print('foo bar qux grault'.index('qux'))
