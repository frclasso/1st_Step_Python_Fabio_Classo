#!/usr/bin/python3

"""The rfind() method returns the last index where the substring str is found, or -1 if no
such index exists, optionally restricting the search to string[beg:end].
"""

str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

print()
print('foo bar foo baz foo qux '.rfind('foo'))
print('foo bar foo baz foo qux '.rfind('foo', 0, 14))
print('foo bar foo baz foo qux '.rfind('foo', 10, 14))
print('foo bar foo baz foo qux '.rfind('grault')) # caso nao encontre, retorna -1

