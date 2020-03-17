#!/usr/bin/env python3

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ",fo.name)
str = "\nThis is 6th line"

#Escreve a string no final do arquivo
fo.seek(0, 2)
line = fo.write(str)

# Lendo o arquivo do inicio
fo.seek(0, 0)
for index in range(6):
    line = next(fo)
    print(f"Line No {index} - {line}")

# Fechando o arquivo
fo.close()