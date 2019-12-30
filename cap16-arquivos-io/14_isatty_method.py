#!/usr/bin/env python3

fo =open('foo.txt', 'wb')
print("Nome do arquivo: ", fo.name)
ret = fo.isatty()
print("Valor retornado: ", ret)
fo.close()