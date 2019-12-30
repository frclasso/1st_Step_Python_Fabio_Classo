#!/usr/bin/env python3


# 1
caminho = '/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'cap16-arquivos-io/datasets_modulo1'

from pathlib import Path

entradas = Path('/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'cap16-arquivos-io/datasets_modulo1')

for entrada in entradas.iterdir():
    print(entrada.name)