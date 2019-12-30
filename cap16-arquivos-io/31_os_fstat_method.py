#!/usr/bin/env python3

"""Retorna diversas informacoes de sistema do arquivo associado fd"""
import os, sys
fd = os.open('foo4.txt',os.O_RDWR|os.O_CREAT)
info = os.fstat(fd)

print("File info: ",info)

# Obtendo UID do arquivo
print("UID do arquivo: {}".format(info.st_uid))

# Obtendo GID do arquivo
print("GID do arquivo: {}".format(info.st_gid))

# Fechando
os.close(fd)