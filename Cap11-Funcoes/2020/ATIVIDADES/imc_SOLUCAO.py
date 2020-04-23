lista_de_pacientes = []


def calcula_imc():
    nome = input('Digite o nome do paciente: ')
    altura = float(input('Digite a altura do paciente: '))
    peso = float(input('Digite a pse do paciente: '))
    imc = peso / altura ** 2
    imc = '{:.2f}'.format(imc)  # formatador de casa decimal
    print(f'Nome: {nome}, Altura: {altura}, Peso:{peso}, IMC: {imc}')
    paciente = (nome, imc)
    #print(paciente)
    lista_de_pacientes.append(paciente)


def lista_paciente():
    for user in lista_de_pacientes:
        print(user)


def menu_opcoes():
    menu =''

    while menu != 0:
        menu = int(input(
            """
                1 - Para inserir um novo valor
                2 - Listar usuarios cadastrados
                3 - salvar dados
                0 - para sair do programa
                
            """
        ))

        if menu == 1:
            print()
            print('Inserindo novo cadastro: ______')
            print()
            calcula_imc() # chamada da funcao, executa

        elif menu == 2:
            print('Lista de usuarios cadastrados')

            lista_paciente()

        elif menu == 3:
            print('Salvando dados')
        elif menu == 0:
            print('Saindo do programa')

        else:
            print('Opcao errada')


menu_opcoes()