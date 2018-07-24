#!/usr/bin/python3

"""Description
The find() method determines if the string str occurs in string, or in a substring of string
if the starting index beg and ending index end are given.

Syntax
str.find(str, beg=0 end=len(string))
"""

str1 = "this is string example....wow!!!"
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))

print()
# s.find(<sub>[,<start>[,<end>]]), busca na string alvo a substring fornecida
# print('foo bar 123 quX'.find('foo')) # retorna a posicao quando encontra a substring
# print('foo bar 123 quX'.find('bar'))
# print('foo bar 123 quX'.find('grault')) # -1, False, quando nao encontra
# print()
