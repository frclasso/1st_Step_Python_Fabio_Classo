#!/usr/bin/env python3

minhatupla = ('abcd', 786, 2.23, 'john', 70.2)

tinytupla = (123, 'john')

print(minhatupla)
print(minhatupla[0])
print(minhatupla[1:3])
print(minhatupla[2:])
print(tinytupla * 2)
print(minhatupla+tinytupla)

# o codigo abaixo eh invalido para tuplas, mas funciona para listas
#minhatupla[2] = 1000 # TypeError: 'tuple' object does not support item assignment
#tinytupla[0] = 1000  # TypeError: 'tuple' object does not support item assignment