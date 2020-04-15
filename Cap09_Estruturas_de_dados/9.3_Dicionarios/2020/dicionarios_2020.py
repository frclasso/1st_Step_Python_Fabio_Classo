#!/usr/bin/env python3

#dicionario vazio
al = {}

aluno = {'ID': 1223,
         'Nome':'Fabio',
         'Sobrenome':'Classo',
         'Idade': 45,
         'Curso': 'Sistemas de Informação',
         'Turno':'Noturno'
         }

print(f"ID: {aluno['ID']}")
print(f"Nome: {aluno['Nome']}")
print(f"Idade:{aluno['Idade']}")

# Atualizando valores existentes
aluno['Idade'] = 28
print(aluno)

# Inserindo novo campo
aluno['Matrícula'] = 8990020198
print(aluno)

aluno.update({'Curso':'Cienccias da Coputacao'})
print(aluno)


aluno.update({'Unidade Educacional': 'Florianopolis Centro'})
print(aluno)

'''Deletando items'''
aluno.__delitem__('Idade')
print(aluno)

aluno.pop('Turno')
print(aluno)
#
del aluno['Matrícula']
print(aluno)

"""Apagando todos os dados"""
aluno.clear()
print(f'clear:',aluno)  # {}

# Deletando o dicionario em si
# del aluno
#print(aluno) # NameError: name 'aluno' is not defined

print(f'Tamanho do dicionario: {len(aluno)} items.')

# Imprimindo um dicionario com as chaves - keys()
print(aluno.keys())

# Imprimindo um dicionario com os valores - values()
print(aluno.values())

# Imprimindo um dicionario com todos os items
print(aluno.items())

# A funcao dict()
aluno2 = dict(nome='Giovanna', idade='7', turno='matutino', unidade_educacional='Santo Antonio de Lisboa')
print(aluno2)
print()

# loops
questions = ['name', 'questions', 'favourite color']
answer = ['Lancelot', 'the holy grail', 'blue']


for q, a in zip(questions, answer):
    print("What's yours {}? It's {}".format(q, a))
print()

# -- criando um dicionarios a partir de outra estrutura de dados
respostas = {}
for q, a in zip(questions, answer):
    respostas[q] = a
print(respostas)

# Chaves repetidas

aluno3 = {'nome':'Erick', 'idade':11, 'turno':'vespertino', 'unidade_educacional':'centro', 'nome':'Perdro'}
print(aluno3)

# conversao (tupla para dict) -erro
#aluno4 = dict(nome='Erick', idade=11, turno='verpertino', unidade_educacional='Santo Antoio de Lisboa', nome='Pedro')
# print(aluno4)

# copy()
aluno5 = aluno3.copy()
print(aluno5)

aluno5['nome']='Vinicius'
print(aluno5)


# fromkeys()

novo_aluno = ['nome', 'idade', 'turno', 'unidade_educaional']
dict_aluno = dict.fromkeys(novo_aluno)
print('Novo aluno: {}'.format(str(dict_aluno)))  # nenhum valor foi definido para 'value'


# procurando chaves inexistentes
#print(aluno5['phone'])

print(aluno5.get('phone','Key Not Found!'))


# Definindo valores padrao
aluno6 = {'nome':'Fernanda'}
aluno6.setdefault('idade', 33)
aluno6.setdefault('turno', 'noturno')
aluno6.setdefault('unidade_educacional', 'Centro')

print(aluno6)


