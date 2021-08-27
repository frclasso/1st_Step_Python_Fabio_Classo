#!/usr/bin/env python3

# IDENTIDADE , sobrenome, nome, idade, sexo, cpf, telefone, cartao, numero do cartao, data expiracao, codigo val
dicionario_clientes = {
      '11223344':['Parker', 'Peter', 44,'M','045045045',99998888,'MasterCard', 12345-0, '10/19', 215],
      '22112233':['Wayne', 'Bruce', 28,'F','345665045',99998888,'VISA', 12345-0, '10/19', 215],
      '33221122':['Jackson', 'Michael', 39,'M','045045045',99998888,'Nubank', 12345-0, '10/19', 215],
      '44332211':['Shorter', 'Wayne', 37,'M','045045045',99998888,'PayPal', 12345-0, '10/19', 215],
      '55443322':['Trump', 'Donald', 46,'M','045045045',99998888,'Credicard', 12345-0, '10/19', 215],
      '66554433':['Schuwazenerger', 'Arnold', 42,'M','045045045',99998888,'Elo', 12345-0, '10/19', 215],
      '77665566':['Marley', 'Bob', 40,'F','045045045',99998888,'American Express', 12345-0, '10/19', 215],
      '88665577':['Martino', 'Pat', 74,'M','045045045',99998888,'Dinners Club', 12345-0, '10/19', 215]
}
print()
# Analise previa
# Tipo de estrutura de dados
#print(type(dicionario_clientes))
#print(dicionario_clientes)
print()


# for id , dados in dicionario_clientes.items():
#       print(f"ID:{id}, - Dados :{dados}.")

# print()

# VERIFICANDO UM REGISTRO
#print(type(dicionario_clientes['11223344']))
#print(dicionario_clientes['11223344'])

# RECUPERANDO DADOS DE UM REGISTRO COM LOOP FOR
# for k, v in dicionario_clientes.items():
#     #print(k, v)
#     if k =="11223344":
#         print(k, v)

# print()

def dados_do_cliente(cliente):
    """Essa função retorna dados de m unico cliente"""
    for k, v in dicionario_clientes.items():
        if k == cliente:
            data = {k :v}
            return data

#print(dados_do_cliente("11223344"))

def salva_registro(registro):
    import os
    # alterando diretorio de trabalho
    current_path = "C:/Users/fabio.classo/Downloads/fabio/aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/9.3_Dicionarios/2021"
    os.chdir(current_path)

    with open('dados_clientes_2.txt','a') as file_writer:
        dados_selecionados = dados_do_cliente(registro)
        #print(dados_selecionados)
        for k, v in dados_selecionados.items():
            print(k,v)
            file_writer.write(str(k))
            file_writer.write(',')
            for data in v:
                print(data)
                file_writer.write(str(data))
                file_writer.write(',')
        file_writer.write('\n')
        print("Dados salvos com sucesso")

salva_registro("11223344")