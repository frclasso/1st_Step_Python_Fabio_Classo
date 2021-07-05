# variaveis

nome = 'Fabio'
sobrenome = 'Classo'
cargo = 'Desenvolvedor de Software'
telefone = '(48)99174-3152'
email = 'frclasso@gmail.com'

print(nome, sobrenome, email)

cargo = 'Desenvolvedor'
lang = 'Python'
versao = 3.8
ano = 2020

# formatadores de string
print('Nome: , cargo: , tecnologia: , em: ')

# Python2.7
print('Nome: %s, cargo: %s, tecnologia: %s, versao: %f , em: %d' % (nome, cargo, lang,versao, ano))
 # %s == string
 # %f == float
 # %d == inteiro

# Python 3.6.5
print('Nome: {}, cargo: {}, tecnologia: {}, versao: {} , em: {}'.format(nome, cargo, lang,versao, ano))

# Python 3.7.3
print(f'Nome: {nome}, cargo: {cargo}, tecnologia: {lang}, versao: {versao} , em: {ano}')