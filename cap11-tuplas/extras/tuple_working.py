#!/usr/bin/env python3

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'courge')

# indices
print(t[0])
print(t[-1])

# fatiamento/slicing
print(t[1::2]) # pula de dois em dois

# invertendo a ordem
print(t[::-1])

# Tuplas nao podem ser modificadas
# t[1]='Bar'  #TypeError: 'tuple' object does not support item assignment
# print(t)

# Definindo uma tupla com um unico elemento
unicoEle = (1,)
print(type(unicoEle))
print(unicoEle)

umElemento=(1)
print(type(umElemento))