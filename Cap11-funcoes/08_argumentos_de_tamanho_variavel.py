#!/usr/bin/env python3

"""Pode ser necessário processar uma função para mais argumentos do que você
especificou ao definí-la. Esses argumentos são chamados de argumentos de
comprimento variável e não são nomeados na definição da função, ao contrário dos
argumentos requeridos e padrão.
"""


def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments."
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# Chamando a funcao printinfo
printinfo(10)
printinfo(70,50,60)