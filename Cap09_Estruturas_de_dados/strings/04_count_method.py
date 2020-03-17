#!/usr/bin/python3

"""Description
The count() method returns the number of occurrences of substring sub in the range
[start, end]. Optional arguments start and end are interpreted as in slice notation.

Syntax
str.count(sub, start= 0,end=len(string))
"""
str="this is string example....wow!!!"

sub='i'

print ("str.count('i') : ", str.count(sub))

sub='exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))
print()

# s.count(<sub>[,<start>[,<end>]]) , conta a ocorrencia de uma substring em uma string alvo.
# print('foo goo moo'.count('oo'))
# print('foo goo moo'.count('oo', 0, 8))
# print()