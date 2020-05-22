import os
from datetime import datetime

#print(os.listdir('.'))

from clientes_autalizado import cabecalho, clientes

#print(cabecalho)
# print(clientes)

# for cliente in clientes:
#     print(cliente)

clientes_iter = iter(clientes)


def get_uma_linha():
    """ Capturando o valor de uma linha """
    cliente = []
    for i in range(8):
        #print(next(clientes_iter))
        dados = next(clientes_iter)
        cliente.append(dados)
    return cliente


# print(get_uma_linha())
# print(get_uma_linha())

# ATIVIDADE DA SEMANA
# 1 - criar uma funcao que valide email "nome.sobrenome@empresa.com"
# criar lista de empresas
# 2 - criar uma funcao que valide telefone, remover caracteres que nao sejam numeros
# 3 - criar uma funcao que valide data:  "2010-01-05"
# 4 - criar uma funcao que leia  o coteudo da lista cientes

def gera_email(linha):
    """Recebe os dados de um cliente e valida o campo email"""
    # print(linha)
    # print(type(linha))
    nome_completo = linha[0]
    # print(nome_completo)
    nome, sobrenome = nome_completo.split()
    # print(nome)
    # print(sobrenome)
    email = f'{nome.lower()}.{sobrenome.lower()}@email.com'
    # print(email)
    return email

l = get_uma_linha()
#gera_email(l)

def valida_telefone(linha):
    #print(linha)
    telefone = linha[4]
    #print(telefone)
    telefone = telefone.replace('(','').replace(')', '').replace('-', '')
    #print(telefone)
    return telefone


valida_telefone(l)

def valida_data(linha):
    """Recebe uma linha e valida campo data"""
    #print(linha)
    data_str = linha[7]
    # print(data_str)
    # data = data_str[:10]
    # print(data)
    #
    # print(datetime.fromisoformat(data_str))
    #print(datetime.fromisoformat(data_str).date())
    data_valida = datetime.fromisoformat(data_str).date()
    #print(data_valida)
    return data_valida


valida_data(l)

def cliente_atulizado(linha):

    email = gera_email(linha)
    telefone = valida_telefone(linha)
    data = valida_data(linha)
    #print(email, telefone, data)
    # print(linha)
    dados_atualizados = linha
    dados_atualizados.pop(3)
    dados_atualizados.insert(3, email)
    dados_atualizados.pop(4)
    dados_atualizados.insert(4, telefone)
    dados_atualizados.pop(7)
    dados_atualizados.insert(7, str(data))
    print(dados_atualizados)
    return dados_atualizados

#cliente_atulizado(l)

for c in clientes:
    try:
        linha = get_uma_linha()
        cliente_atulizado(linha)
    except StopIteration:
        break




