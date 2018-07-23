#!/usr/bin/python3

"""Description
It returns True if the string ends with the specified suffix, otherwise return False optionally
restricting the matching with the given indices start and end.
Syntax
str.endswith(suffix[, start[, end]])"""

Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))
print()

#s.endswith(<sufix>[,<start>[,<end>]]), determina se a string termina
                   # com a substring fornecida
print('foobar'.endswith('bar'))
print('foobar'.endswith('baz'))
print('foobar'.endswith('oob', 0, 4))
print('foobar'.endswith('oob', 2, 4))


