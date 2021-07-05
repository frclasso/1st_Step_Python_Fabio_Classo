

# Primeira aula do EAD - 24/03/2020
# Revisão variaveis

# declarando uma variavel simples em Python
x = 100
nome = 'Fabio'
tecnologia = 'Python'
versao = 3.8
ano = 2020

# Vertificando o tipo de variável com a função built-in type
print(type(x))
print(type(nome))
print(type(versao))
print(type(ano))
print()
# Formatadores de string
#python 2.7
print("Nome: %s, Tecnologia: %s, Versão: %f , liberada no ano de: %d." % (nome,tecnologia,versao,ano))

#python3.5.6
print("Nome: {}, Tecnologia: {}, Versão: {} , liberada no ano de: {}.".format (nome,tecnologia,versao,ano))

#python3.7
print(f"Nome: {nome}, Tecnologia: {tecnologia}, Versão: {versao} , liberada no ano de: {ano}.")
print()



""" Declarando variaveis compostas
"""


"""
    Listas
"""
audi = ['Audi','Consumer goods','Automobiles','Ingolstadt',1910,'Auto manufacturer, part of Volkswagen Group']
print(type(audi))
print(audi)

#indices
print(audi[0])
print(audi[1])
print(audi[-1])

# Podemos atribuir variaveis aos indices
# name, industry, sector, headquarters, founded, notes

empresa = audi[0]
industria = audi[1]
setor = audi[2]
localizacao = audi[3]
fundada_em = audi[4]

print(f"A {empresa}, um industria {industria} do setor {setor}, localizada em {localizacao} e fundada em {fundada_em}")
print()

# Uma outra maneira de retornarmos os indices de uma lista
print(audi.index(empresa))
# ou
print(audi.index('Audi'))

print(audi.index(industria))
print(audi.index(setor))
print(audi.index(localizacao))
print(audi.index(fundada_em))
print()

# Alterando valores de uma lista
audi[4] = 1911
print(audi)
print()

# Adicionando um novo campo
audi.append('153.000')
print(audi)
print(len(audi)) # qtd de elementos
print(audi[6])
qtd_funcionarios = audi[6]
print(qtd_funcionarios)
print(audi.index(qtd_funcionarios))  #posicao
print()

# Deletando um elemento
audi.pop() # deleta o ultimo, caso na passemos parametros
audi.pop(2) # passando parametro
print(audi)
print()
del (audi[1])
print(audi)

# deletando toda a lista
# del audi
# print(audi) # NameError: name 'audi' is not defined
# print()

"""Retornando todos os métodos"""
print(dir(audi))



"""
    Tuplas
"""

adidas = ('Adidas','Consumer goods','Footwear','Herzogenaurach',1924,'Shoes, apparel and accessories')
print(type(adidas))
print(len(adidas))
print(adidas)
print(adidas[0])
print(adidas[-1])
print(adidas.index('Adidas'))
fundada_em = adidas.index(1924)
print(f'A Adidas foi fundada em: {fundada_em}')

# 9.4_Tuplas sao imutaveis
#adidas[0] = 'Nike'
#print(adidas) # erro TypeError: 'tuple' object does not support item assignment

#adidas.pop() # AttributeError: 'tuple' object has no attribute 'pop'
# adidas.append('novo item')

# Podemos forçar
# sobrescerver a varivel manualmente, não recomendado
# adicionando um novo campo
adidas_new_info = adidas + ('258.000',)
print(adidas_new_info)
print(type(adidas_new_info))
print()
# removendo
adidas_new_info_2 = adidas_new_info[:3]
print(adidas_new_info_2)
# a tupla original permanece inalterada
print(adidas)
print()

"""Retornando todos os métodos"""
print(dir(adidas))


"""
    Dicionarios
"""

# name, industry, sector, headquarters, founded, notes

montblanc = {'name':'Montblanc',
             'industry':'Consumer goods',
             'sector':'Nondurable household products',
             'headquarters':'Hamburg',
             'founded':1906,
             'notes':'Luxury goods'}

# Dicionario são estruturas q utilizam chaves pares e valor
# nao usamos indices, chamamos pela chave
print(montblanc)
print(montblanc['name'])
print(montblanc['industry'])
print(montblanc['sector'])
print(montblanc['headquarters'])
print(montblanc['founded'])
print()
# obtendo as chaves do 9.3_Dicionarios
print(montblanc.keys())
# obtendo os valores
print(montblanc.values())
#obtendo os um dicionario das chaves e valores
print(montblanc.items())
print()

#Alterando valores
montblanc['founded'] = 1907
print(montblanc)

# Adicionando um item
print(len(montblanc))
montblanc['qtd_funcionarios'] = '38.000'

# Removendo items
del montblanc['notes']
print(montblanc)

montblanc.pop('founded')
print(montblanc)

montblanc.popitem() # deleta ultimo item, não permite parametros
print(montblanc)




