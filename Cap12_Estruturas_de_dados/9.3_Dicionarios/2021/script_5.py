
import os

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
# Analise previa
# Tipo de estrutura de dados
print(type(lista_de_clientes))
print(lista_de_clientes)
print()

# VERIFICANDO UM REGISTRO
print(type(lista_de_clientes[0])) # 
print(lista_de_clientes[0][1]) # Peter
print(lista_de_clientes[1][1]) #Bruce
print()

# RECUPERANDO DADOS DE UM REGISTRO COM LOOP FOR
# for cliente in lista_de_clientes:
#       #print(cliente)
#       print(f'Noome: {cliente[1]}, nr_cartao: {cliente[6]}')

print()
# for lista in lista_de_clientes:
#      print(f'Sobrenome:{lista[0]}, Nome:{lista[1]}, Idade:{lista[2]}, Sexo:{lista[3]},'
#      f'CPF:{lista[4]}, Identidade:{lista[5]}, Tel:{lista[6]}, Cartao:{lista[7]}, Num:{lista[8]},'
#            f'Expira em:{lista[9]}, Codigo val:{lista[10]}')

print("=" *160)
print()

def dados_do_cliente(cliente):
    dados_do_cliente = []
    for dados in cliente:
        #print(dados)
        dados_do_cliente.append(dados)
    return(dados_do_cliente)

#print(dados_do_cliente(lista_de_clientes[0]))

#print(os.getcwd())

current_path = "C:/Users/fabio.classo/Downloads/fabio/aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/9.3_Dicionarios/2021"

os.chdir(current_path)
print(os.getcwd())

def salva_registro(registro):
    with open('dados_clientes.txt','a') as file_writer:
        dados_selecionados = dados_do_cliente(registro)
        for data in dados_selecionados:
            print(data)
            file_writer.write(str(data))
            file_writer.write(',')
        file_writer.write('\n')
        print("Dados salvos com sucesso")

salva_registro(lista_de_clientes[0])

