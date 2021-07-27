#!/usr/bin/env python3

# Listando todos os arquivos de um diretorio

import os

# 1
caminho = '/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'Cap13_Manipulando_arquivos-io/datasets_modulo1'


# for entrada in os.listdir(caminho):
#     if os.path.isfile(os.path.join(caminho, entrada)):
#         print(entrada)

# 2
# usando os.scandir()

# with os.scandir(caminho) as entradas:
#     for entrada in entradas:
#         if entrada.is_file():
#             print(entrada.name)


# 3
# usando pathlib.Path()
from pathlib import Path


caminho = Path('/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'Cap13_Manipulando_arquivos-io/datasets_modulo1')

entradas = caminho.iterdir()
for file in entradas:
    if file.is_file():
        print(file.name)
