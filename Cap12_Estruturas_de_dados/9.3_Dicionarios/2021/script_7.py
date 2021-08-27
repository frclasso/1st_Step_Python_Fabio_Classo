#!/usr/bin/env python3
import os

# IDENTIDADE , sobrenome, nome, idade, sexo, cpf, telefone, cartao, numero do cartao, data expiracao, codigo val

id_clientes = [
      ('22112233', {'sobrenome':'Parker', 'nome':'Peter', 'idade':44,'sexo':'M', 'cpf':'045045045', 'telefone':9999888,
                    'cartaoCredito':'MasterCard', 'numeroCartao':'12345-0', 'dataValidade':'10/19',
                    'codigoSeguranca':215}),

      ('23112233', {'sobrenome':'Wayne','nome':'Bruce','idade':28,'sexo':'F','cpf':'345665045','telefone':99998888,
                     'cartaoCredito':'VISA', 'numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('33221122', {'sobrenome':'Jackson','nome':'Michael','idade':39,'sexo':'M','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'Nubank','numeroCarato':'12345-0', 'dataVailidade':'10/19','codigoseguranca' :215}),

      ('44332211',{'sobrenome':'Shorter','nome':'Wayne','idade':37,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'PayPal','numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('55443322',{'sobrenome':'Trump','nome':'Donald','idade':46,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Credicard','numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('66554433',{'sobrenome':'Schuwazenerger','nome':'Arnold','idade':42,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Elo','numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca' :215}),

      ( '77665566',{'sobrenome':'Marley','nome':'Bob','idade':40,'sexo':'F','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'American Express','numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca':215}),

      ('88665577',{'sobrenome':'Martino','nome':'Pat','idade':74,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Dinners Club', 'numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca':215})

]

# Analise previa
# Tipo de estrutura de dados
print(type(id_clientes))
#print(id_clientes)
print()

# VERIFICANDO UM REGISTRO
# print(type(id_clientes[0]))
# print(id_clientes[0])
# print()

# print(id_clientes[0][0])
# print(id_clientes[0][1])
# print()

# for data in id_clientes[0]:
#     print(data)
# print()

# Verificando todos os registros
# for ID, dados in id_clientes:
#     #print(ID, dados)
#     print(ID, dados['sobrenome'],',', dados['nome'], ',', dados['cartaoCredito'])
# print("=" * 80)
# print()


def dados_do_cliente(cliente):
    """Essa função retorna dados de m unico cliente"""
    for data in cliente:
        #print(data)
        #print(type(data))
        dados_cliente = {}
        for k, v in cliente[1].items():
            #print(k, v)
            d = {k :v}
            dados_cliente.update(d)
        return dados_cliente


#print(dados_do_cliente(id_clientes[0]))



import os
# alterando diretorio de trabalho
current_path = "C:/Users/fabio.classo/Downloads/fabio/aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/9.3_Dicionarios/2021"
os.chdir(current_path)

def salva_registro(registro):
    """Salvando em um arquivo .txt"""
    with open('dados_clientes_3.txt','a') as file_writer:
        dados_selecionados = dados_do_cliente(registro)
        print(dados_selecionados)
        for k, v in dados_selecionados.items():
            print(k,v)
            file_writer.write(str(k))
            file_writer.write(',')
            file_writer.write(str(v))
            file_writer.write(',')
        file_writer.write('\n')
        print("Dados salvos com sucesso")

#salva_registro(id_clientes[0])


# with open('clientes.txt', 'w') as f:
#     for ID ,dados in id_clientes:
#         f.write('\n{},{},{},{},{},{},{},{}'.format(ID,dados['sobrenome'],dados['nome'], dados['idade'], dados['sexo'],
#                                     dados['cpf'], dados['telefone'], dados['cartaoCredito']))


# """Salvando  em um arquivo .csv"""
# #
# import csv

# with open('clientes.csv', mode='w') as f2:
#     csv_file = csv.writer(f2)
#     for ID ,dados in id_clientes:
#         f2.write('\n{},{},{},{},{},{},{},{}'.format(ID,dados['sobrenome'],dados['nome'], dados['idade'], dados['sexo'],
#                                                     dados['cpf'], dados['telefone'], dados['cartaoCredito']))


# print('Arquivos gerados com Sucesso:', f.name,',', f2.name)
# print('Done...')
