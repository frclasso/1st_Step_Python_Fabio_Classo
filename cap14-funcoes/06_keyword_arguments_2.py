#!/usr/bin/env python3

"""Um exemplo mais claro, observe que a ordem dos paramentros nao eh obedecida"""


def printinfo(name, age):
    "This prints a passed info into this function."
    print("Name: ",name)
    print("Age: ",age)
    return


# Chamando a funcao printinfo
printinfo(age=43, name="Fabio")