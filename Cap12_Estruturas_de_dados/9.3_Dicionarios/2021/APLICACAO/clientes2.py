#!/usr/bin/env python3

"""Aplicação de dados de clientes"""

# Lista de clientes
print()
print('-' * 90)
print('Hotel Floripa Paradise')
print('Relação de de clientes')
print()

# sobrenome, nome, idade, sexo, cpf, identidade, telefone, cartao, numero do cartao, data expiracao, codigo val
lista_de_clientes = [
      ['Parker', 'Peter', 44,'M','045045045', '454545-0',99998888,'MasterCard', 12345-0, '10/19', 215],
      ['Wayne', 'Bruce', 28,'F','345665045', '454545-0',99998888,'VISA', 12345-0, '10/19', 215],
      ['Jackson', 'Michael', 39,'M','045045045', '454545-0',99998888,'Nubank', 12345-0, '10/19', 215],
      ['Shorter', 'Wayne', 37,'M','045045045', '454545-0',99998888,'PayPal', 12345-0, '10/19', 215],
      ['Trump', 'Donald', 46,'M','045045045', '454545-0',99998888,'Credicard', 12345-0, '10/19', 215],
      ['Schuwazenerger', 'Arnold', 42,'M','045045045', '454545-0',99998888,'Elo', 12345-0, '10/19', 215],
      ['Marley', 'Bob', 40,'F','045045045', '454545-0',99998888,'American Express', 12345-0, '10/19', 215],
      ['Martino', 'Pat', 74,'M','045045045', '454545-0',99998888,'Dinners Club', 12345-0, '10/19', 215]
]
print(lista_de_clientes)
print()
print(lista_de_clientes[0][1]) # Peter

print(lista_de_clientes[1][1]) #Bruce
print()

for cliente in lista_de_clientes:
      #print(cliente)
      print(f'Noome: {cliente[1]}, nr_cartao: {cliente[6]}')


#for lista in lista_de_clientes:
#      print(f'Sobrenome:{lista[0]}, Nome:{lista[1]}, Idade:{lista[2]}, Sexo:{lista[3]},'
#      f'CPF:{lista[4]}, Identidade:{lista[5]}, Tel:{lista[6]}, Cartao:{lista[7]}, Num:{lista[8]},'
#            f'Expira em:{lista[9]}, Codigo val:{lista[10]}')

