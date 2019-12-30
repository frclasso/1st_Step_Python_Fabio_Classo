#!/usr/bin/env python3

"""Exemplo 1"""
# a = {5,1,2,3,4}
# print(type(a))
# print(a)
#
# # Os elementos nao se repetem
# b = {1,2,2,3,3,6,5,5,6,8,7,8,7}
# print(b)
#
# c = set()
# print(type(c))

"""Exemplo 2"""
# basket = {'apple', 'banana', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
#
# print('orange' in basket)
# print('chocolate' in basket)

"""Exemplo3"""

a = set('abracadabra') # string convertida em set
b = set('alacazam')
print(a)
print(b)

# Letras em 'a' mas nao em 'b'
print(a - b)

# Letras em 'a' ou 'b' ou em ambos, OR
print(a | b)

# Letras em 'a' e 'b', AND
print(a & b)

# Letras em 'a' ou 'b' mas nao em ambos, OU EXCLUSIVO XOR
print(a ^ b)