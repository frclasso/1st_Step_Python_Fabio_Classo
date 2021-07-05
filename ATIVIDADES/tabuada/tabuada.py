"""Criar um aplicacao de tabuada simples,
imaginem ensinar tabuada pra uma criança"""




# range
# n = 11
# while n != 11:
#      fibonacci_exemplos = range(11)
#      for num in fibonacci_exemplos:
#           print(f'O Numero {n} * {num} = {num * n}')

continua = ['sim', 's']
sair = ['nao', 'n']
resposta = 's'
while resposta in continua:
     try:
          tabuada = int(input('Digite a tabuada:'))
          for i in range(1, 11):
               print(i, '*', tabuada, '=', i * tabuada)
     except ValueError:
          print('Precisa ser um numero inteiro')
     resposta = input('Vamos fazer outra tabuanda? sim/nao')
print('Saindo..')

