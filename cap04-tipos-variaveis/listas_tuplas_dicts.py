#!/usr/bin/env python3

print('Listas_________')
minhaLista = ['ABCD', 2.33, 'efgh', 'bola', 'copo']
print(minhaLista[0])
print(minhaLista[1])
print(minhaLista[2])
print(minhaLista[-1])

#Adicionando um elemento no final da lista utilizamos append
minhaLista.append('Fogo')
print(minhaLista)

# Para adicionar e escolher a posição utilizamos insert
minhaLista.insert(5, 'Terra')
print(minhaLista)
print()

# deletando o ultimo elemento da lista
del minhaLista[-1]
print(minhaLista)

print("Deletando todos os elementos de uma lista")
del minhaLista[:]
print(minhaLista)

print("Deletando toda a lista")
del minhaLista
#print(minhaLista)  # NameError: name 'minhaLista' is not defined

print()

print("Tupla_________")
minhaTupla = ('ABCD', 2.33, 'efgh', 'bola', 'copo')
print(minhaTupla[0])
print(minhaTupla[1])
print(minhaTupla[-1])
#del minhaTupla[0]  # Error
#minhaTupla.append('Fogo') # Error
#minhaTupla.insert(5, 'Terra') # Error

# del minhaTupla
# print(minhaTupla) # NameError: name 'minhaTupla' is not defined
print()


print('Dicionarios_________')

dict = {'one': 1, 'two': 2, 'tree': 3}

print(dict['one'])
print(dict['two'])

dict['Four'] = 4
dict.update({'Five': 5})
print(dict)

del dict['one']
print(dict)

dict.pop('two')
print(dict)


pessoa = {"Nome": "fabio", "Identidade": "000000", "Idade": 43,"telefone": '9999-8888'}

print(pessoa['Nome'])
print(pessoa['Identidade'])

del pessoa['Identidade']
print(pessoa)

# Deleta todos os elementos do dicionario
pessoa.clear()
print(pessoa)

# Deletando todo o dicionario
del pessoa
print(pessoa) # NameError: name 'pessoa' is not defined
