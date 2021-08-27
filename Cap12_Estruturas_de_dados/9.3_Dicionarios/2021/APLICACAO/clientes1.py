#!/usr/bin/env python3

"""Aplicação de dados de clientes"""

# Cadastrando dados com variáveis fixas
print('Hotel Floripa Paradise')
print('Cadastro de clientes')

# nome = 'Fabio'
# sobrenome = 'Classo'
# idade = 44
# sexo = 'M'
# cpf = '045045045'
# identidade = '454545'
# ddd = '48'
# telefone = 99998888
# cartao_credito = 'MasterCard'
# numero_cartao_de_credito = 12345
# data_expiracao = '10/19'
# cod_validacao = 215


# Utilizando método dinâmico - input via prompt

nome = input("Digite o nome do cliente: ")
sobrenome = input('Dogite o sobrenome: ')
idade =int(input("Digite a idade do cliente: "))
sexo = input("Digite o sexo do cliente, M(Masculino) ou F(Feminino): ")
cpf = input("Digite o CPF do cliente: ")
identidade = input("Digite a identidade do cliente: ")
ddd = input('DDD , ex: (48):')
telefone = input('Digite o telefone do cliente: ')
cartao_credito = input('Qual  cartao de credito? VISA/MasterCard: ')
numero_cartao_de_credito = input('Numero do cartao de crédito: ')
data_expiracao = input('Data de expiracao: ')
cod_validacao = input('Codigo de validacao: ')
print()

print('Dados do cliente cadastrado')
print()
print(f'Cliente: Mr/Mrs/Ms/Miss {sobrenome},{nome}. ')
print(f'Idade:{idade} anos')
print(f'Sexo:{sexo}')
print(f'CPF:{cpf}')
print(f'Identidade:{identidade}')
print(f'Telefone: DDD +55({ddd})-{telefone}')
print(f'Cartão de Crédito: {cartao_credito} - Número:{numero_cartao_de_credito} - Expira em: {data_expiracao}'
      f' - Código validação: {cod_validacao}')
print()
print('-' * 90)
print('Registro realizado com sucesso')