#!/usr/bin/env python3

import os, sys, stat

fd = os.open('foo.txt', os.O_RDONLY)

# Definindo o arquivo para ser executado pelo grupo
os.fchmod(fd, stat.S_IXGRP)

# Re-definindo o arquivo para ser escrito por outros
os.fchmod(fd, stat.S_IWOTH)

print("Alteracoes realizadas com sucesso.")

os.close(fd)