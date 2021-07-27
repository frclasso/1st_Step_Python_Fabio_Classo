#!/usr/bin/env python3


"""Programa de cadastro de Pessoa Fisica

Utilizem variaveis para salvar valores/dados de uma pessoa, tais como:
identidade, cpf, nome, sobrenome, telefone, profissao etc"""

nome = 'Fabio'
sobrenome = 'Classo'
idade = 43
identidade = 1122335455
cpf = '888-333-44-55-/22'
telResidencial = '(48)30283446'
telCelular = 99998888
email = 'frclasso@gmail.com'

print("Nome:{} \nsobrenome:{} \nIdade:{} \nCPF{} \nIdentidade:{}"
      "\nTelefone Residencial:{} \nTelefone Celular:{}"
      "\nemail:{}".format(nome, sobrenome,idade, identidade,cpf,telResidencial,telCelular,email))

print()

print(f'Nome:{nome} \nSobrenome:{sobrenome} \nIdade:{idade} \nIdentidade:{identidade}'
      f'CPF:{cpf} \nTelefone Residencial:{telResidencial}'
      f'\nTelefone Celular:{telCelular}\nemail:{email}')

