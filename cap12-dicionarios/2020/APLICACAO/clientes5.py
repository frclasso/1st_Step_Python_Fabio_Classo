#!/usr/bin/env python3

"""Aplicação de dados de clientes"""

# Dicionario de clientes
print()
print('-' * 90)
print('-'* 33 ,'Hotel Floripa Paradise','-'* 33)
print('-'* 33,'Salvando seus dados','-'* 33)
print()


# IDENTIDADE , sobrenome, nome, idade, sexo, cpf, telefone, cartao, numero do cartao, data expiracao, codigo val

id_clientes = [
      ('22112233', {'sobrenome':'Classo', 'nome':'Fabio', 'idade':44,'sexo':'M', 'cpf':'045045045', 'telefone':9999888,
                    'cartaoCredito':'MasterCard', 'numeroCartao':'12345-0', 'dataValidade':'10/19',
                    'codigoSeguranca':215}),

      ('23112233', {'sobrenome':'Ferreira','nome':'Joanna','idade':28,'sexo':'F','cpf':'345665045','telefone':99998888,
                     'cartaoCredito':'VISA', 'numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('33221122', {'sobrenome':'Pereira','nome':'Karbony','idade':39,'sexo':'M','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'Nubank','numeroCarato':'12345-0', 'dataVailidade':'10/19','codigoseguranca' :215}),

      ('44332211',{'sobrenome':'Faccin','nome':'Andre','idade':37,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'PayPal','numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('55443322',{'sobrenome':'Cardoso','nome':'Jonas','idade':46,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Credicard','numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('66554433',{'sobrenome':'Lopes','nome':'Cesar','idade':42,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Elo','numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca' :215}),

      ( '77665566',{'sobrenome':'Reis','nome':'Juliana','idade':40,'sexo':'F','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'American Express','numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca':215}),

      ('88665577',{'sobrenome':'Neto','nome':'Ramiro','idade':74,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Dinners Club', 'numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca':215})

]


# Verificando
# for ID, dados in id_clientes:
#     print(ID, dados['sobrenome'],',', dados['nome'], ',', dados['cartaoCredito'])

"""Salvando em um arquivo .txt"""

with open('clientes.txt','w') as f:
    for ID ,dados in id_clientes:
        f.write('\n{},{},{},{},{},{},{},{}'.format(ID,dados['sobrenome'],dados['nome'], dados['idade'], dados['sexo'],
                                    dados['cpf'], dados['telefone'], dados['cartaoCredito']))


"""Salvando  em um arquivo .csv"""
#
import csv

with open('clientes.csv', mode='w') as f2:
    csv_file = csv.writer(f2)
    for ID ,dados in id_clientes:
        f2.write('\n{},{},{},{},{},{},{},{}'.format(ID,dados['sobrenome'],dados['nome'], dados['idade'], dados['sexo'],
                                                    dados['cpf'], dados['telefone'], dados['cartaoCredito']))


print('Arquivos gerados com Sucesso:', f.name,',', f2.name)
print('Done...')
