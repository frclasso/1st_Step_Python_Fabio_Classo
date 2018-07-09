#!/usr/bin/env python3

import os, sys

# Primeiro vamos para o diretorio '/var/www/html'
os.chdir('/var/tmp/')

#Imprimindo diretorio atual
print("Diretorio atual: ",os.getcwd())


# Agora abriremos o diretorio '/tmp'
fd = os.open("/tmp", os.O_RDONLY)

# Usando os.fchdir() para mudar o diretorio
os.fchdir(fd)

#Imprimindo diretorio atual
print("Diretorio atual: ",os.getcwd())

# Fechando
os.close(fd)