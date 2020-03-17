#!/usr/bin/env python3

"""O metodo copy() retorna uma copia superficial do dicionario
   Sintaxe:  dicit.copy()
"""

meudic = {'Name':'Zara', 'Age': 7, 'Class': 'First'}
dict2 = meudic.copy()
print('Novo dicioario: ', dict2)


# Verificando se os dicionarios sao objetos diferentes
# print(meudic is dict2)
# print(id(meudic))
# print(id(dict2))