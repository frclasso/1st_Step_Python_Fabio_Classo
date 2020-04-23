#!/usr/bin/env python3

import os, sys

os.remove('foo4.txt')
#Listando arquivos no diretorio
#print("Arquivos contidos neste diretorio: {}".format(os.listdir(os.getcwd())))
listaDir = os.listdir(os.getcwd())
for x in listaDir:
    print(x)