#!/usr/bin/python3

"""Equivale a invocar lstrip() e rstrip() sucessivamente.
   Sintaxe: str.strip([chars]);
"""

str = "*****this is string example....wow!!!*****"
print(str.strip( '*' ))
print()

s = '    foo bar baz\t\t\t'
print(s.lstrip().rstrip())

print('www.realpython.com'.strip('w.com'))
