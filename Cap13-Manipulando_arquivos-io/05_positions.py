#!/usr/bin/env python3

"""O método tell () informa a posição atual dentro do arquivo; em outras palavras, o
próximo read ou write ocorrerá nesse número de bytes a partir do início do arquivo.

O método seek (offset [, from]) altera a posição atual do arquivo. O argumento
de compensação indica o número de bytes a serem movidos. O argumento from
especifica a referência posição de onde os bytes devem ser movidos."""

fo = open('foo.txt','r+')
str = fo.read(28)
print("Read String is: ", str)

# Checando a posicao atual
position = fo.tell()
print("Current file position: ", position)

# Colocando o ponteiro no inicio
position = fo.seek(0, 0)
str = fo.read(28)
print("Again read String is: ",str)

# Fechando
fo.close()