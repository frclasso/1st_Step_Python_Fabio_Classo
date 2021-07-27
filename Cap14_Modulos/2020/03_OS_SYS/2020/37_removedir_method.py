#!/usr/bin/env python3

import os, sys

os.removedirs('./teste/month/daily/hourly')
# Listando diretorios
listaDir = os.listdir(os.getcwd())
for x in listaDir:
    print(x)