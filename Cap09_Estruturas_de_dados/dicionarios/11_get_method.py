#!/usr/bin/env python3

"""obtém o conteúdo de uma chave. Não causa erro caso uma chave não exista, retorna valor;e
    Se valor não for especificados nas chaves existentes, retorna None.
    Sintaxe:dict.get(key, default=None)
"""
dict = {'Name':'Zara', 'Age':7}
print('Valor do campo: {}'.format(dict.get('Age')))
print('Valor do campo: {}'.format(dict.get('Sexo')))
print('Valor do campo: {}'.format(dict.get('Sobrenome', 'Vasquez')))  # passando valor 