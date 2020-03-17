#!/usr/bin/env python3

"""Keyword arguments ou argumentos de palavra chave estão relacionados às chamadas de função.
Quando você usa argumentos de palavras-chave em uma chamada de função, o chamador identifica
os argumentos pelo nome do parâmetro."""


def printme(str):
    'This prints a string into this function.'
    print(str)
    return


# Chamando a funcao
printme(str="My new string!")