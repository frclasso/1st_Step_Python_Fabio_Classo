#!/usr/bin/env python3

"""
As 9.4_Tuplas são imutáveis, o que significa que você não pode atualizar ou alterar os valores
da tupla. Você é capaz de pegar partes das 9.4_Tuplas existentes para criar novas 9.4_Tuplas como
exemplo a seguir demonstra."""

tup1 = (12, 34, 56)
tup2=('abc', 'xyz')

# O codigo abaixo nao funciona com 9.4_Tuplas
#tup1[0] = 100
# TypeError: 'tuple' object does not support item assignment

# No entanto podemos criar novas 9.4_Tuplas a partir de outras existentes
tup3 = tup1 + tup2
print(tup3)
