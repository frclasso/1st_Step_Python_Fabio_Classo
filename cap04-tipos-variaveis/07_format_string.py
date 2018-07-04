#!/usr/bin/env python3

"""Ao setarmos uma variavel podemos imprimi-la dentro da string utilizando um placeholder
 para posiciona-la
 Existem em Python tres modelos de place holders
"""

nome = 'Patricia'
idade = 28
print('Nome: %s, idade: %d anos' % (nome, idade))  # %s string e %d numeros inteiros

# segundo modo
print('Nome: {}, idade: {} anos'.format(nome,idade))

# terceiro modo
print(f'Nome: {nome}, idade: {idade} anos')