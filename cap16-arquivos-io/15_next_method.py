#!/usr/bin/env python3

fo = open('foo3.txt', 'r') # modo leitura r/read
print("Nome do arquivo: ", fo.name)
for index in range(5):
    line = next(fo)
    print(f'Line No {index} - {line}')
fo.close()