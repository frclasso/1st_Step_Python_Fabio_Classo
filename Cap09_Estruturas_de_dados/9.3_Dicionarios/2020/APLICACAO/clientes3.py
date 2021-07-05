#!/usr/bin/env python3

"""Aplicação de dados de clientes"""

# Dicionario de clientes
print()
print('-' * 90)
print('Hotel Floripa Paradise')
print('Relação de de clientes')
print()

# IDENTIDADE , sobrenome, nome, idade, sexo, cpf, telefone, cartao, numero do cartao, data expiracao, codigo val
clientes = {
      '11223344':['Classo', 'Fabio', 44,'M','045045045',99998888,'MasterCard', 12345-0, '10/19', 215],
      '22112233':['Ferreira', 'Joanna', 28,'F','345665045',99998888,'VISA', 12345-0, '10/19', 215],
      '33221122':['Pereira de Moraes', 'Karbony', 39,'M','045045045',99998888,'Nubank', 12345-0, '10/19', 215],
      '44332211':['Faccin de Almeida', 'Andre', 37,'M','045045045',99998888,'PayPal', 12345-0, '10/19', 215],
      '55443322':['Cardoso', 'Jonas', 46,'M','045045045',99998888,'Credicard', 12345-0, '10/19', 215],
      '66554433':['Lopes', 'César', 42,'M','045045045',99998888,'Elo', 12345-0, '10/19', 215],
      '77665566':['Reis', 'Juliana', 40,'F','045045045',99998888,'American Express', 12345-0, '10/19', 215],
      '88665577':['Neto', 'Ramiro', 74,'M','045045045',99998888,'Dinners Club', 12345-0, '10/19', 215]
}


# for id , dados in clientes.items():
#       print(f"Registro  - ID:{id}, - Dados :{dados}.")
#
# print()

print(clientes['33221122'][0])

# Loop aninhado, exibindo apenas os nomes
# for c in clientes.items():
#     for nome in c[1][0].split():
#         print('Cliente:',nome)


