#!/usr/bin/env python3

"""O método list () pega tipos de sequência e os converte em listas.
Isso é usado para converter uma dada tupla em lista."""

aTuple = (123, 'C++', 'Java', 'Python')

list1 = list(aTuple)  # aqui convertemos uma tupla em uma lista de elementos
print('Elementos da lista: ', list1)
print(type(list1)) # para verificar se realmente eh uma lista

str="Hello World"
list2=list(str) # Aqui convertemos uma string em uma lista
print('Elementos da lista: ',list2)
print(type(list2))