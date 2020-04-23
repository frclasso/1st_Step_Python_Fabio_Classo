#!/usr/bin/env python3

import os, sys

# Abrindo arquivo

fd = os.open('foo.txt', os.O_RDWR | os.O_CREAT)

# Escrevendo String
line = "this is test"
# Strings precisam ser convertidas em byte objects
b=str.encode(line)
os.write(fd, b)
# Fechando o arquivo
os.close(fd)
print("Alteracoes concluidas com sucesso.")