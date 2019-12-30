#!/usr/bin/env python3

aluno = {'ID': 1223,
         'Nome':'Zara',
         'Idade': 27,
         'Curso': 'Sistemas de Informação',
         'Turno':'Noturno'
         }

# print(f"ID: {aluno['ID']}")
# print(f"Nome: {aluno['Nome']}")
# print(f"Idade:{aluno['Idade']}")

# Atualizando valores existentes
# aluno['Idade'] = 28
# print(aluno)

# Inserindo novo campo
# aluno['Matrícula'] = 8990020198
#print(aluno)

'''Deletando items'''
# aluno.__delitem__('Idade')
# print(aluno)
#
# aluno.pop('Turno')
# print(aluno)
# #
# del aluno['Matrícula']
# print(aluno)
#
# # Apagando todos os dados
# aluno.clear()
# print(aluno)  # {}

# Deletando o dicionario em si
# del aluno
#print(aluno) # NameError: name 'aluno' is not defined

# criando um dicionario vazio
# meuDic = {}
# print(meuDic)
# print(type(meuDic))


#print(f'Tamanho do dicionario: {len(aluno)} items.')

# Imprimindo um dicionario com as chaves - keys()
#print(aluno.keys())

# Imprimindo um dicionario com os valores - values()
#print(aluno.values())

# Imprimindo um dicionario com todos os items
#print(aluno.items())

