#!/usr/bin/env python3

"""O método readlines () lê até EOF usando o método readline( ) e retorna uma lista
contendo as linhas. """

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ",fo.name)
line = fo.readlines()
print("Lendo linhas: ", line)
line = fo.readlines(2)
print("Lendo linhas: ", line)
