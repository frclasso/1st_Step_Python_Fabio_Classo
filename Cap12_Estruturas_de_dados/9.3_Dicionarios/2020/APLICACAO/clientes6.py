#!/usr/bin/env python3

'''Lendo dados externos'''


arquivo = input('Insira o nome do arquivo: ')

try:
    with open(arquivo, 'r') as f:
        for l in f.readlines():
            print(l,end='')
except FileNotFoundError:
    print('Arquivo nao encontrado')
print()

