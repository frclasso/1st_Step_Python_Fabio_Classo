#!/usr/bin/env python3

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ",fo.name)
line = fo.read(16)
print('Lendo linda: ', line)
fo.close()