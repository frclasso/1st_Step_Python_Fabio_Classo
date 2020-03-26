#!/usr/bin/env python3

import os, sys, stat

fd = os.open('foo4.txt', os.O_RDONLY)

# Definindo o usuario ID 1000 para esse arquivo
os.fchown(fd, 1000, -1)

# Re-definindo o ID do grupo para 50
os.fchown(fd, -1, 0)
print("Proprietario alterado com sucesso.")
os.close(fd)