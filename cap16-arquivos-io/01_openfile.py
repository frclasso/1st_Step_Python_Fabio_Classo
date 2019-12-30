#!/usr/bin/env python3

# Abrindo arquivo
fo = open('foo.txt', 'wb')  # o modo de abertura 'w/write' cria o arquivo, caso nao exista.
print("Nome do arquivo: ", fo.name) # Retorna o nome do arquivo
print("Verificando se esta fechado: ",fo.closed) # Retorna True se o arquivo esta fechado
print("Verificando o mode de abertura: ",fo.mode) # Retorno o modo de abertura
