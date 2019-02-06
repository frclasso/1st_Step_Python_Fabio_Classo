#!/usr/bin/env python3


# menu
# if, elif, else => switch case

print('Cadastro  de clientes')
print()
menu = int(input('''Escolha uma opção
                    1 para cadastrar novo cliente;
                    2 para alterar cadastro existente;
                    3 para Deletar cadastro;
                    0 para Sair do programa: '''))

if menu == 1:
    print('Cadastrar novo cliente')
elif menu == 2:
    print('Alterar cadastro')
elif menu == 3:
    print('Deletar cadastro')
elif menu == 0:
    print('Sair')
else:
    print('Voce deve escolher uma opção')

