

# Variaveis
# simples
x = 1000
print(x)
nome = 'Fabio'
linguagem = 'Python'
versao = 3.8
ano = 2020

# Built ins (funcoes internas)
print(type(x))
print(type(nome))
print(type(linguagem))
print(type(versao))
print(type(ano))

#foramatadores
#python2.7
print('Nome:  %s, Tecnologia:  %s, Versão: %f, ano: %d' % (nome, linguagem, versao, ano))

# python3.5.6
print('Nome:  {}, Tecnologia:  {}, Versão: {}, ano: {}'.format(nome, linguagem, versao, ano))

# 3.7
print(f'Nome:  {nome}, Tecnologia:  {linguagem}, Versão: {versao}, ano: {ano}')
print()

# Compostas

# listas
audi = ['Audi',
        'Consumer goods',
        'Automobiles',
        'Ingolstadt',
        1910,
        'Auto manufacturer, part of Volkswagen Group']

print(type(audi))
# print(dir(audi))
# qtd elementos
print(len(audi))

# indices
# print(audi[0])
# print(audi[1])
# print(audi[2])
# print(audi[3])
empresa = audi[0]
industria = audi[1]
setor = audi[2]
print(empresa)
print(industria)
print(setor)

#  alterar valores
audi[4] = 1911  # reatribuicao
print(audi)

# inserir um campo
audi.append('150.000')  # insere no final
print(audi)
qtd_funcionarios = audi[6]
print(qtd_funcionarios)

# remover
audi.pop() # remove o ultimo
print(audi)
audi.pop() # remove na posicao
print(audi)
audi.pop() # remove na posicao
print(audi)
audi.pop() # remove na posicao
print(audi)
# del audi[0]
# print(audi)
# print()
#
#tuplas
adidas = ('Adidas',
          'Consumer goods',
          'Footwear',
          'Herzogenaurach',
          1924,
          'Shoes, apparel and accessories'
          )

print(type(adidas))
print(adidas)
print(adidas[0])
print(adidas[1])
print(adidas[2])
print(adidas[:3])

# imutaveis
#adidas[0] = 'Nike'
#adidas.pop()
#adidas.append()
adidas_new = adidas + ('230.000',)
print(type(adidas_new))
print(adidas_new)
adidas_new_2 = adidas[:2]
print(adidas_new_2)
print(adidas)
print(dir(adidas))
print(len(adidas))

#
#
# #dicionarios
# t = (1,2,3,4)
# l = [1,2,3,4]

#d = {k:v, k:v, k:v}
# name, industry, sector, headquarters, founded, notes

montblanc = {'name':'Montblanc',
             'industry':'Consumer goods',
             'sector':'Nondurable household products',
             'headquartes':'Hamburg',
             'founded':1906,
             'notes':'Luxury goods'
             }
print(type(montblanc))
print(montblanc['name'])
print(montblanc['industry'])
print(montblanc['sector'])
print(montblanc['headquartes'])

# alterando valore
montblanc['founded'] = 1907
print(montblanc)

# adicionar
montblanc['qtd_funcioarios'] = '1.000.000'
print(montblanc)

# deletar campo
del montblanc['qtd_funcioarios']
print(montblanc)

montblanc.pop('headquartes')
print(montblanc)

montblanc.popitem() # NAO ACEITA PARAMENTROS, de tras pra frente
print(montblanc)

# metdos dicionarios
print(montblanc.keys())
print(montblanc.values())
print(montblanc.items())
