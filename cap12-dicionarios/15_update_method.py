#!/usr/bin/env python3

# -*-coding:utf-8 -*-

"""atualiza o dicionário com elementos de outro dicionário e possibilita
a alteração (atualização) de valores"""

dict = {'Name':'Zara', 'Age':7}
dict2 = {'Sex':'Female'}
dict.update(dict2)
print('Dicionario atualizado: {}'.format(dict))