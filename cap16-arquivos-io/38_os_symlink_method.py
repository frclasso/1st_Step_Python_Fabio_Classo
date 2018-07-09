#!/usr/bin/env python3

import os

"""Cria um link simnbolico para um arquivo ou diretorio."""

src = "/home/fabio/Desktop/estudo_ti/Python/apostila_python_modulo_1/" \
       "cap16-arquivos-io/foo2.txt"
dst = '/home/fabio/Desktop/foo'

os.symlink(src, dst)
print("Symlink criado com sucesso.")
