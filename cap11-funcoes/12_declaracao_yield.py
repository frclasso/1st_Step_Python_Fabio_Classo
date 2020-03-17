#!/usr/bin/env python3

"""Sempre que usamos a palavra reservada yield , estamos criando uma funcao
geradora. A funcao geradora gera um valor toda vez em que e “chamada”, e aqui,
usamos aspas, pois não e uma chamada comum. Por padrão, as funções geradoras
podem ser iteradas no comando for"""


def get_generator():
    for i in range(10):
        yield i  # Substitua yeild por return Erro: TypeError: 'int' object is not iterable


for number in get_generator():
    print(number)


"""Para obtermos o mesmo resulta utilizando a declaracao return, precisamos  salvar o numeros
gerados em uma lista"""

print()


# def get_list():
#     numbers = []  # Lista onde sera salva os numeros
#     for i in range(10):
#         numbers.append(i)
#     return numbers
#
#
# for number in get_list():
#     print(number)