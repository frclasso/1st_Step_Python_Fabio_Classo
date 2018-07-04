#!/usr/bin/env python3
# -*-coding:utf-8 -*-

""" Mais de uma entrada por chave não é permitida. Isso significa que nenhuma chave
duplicada é permitida.Quando chaves duplicadas são encontradas durante a atribuição,
 a última atribuição ganha.
"""

meudic = {'Name':'Zara', 'Age': 7, 'Class': 'First', 'Name': 'Mani'}
print(meudic['Name'])  # Mani
