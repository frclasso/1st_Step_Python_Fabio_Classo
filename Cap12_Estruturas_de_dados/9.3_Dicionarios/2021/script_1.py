
# CRIANDO DICIONARIOS VAZIOS

pessoas = {}
print(type(pessoas))
print(len(pessoas))

print()
empregados = dict()
print(type(empregados))
print(len(empregados))

# CRIANDO DICIONARIOS COM VALORES

users = dict(nome='Fabio', cargo="Eng Dados")
print(type(users))
print(len(users))

cliente = {'id':1000, 'nome':'Fabio'}
print(type(cliente))
print(len(cliente))

# METODOS KEYS() VALUES() ITEMS()
print(users.keys())
print(users.values())
print(users.items())

# ADICIONANDO ELEMENTOS
fabio = {}
fabio['id'] = 2000
fabio['nome'] ='Fabio'
fabio['cargo'] = 'Developer'
fabio['natural'] ='Rio de Janeiro'
fabio['nacionaliade'] = 'Brasileiro'
fabio['email'] ='fabio@emial.com'
fabio['time'] = 'Flamengo'
print(fabio)

fabio.update({'telefone':'(48)0800900900'})
print(fabio['telefone'])

# ACESSANDO VALORES
print(fabio['nome'])

# ALTERANDO /ATUALIZANDO
# corrigindo o email
fabio['email'] = 'fabio.classo@fiesc.com.br'
print(fabio['email'])

#atualizando o cargo
fabio.update({'cargo': 'Desenvolvedor de Software'})
print(fabio['cargo'])

# REMOVENDO
fabio.pop('time')
# ou
#del fabio['time']

print(fabio)


# USANDO METODO GET() PARA ACESSAR VALORES
print(fabio.get('nome'))

print(fabio.get('bairro')) # none
#print(fabio['bairro']) # KeyError: 'bairro'


# APAGANDO TODOS OS VALORES DE UM DICIONARIO
print('-' * 40)
fabio.clear()
print(fabio)


# DELETENDO O DICIONARIO
del fabio
#print(fabio) # NameError: name 'fabio' is not defined