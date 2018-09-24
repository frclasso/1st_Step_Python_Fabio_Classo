#!/usr/bin/env python3
# -*- coding:utf-8 -*-

x = 'Hello world'
y = {1: 'a', 2: 'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

"""Aqui, 'H' está em 'x' mas 'hello' não está presente em 'x' (lembre-se, o
 Python é sensível a maiúsculas e minúsculas). 
 Similarmente, 1 é chave e 'a' é  o valor no dicionário y. 
 Portanto, 'a' em y retorna False. So a chave é avaliada"""