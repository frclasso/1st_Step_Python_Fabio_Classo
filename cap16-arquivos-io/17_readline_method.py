#!/usr/bin/env python3

"""O método readline () lê uma linha inteira do arquivo. """

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ",fo.name)
line = fo.readline()
print("Lendo linha: ", line) # This is 1st line
line = fo.readline(5)
print("Lendo linha: ", line) # This
fo.close()