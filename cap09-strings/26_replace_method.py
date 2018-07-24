#!/usr/bin/python3

"""The replace() method returns a copy of the string in which the occurrences of old have
been replaced with new, optionally restricting the number of replacements to max.

Syntax
str.replace(old, new[, max])
"""
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 1))
print (str.replace("is", "was", 2))
print (str.replace("is", "was", 3))
print (str.replace("is", "was", 4))
print()

print('foo bar foo baz foo qux'.replace('foo', 'grault'))
print('foo bar foo baz foo qux'.replace('foo', 'grault', 2))