#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# TABELA VERDADE

# and or not

p = True
q = False

print('Conjunção: basta uma variável ter o valor False para o resultado ser False')
print(p and p)
print(p & True)
print(True and True)
print(True and False)
print(False and False)
print()

print('Disjunção:  basta uma variável ter o valor True para o resultado ser True')
print(p or q)
print(p | q)
print(True or False)
print(False or False)
print(True or True)
print()
print('Negação:  inverte o valor')
print(not p) # negação
print(not q) # negação

