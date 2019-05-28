#!/usr/bin/env python3

"""cria diretorios recursivamente"""

import os,sys
path = '/home/fabio/Desktop/estudo_ti/Python/1st_Step_Python_Fabio_Classo/' \
       'cap16-arquivos-io/teste/month/daily'
os.makedirs(path, 493)  # Equivalente a 0755 no Windows
print("Diretorios criados")