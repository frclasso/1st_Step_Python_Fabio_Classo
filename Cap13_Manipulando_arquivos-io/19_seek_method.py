#!/usr/bin/env python3

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ", fo.name)
line=fo.readlines()
print("Lendo linhas: ",line)

# Posicionando o cursor no inicio do arquivo
fo.seek(0,0)
line = fo.readline()
print("Lendo linha: ", line)
fo.close()