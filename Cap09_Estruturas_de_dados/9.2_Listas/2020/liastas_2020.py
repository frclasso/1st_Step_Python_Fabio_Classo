

# lista vazia
disciplinas = []

# operacoes básicas

# contar elementos
print(len(disciplinas))

# inserir elementos

# usando append
disciplinas.append('Matematica')
disciplinas.append('Quimica')

print(disciplinas)
print(len(disciplinas))

# Usando insert

disciplinas.insert(0, 'Fisica')
print(disciplinas)

# Usando extend
outras_disciplinas = ['Biologia', 'Farmacologia', 'Estatistica', 'Geologia', 'Economia']

# errado
#disciplinas.append(outras_disciplinas)
#print(disciplinas)

# correto
disciplinas.extend(outras_disciplinas)
print(disciplinas)

# removendo

# pop
disciplinas.pop() # remove ultimo item
print(disciplinas)

# removendo o primeiro item
disciplinas.pop(0)
print(disciplinas)

# usando del
del disciplinas[0] # remove o primeiro item
print(disciplinas)

# usando remove
disciplinas.remove('Biologia')
print(disciplinas)

# atualizando valores
disciplinas[0] = 'Chemistry'
print(disciplinas)

d2 = disciplinas.clear()
print(f'd2: {d2}')

# del d2
# print(d2)

tec_disciplinas = ['Sistemas', 'Arquitetura de Sistemas', 'Ciencias da Computacao',
                   'Calculo', 'Bancos de dados']
print(len(tec_disciplinas))
print(max(tec_disciplinas))
print(min(tec_disciplinas))

# ordenando
tec_disciplinas.sort()
print(f'Usando sort(): {tec_disciplinas}')

tec_disciplinas.sort(reverse=True)
print(tec_disciplinas)

tec2 = sorted(tec_disciplinas)
print(f'Usando sorted: {tec2}')

# reverse
tec_disciplinas.reverse()
print(f'Usando reverse: {tec_disciplinas}')


# contando
print(tec_disciplinas.count('Sistemas'))

tec_disciplinas.append('Sistemas')
print(tec_disciplinas)
print(tec_disciplinas.count('Sistemas'))


# somando valores
valores = [200, 20, 50]
print(f'Total: {sum(valores)}')

# index
print(tec_disciplinas.index('Calculo'))

# membership
print('Sistemas' in tec_disciplinas)
print('Python' not in tec_disciplinas)
print()

# classe list
texto = 'The Python Program Language'
texto_para_lista = list(texto)
print(texto_para_lista)

texto_para_lista_usando_split = texto.split()
print(texto_para_lista_usando_split)

arte_disciplinas = ('Pintura', 'Musica', 'Literatura')
print(type(arte_disciplinas))

arte_disciplinas_lista = list(arte_disciplinas)
print(arte_disciplinas_lista)
print()

#loop

todas_as_disciplinas = []
for d1 in tec_disciplinas:
    print(d1)
    todas_as_disciplinas.append(d1)


for d2 in arte_disciplinas:
    #print(d2)
    todas_as_disciplinas.append(d2)

for d3 in outras_disciplinas:
    #print(d3)
    todas_as_disciplinas.append(d3)


print(sorted(todas_as_disciplinas))
print()

l1 = ['Audi', 'BMW', 'VW']
l2 = ['Ford', 'Jeep', 'GMC']
companies = []
for k, v in zip(l1, l2):
    companies.append(k)
    companies.append(v)
print(sorted(companies))


l3 = l2.copy()
print(l3)

l4 = l3[:]
print(l4)