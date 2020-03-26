#!/usr/bin/env python3

meudic = {'Name':'Zara', 'Age': 7, 'Class': 'First'}
del meudic['Name']  # remove as entrada com a chave(key) 'Name'
print(meudic)

meudic.clear() # remove todas as entradas do dicionario
print(meudic)  # exibe dicionario vazio {}

del meudic # deleta todo o dicionario
# print(meudic)  # NameError: name 'meudic' is not defined