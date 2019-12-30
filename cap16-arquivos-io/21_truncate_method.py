#!/usr/bin/env python3

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ",fo.name)
line = fo.readline()
print("Lendo linhas: ", line)

fo.truncate()
line = fo.readlines()
print("Lendo linhas: ", line)
fo.close()