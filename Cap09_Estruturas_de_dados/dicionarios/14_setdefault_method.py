#1/usr#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""O método setdefault () é semelhante a get (), mas irá definir dict [key] = default
 se a chave já  não estiver  no dicionário.
"""

dict = {'Name':'Zara', 'Age':7}
print('Valor: {}'.format(dict.setdefault('Age',None)))
print('Valor: {}'.format(dict.setdefault('Sex',None)))

print(dict)