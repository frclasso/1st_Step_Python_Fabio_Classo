

# definindo uma funcao
# def NOME(args):
    # pass


# def calcula_imc():
#     pass

"""Chamando a funcao"""
# calcula_imc()


""" Saida ou retorno de uam funcao"""

# def calcula_imc():
#     peso = 84.0
#     altura = 1.74
#     imc = peso / altura ** 2
#     print(f'IMC: {imc}')

# calcula_imc()

# def calcula_imc():
#     peso = 84.0
#     altura = 1.74
#     imc = peso / altura ** 2
#     return imc
#
#
# print(calcula_imc())

"""Documentando funcoes"""
# DOCSTRINGS
# def calcula_imc():
#     """Esta função realiza o calculo do imc de um individuo"""
#     peso = 84.0
#     altura = 1.74
#     imc = peso / altura ** 2
#     return imc
#
#
# print(calcula_imc())
# print(calcula_imc.__doc__)

"""Escopo de variaveis"""

# peso = 80 # escopo global
#
#
# def calcula_imc():
#     #global peso
#     peso = 84.0
#     altura = 1.74
#     imc = peso / altura ** 2
#     print(f'Valor da variavel peso dentro da função: {peso}') # escopo local
#     return imc
#
# calcula_imc()
#
# print(f'Valor da variavel peso FORA da função: {peso}')
#
# print()

""" Argumentos de uma função"""
# Args requeridos
# peso = 80 # escopo global
#
#
# def calcula_imc(peso, altura):
#     imc = peso / altura ** 2
#     return imc
#
#
# print(calcula_imc(84, 1.74))


# Args padrao


# def calcula_imc(peso, altura=1.80): #obs, o argumento padrao deve ser declarado depois do argumento requerido
#     imc = peso / altura ** 2
#     return imc
#
#
# print(calcula_imc(84))
# print(calcula_imc(84, 1.50))
# print(calcula_imc(peso=90, altura=1.90))

# Argumentos de tamanho variavel - *args
# def calcula_imc(args):
#     print(f'Argumentos passados: {args}')
#
#
# calcula_imc(84, 1.74)
#
#
# def calcula_imc(*args):
#     peso = args[0]
#     altura = args[1]
#     imc = peso /altura ** 2
#     return imc
#
#
# print(f'IMC usando *args: {calcula_imc(90, 1.95):.2f}')


# Arggumento de palavras chaves - **kwargs
def calcula_imc(**kwargs):
    print(f'Argumentos passados: {kwargs}')

calcula_imc(peso=87, altura=1.87)


def calcula_imc(**kwargs):
    peso = kwargs['peso']
    altura = kwargs['altura']
    imc = peso /altura ** 2
    return imc


print(f'Utilizando **kwargs: {calcula_imc(peso=80, altura=1.8):.2f}')


""" Ordem dos argumentos
     1) requiridos, 
     2) padrao
     3) *args
     4) **kwargs
"""


def calcula_imc(nome, idade=40, *args, **kwargs):
    print(nome)
    print(idade)
    print(args)
    print(kwargs)


calcula_imc('Fabio', 44, 84, altura=1.74)