#!/usr/bin/env python3

fo = open('foo2.txt', 'r+')
print("Nome do arquivo: ",fo.name)
seq = ["\nThis is 7th line\nThis is 8th line"]  # Sequencia de strings

#Escreve a sequencia no final do arquivo
fo.seek(0, 2)
line = fo.writelines(seq)

# Lendo o arquivo do inicio
fo.seek(0, 0)
for index in range(7): # Aumentei de 6 para 7
    line = next(fo)
    print(f"Line No {index} - {line}")

# Fechando o arquivo
fo.close()