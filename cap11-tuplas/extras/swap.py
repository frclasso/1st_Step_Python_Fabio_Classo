#!/usr/bin/env python3

# Trocando os valores de duas variaveis , SWAP

a = 'foo'
b = 'bar'
#print(a,b)

# Primeira maneira, utilizando um variavel temporaria
# temp = a
# a = b
# b = temp
# print('Valor de a: "{}" e valor de b: "{}".'.format(a, b))

# De maneira mais Pythonica
a, b = b, a
print('Valor de a: "{}" e valor de b: "{}".'.format(a, b))

