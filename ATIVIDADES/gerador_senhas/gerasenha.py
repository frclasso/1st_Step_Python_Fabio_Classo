#!/usr/bin/env python3


"""Desenvolver um gerador de senha"""

# random
import random
# minusculos
minusculos = 'abcdefghijklmnopqrstuwxyz'
# maiusculos
maiusculos = minusculos.upper()  # upper, strings
# simbolos
simbolos = '!@#$%^&*()_+-=?/><:;'
# numeros
numeros = range(10) # valores 0 - 9

# print(maiusculos)
# print(list(numeros))


# choice, sample
#print(random.sample(minusculos, 5))
senha = []
for i in range(5):
    s = random.choice(minusculos)
    senha.append(s) # adiciona

for i in range(5):
    s = random.choice(maiusculos)
    senha.append(s)

for i in range(5):
    s =random.choice(simbolos)
    senha.append(s)

for i in range(5):
    s = random.choice(str(numeros))
    senha.append(s)

#rint(senha)
s2 = ''.join(senha)
#print(s2)
#
novaSenha = []
for i in s2:
    for x in i:
        s = random.choice(s2)
    novaSenha.append(s)
senha= ''.join(novaSenha)
print(senha)


# Concatenar e condensar
senha2 = minusculos + maiusculos + simbolos
