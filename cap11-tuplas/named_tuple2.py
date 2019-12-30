#!/usr/bin/env python3

from collections import namedtuple

# utilizando um dicionario
Person = namedtuple('Person', {'name':'', 'age':'', 'height':'', 'nationality':''})

yinka = Person(name='Ynka', age=20, height=5.2, nationality='Nigerian')

print(yinka)

print(yinka.name)
print(yinka.age)
print(yinka.nationality)

print()
# tambem funciona como uma tupla normal
print(yinka[0])
print(yinka[1])
print(yinka[3])

# é imutável assim como as tuplas normas
# yinka.age = 40
# print(yinka.age) #AttributeError: can't set attribute

# Atributos

#  _fields , retorna os nomes dos itens dos elementos da instancia namedtuple
#  _replace, retorna uma nona instancia  de uma namedtuple, a instancia original continua inalterada.
#  _asdict, retorna um dicionario ordenado  a partir de uma instancia namedtuple na order  em que foram inseridos
# _make, cria uma nova instancia namedtuple a partir de dados iteráveis disponíveis

print(yinka._fields)  # semelhante as chaves dos dicionarios
print()
paul = yinka._replace(name='Paul', age=40, height=5.2, nationality='Candian')
print(paul)
print(yinka)
print()
print(yinka._asdict)
print(yinka._asdict())
print()
print(paul._asdict())
print()
Person = namedtuple('Person', 'name, age, height, nationality')
jane_doe_data = ['Jane', 20, 5.9, 'American']
jane = Person._make(jane_doe_data)
print(jane)

# a partir de um dicionario
john_doe_data = {'name':'Joe', 'age':20, 'height':6.2, 'nationality':'India'}
john = Person._make(john_doe_data.values())
print(john) 