#!/usr/bin/env python3

"""Todos os parâmetros (argumentos) em Python são passados por referência. Isso
significa que se você mudar o valor ao qual um parâmetro se refere dentro de uma
função, a mudança também reflete de volta a função de chamada.
"""


def changeme(mylist):
    "This changes  a passed list into this function."
    print("Values inside the function before change: ", mylist)
    mylist[2]=50
    print("Values inside the function after change: ", mylist)
    return


# Chamando a funcao
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

"""Aqui, estamos mantendo a referência do objeto passado e acrescentando valores no mesmo
objeto."""
