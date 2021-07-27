#!/usr/bin/env python3

import os

#Diretorio atual
print(f'Diretorio atual:{os.getcwd()}')

# Cria o diretorio 'TesteDir no diretorio atual
os.mkdir("diretorio_teste")


# Mudando de diretorio
os.chdir("diretorio_teste")
print(f'Diretorio atual:{os.getcwd()}')


# voltando ao diretorio anterior
os.chdir("../")
print(f'Diretorio atual:{os.getcwd()}')

# DELETANDO DIRETORIO 'diretorio_teste'
#os.rmdir("diretorio_teste")