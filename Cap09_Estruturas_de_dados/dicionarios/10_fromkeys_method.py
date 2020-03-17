#!/usr/bin/env python3

"""retorna um novo dicionário cujas chaves são os elementos de uma sequencia e cujos
valores são todos iguais ao argumento valor.
   Sintaxe: dict.fromkeys(seq[, value])
"""

seq = ['name', 'age', 'sex']
dict = dict.fromkeys(seq)
print('Novo dicionario: {}'.format(str(dict)))  # nenhum valor foi definido para 'value'

# definido o valor 10 para o argumento value
# dict = dict.fromkeys(seq, 10)
# print('Novo dicionario: {}'.format(str(dict)))


