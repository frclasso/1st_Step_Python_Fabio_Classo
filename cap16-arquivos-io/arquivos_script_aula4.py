#!/usr/bin/env python3

# Listando subdiretorios

import os


caminho = '/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'cap16-arquivos-io/'

# 1 com os.listdri()
# for entrada in os.listdir(caminho):
#     if os.path.isdir(os.path.join(caminho, entrada)):
#         print(entrada)

print ()
# 2 com os.scandir()
# with os.scandir(caminho) as entradas:
#     for entrada in entradas:
#         if entrada.is_dir():
#             print(entrada.name)

print()
# 3 com pahtlib.Path()

from pathlib import Path
caminho = Path('/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'cap16-arquivos-io/')

for entrada in caminho.iterdir():
    if entrada.is_dir():
        print(entrada.name)