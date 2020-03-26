#!/usr/bin/env python3


'''Assignment and packing'''

t = ('foo', 'bar', 'qux', 'baz')
# print(t[0])
# print(t[-1])

'''unpacking'''
# (s1, s2, s3, s4) = t
"""Quando desempacotamos o fibonacci_exemplos de variaveis da essquerda
tem de ser o mesmo contido na tupla"""

# ou
# (s1, s2, s3, s4) = ('foo', 'bar', 'qux', 'baz')
#
# print(s1)
# print(s2)
# print(s3)
# print(s4)

t1 = 1,2,3
print(t1)

x1, x2, x3 = t1
print(x1, x2, x3)

x1, x2, x3 = 4,5,6
print(x1, x2, x3)

t2= 2,
print(t2)
