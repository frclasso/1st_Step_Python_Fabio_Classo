#!/usr/bin/env python3


"""Programa de cadastro de Pessoa Fisica

Utilizem variaveis para salvar valores/dados de uma pessoa, tais como:
identidade, cpf, nome, sobrenome, telefone, profissao etc"""

# operador de insercao de dados input

# input - sempre string
# int(input)  - variaveis do tipo inteiro
# float(input)  - variaveis do tipo float


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade:'))
identidade = input('Digite sua identidade: ')
cpf = input('Digite seu cpf: ')
telResidencial = int(input('Digite seu telefone residencial: '))
telCelular = int(input('Digite seu telefone celular: '))
email = input('Digite seu email: ')



# print("Nome:{} \nsobrenome:{} \nIdade:{} \nCPF{} \nIdentidade:{}"
#       "\nTelefone Residencial:{} \nTelefone Celular:{}"
#       "\nemail:{}".format(nome, sobrenome,idade, identidade,cpf,telResidencial,telCelular,email))
# #
# # print()
#
print(f'Nome:{nome} \nSobrenome:{sobrenome} \nIdade:{idade} \nIdentidade:{identidade}'
      f'CPF:{cpf} \nTelefone Residencial:{telResidencial}'
      f'\nTelefone Celular:{telCelular}\nemail:{email}')

