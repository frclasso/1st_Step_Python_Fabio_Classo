# Todas as funcoes
print('Listando todas as funções Python.')
print(dir())
print()

# Funcoes Built-ins
print('Listando as funções Built-ins')
print(dir('__builtins__'))
print()

# help - funcao
print('Help')
#print(help(list))
print()

# type - retorna o tipo da estrutura de dados avaliada
print('type: ',type('Pyhton'))
print()

# id - retorna o endereço de memória de uma variável
tecnologia = 'Python3.8.7'
print(f'id  de tecnologia: {id(tecnologia)}')
print()


# input()
nome = input('Digite seu nome: ')
print(nome)

idade = int(input('Digite sua idade: '))
print(idade)

peso = float(input('Digite seu peso em Kg: '))
print(peso)


# isinstance()
companies = ('Audi', 'Tesla', 'Apple')
print('método isinstance: ',isinstance(companies, tuple))

# len() - retorna o tamanho/quantidade de elementos
print('len: ',len('Python'))
print()


# max, min, sum
numbers = (10,20,30,40,50)
print('len de x: ', len(numbers))
print('max: ', max(numbers))
print('min: ', min(numbers))
print('Sum: ',sum(numbers))
print()

# ranage()

# Start
print('Range')
print(range(10))
print(list(range(10)))

# Start e Stop
print(range(1, 11))
print(list(range(1, 11)))

# Start - Stop - Step
print(range(0, 30, 5))
print(list(range(0, 30, 5)))
print()


# round()
num = 80.26467
print('round number :',round(num, 2))


# abs()
print('Absoluto de um numero')
print(abs(-45))
temperature = -2.4
print(abs(temperature))
print()

# pow() - potencia
# x = base, y = exponent
print(f'3 elevado a 2 = {pow(3,2)}')

# sorted()
pointsInGame = [0,-10,15,-2,1,12]
print(sorted(pointsInGame))
# modo reverso ,lista
print(sorted(pointsInGame, reverse=True))

# Ordem alfabetica
children =['Sue', 'Jerry','Linda', 'Amanda']
print(sorted(children))


print()

# enumerate()
animals = ('cat', 'dog','rabbit', 'monkey', 'bird')
for i, v in enumerate(animals):
    print(f'{i}:{v}')

