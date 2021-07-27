#!/usr/bin/env python3

"""A instrução return [expressão] sai de uma função, passando opcionalmente uma
expressão para o chamador. Uma declaração de retorno sem argumentos é a mesma
que retornar None .
"""


def sum(arg1, arg2):
    # Adiciona os paramentros e os retorna
    total = arg1 + arg2
    print("Inside the function: ",total)
    return total


# Chamando a funcao
sum(10, 20)
