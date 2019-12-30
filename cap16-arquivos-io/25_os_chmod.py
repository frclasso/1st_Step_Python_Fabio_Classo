#!/usr/bin/env python3

import os, sys, stat

# Assumindo que o arquivo foo.tx existe  vamos defini-lo para ser executado por um grupo
os.chmod('foo.txt', stat.S_IXGRP)

# Definindo a escrita do arquivo para outros usuario
os.chmod('foo.txt', stat.S_IWOTH)
print("Modo de execucao alterado com sucesso.")