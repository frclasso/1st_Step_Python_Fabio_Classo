#!/usr/bin/env python3

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ", fo.name)
line = fo.readline()
print("Lendo linha: ", line)

pos = fo.tell()
print("Posicao atual: ",pos)
fo.close()