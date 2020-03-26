#!/usr/bin/env python3

import os

"""Cria um link simnbolico para um arquivo ou diretorio."""

src = "/home/fabio/Desktop/estudo_ti/Python/1st_Step_Python_Fabio_Classo/" \
       "Cap13-Manipulando_arquivos-io/foo2.txt"
dst = '/home/fabio/Desktop/foo'

os.symlink(src, dst)
print("Symlink criado com sucesso.")
