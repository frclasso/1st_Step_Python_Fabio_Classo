

pessoas = {
    1:{'nome':'John', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    2:{'nome':'Jane', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    3:{'nome':'Mary', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    4:{'nome':'Peter', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    5:{'nome':'Harry', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    6:{'nome':'Susan', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    7:{'nome':'Michael', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    8:{'nome':'Jimmy', 'sobrenome':'', 'idade':20, 'sex':'M'},
}

for k, v in pessoas.items():
    #print(k, v)
    for chave, valor in v.items():
        pass
        #print(v)
    v['tel'] = 'None'
    print(v)
print()


### ATIVIDADE

# Adicionar sobrenomes
lista_de_sobrenomes = ['Lennon', 'Fonda','Jane', 'Parker', 'Potter', 'Sarandon', 'Jackson', 'Hendrix']
#print(pessoas[1]['sobrenome'])
pessoas[1]['sobrenome'] = lista_de_sobrenomes[0]
print(pessoas[1])
print()

count = 0
for k, v in pessoas.items():
    #rint(v['sobrenome'])
    v['sobrenome'] = lista_de_sobrenomes[count]
    count += 1
    print(v)

print()

# empresas
lista_de_empresas = ['Audi', 'VW', 'Vivo', 'Nextel', 'JetBrains', 'Apple', 'Canonical', 'DropBox']

# email
nome = pessoas[1]['nome']
sobrenome = pessoas[1]['sobrenome']
empresa = lista_de_empresas[0]
email = nome.lower() + '.' + sobrenome.lower() + '@' +empresa.lower() + '.com.br'
print(email)


# criar lista de telefones


# passar valores padrao (setdefault(), fromkeys(), get())

#remover colunar 'sex'


