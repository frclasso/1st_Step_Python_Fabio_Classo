#!/usr/bin/env python3

import os, sys

# Definindo o proprietario 'Dono/Owner' do arquivo como 'ID 1000'

fo = open('foo4.txt', 'w')
os.chown('foo4.txt', 1000, -1)
print("Propietario atualizado com sucesso.")