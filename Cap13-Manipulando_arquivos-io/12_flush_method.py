#!/usr/bin/env python3

fo =open('foo.txt', 'wb')
print("Nome do arquivo: ", fo.name)
#Fazendo o flush
fo.flush()
# Fechando
fo.close()