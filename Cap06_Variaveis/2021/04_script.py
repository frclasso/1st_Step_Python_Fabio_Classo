l = [1,2,3,4]

t = (1,2,3,4)

# dicionarios

mydict = {'chave':'valor'}

vazio = {}
print(type(vazio))
print(vazio)

print(mydict)

funcionario = {
    'nome': 'Fabio',
    'sobrenome': 'Classo',
    'funcao':'Desenvolvedor',
    'idade':45
}

print(funcionario)
print(funcionario['nome'])
print(funcionario['sobrenome'])
print(funcionario['funcao'])
print(funcionario['idade'])

print(f"Nome: {funcionario['nome']}, sobrenome:{funcionario['sobrenome']},"
      f" funcao:{funcionario['funcao']}, idade:{funcionario['idade']}")

# alterei
funcionario['idade'] = 46
print(funcionario)
del funcionario['sobrenome']
print(funcionario)

print(funcionario.keys())
print(funcionario.values())
print(funcionario.items())