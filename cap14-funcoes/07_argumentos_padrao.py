#!/usr/bin/env python3

"""Argumentos padrao ou default arguments,  é um argumento que assume um valor padrão se um valor
não for fornecido na chamada de função para esse argumento."""


def printinfo(name, age=35):
    "This prints a passed info into this function."
    print("Name: ",name)
    print("Age: ", age)
    return


# Chamando a funcao printinfo
printinfo(age=50, name="Niki")
#printinfo(name='Fabio Classo')