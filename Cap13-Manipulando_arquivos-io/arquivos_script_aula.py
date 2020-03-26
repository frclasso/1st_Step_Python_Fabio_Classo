#!/usr/bin/env python3

import os

#print(os.getcwd())

# 1
arquivos = '/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'Cap13-Manipulando_arquivos-io/datasets_modulo1'

# for file in os.listdir(arquivos):
#     print(file)

# 2 os.scandir() foi introduzido a partir da versão 3.5 de Python - PEP 471

arqs = os.scandir('/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'Cap13-Manipulando_arquivos-io/datasets_modulo1')
#print(arqs)

# os.scandir() é um iterator, precisamos de um loop para ler os elementos

with os.scandir('/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'Cap13-Manipulando_arquivos-io/datasets_modulo1') as entradas:
    for files in entradas:
        print(files.name)