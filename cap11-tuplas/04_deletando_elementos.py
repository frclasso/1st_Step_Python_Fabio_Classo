#!/usr/bin/env python3

"""A remoção de elementos individuais da tupla não é possível.
"""

tup1 = ('physics', 'chemistry', 'maths')
# O codigo abaixo e invalido para tuplas
#del tup1[0]

"""Podemos criar uma nova tupla a partir de uma existente e adicionar seus elementos 
utilizando o operador de slice [:]"""
#tup2 = tup1[0:2]
#print(tup2)

# Caso a intencao seja deletar toda a tupla, utilizamos a instrucao 'del'
tup3 = tup1[-1]
#print(tup3)  # ultimo elemento, maths
del tup3
print(tup3) # NameError: name 'tup3' is not defined