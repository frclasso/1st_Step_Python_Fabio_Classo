#!/usr/bin/env python3

import csv

print('Cadastro  de clientes')
print()


def cadastro_clientes():
    nome = input('Digite nome do usuario: ')
    sobrenome = input('Didige o sobrenome: ')
    email = input('Digite o email: ')
    clientes.append(nome)
    clientes.append(sobrenome)
    clientes.append(email)
    with open('clientes.csv', 'a') as csv_file:
        for l in clientes:
            cadastra = csv.writer(csv_file)
            cadastra.writerow(nome + sobrenome + email)

def atualiza_cadastro(): # dentro de clientes.csv
    print('Alterar cadastro')


def deleta_cadastro(): # dentro de clientes.csv
    print('Deletar cadastro')


def lista_clientes(): # dentro de clientes.csv
    try:
        with open('clientes.csv', 'r') as csv_file:
            leitor = csv.reader(csv_file)
            for line in leitor:
                print(line)
    except IOError: print('Arquivo nao encontrado')
    opcao()


def salvar():
    # Salvando em um arquivo .csv
    with open('clientes.csv', 'a') as clientes_file:
        writelines = csv.writer(clientes_file, delimiter=',')
        for line in clientes:
            writelines.writerow(line)
        print('Dados salvos com sucesso')


clientes = []  # salva os dados cadastrados temporariamente



def opcao():
    while True:
        print()
        menu = int(input('''Escolha uma opção
                    1 para cadastrar novo cliente;
                    2 para alterar cadastro existente;
                    3 para Deletar cadastro;
                    4 para listar os clientes cadastrados
                    5 para gravar dados
                    0 para Sair do programa: '''))
        if menu == 0:
            break
        if menu == 1:
            cadastro_clientes()
        elif menu == 2:
            atualiza_cadastro()
        elif menu == 3:
            deleta_cadastro()
        elif menu == 4:
            lista_clientes()
        elif menu == 5:
            salvar()
        else:
            print('Voce deve escolher uma opção')

print()

# chamada de funcao
opcao()

