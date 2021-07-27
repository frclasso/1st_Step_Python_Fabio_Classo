#!/usr/bin/env python3

# multiplos diretorios e arquivos



import os

for dirpath, dirnames, files in os.walk(''):
    print('-' * 70)
    print(f'Diretorios e arquivos encontrados: {dirpath}')
    for file_name in files:
        print(file_name)


