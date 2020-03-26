# https://calculosalarioliquido.com/

empresa = "Floripa Code Gurus Escola de Tecnologia"
competencia = 'Novembro 2019'
codigo_colaborador = 10001
nome ='Fabio Reis Classo'
data_admissao = '18/11/2019'
cargo = 'Analista de Sistemas'
qtd_horas_trabalhadas = 160
vale_refeicao = 39.91
horas_extras = 0
qtd_dependentes = 0

salario_base =3000


def faixa_de_INSS(salario):
    if salario <= 1693.72:
        inss = (8/100)
        desconto = salario * inss
    elif 1693.73 <= salario <= 2822.90:
        inss = (9/100)
        desconto = salario * inss
    elif 2822.91 <= salario <= 5645.80:
        inss = (11/100)
        desconto = salario * inss
    else:
        sal_d = salario - 621.04
        desconto = salario - sal_d
    return desconto


def faixa_de_IRPF(salario, qtd_dependentes=0):

    deducao_dependentes = qtd_dependentes * 189.59

    if salario < 1903.98:
        desconto = 0
    elif 1903.99 <= salario <= 2826.65:
        irrf = (7.5/100)
        parcela = 142.80
        # print(f'Salario atual: R${salario:.2f}')
        desc = salario * irrf - parcela - deducao_dependentes
        desconto= abs(desc)
    elif 2826.66 <= salario <= 3751.05:
        irrf = (15/100)
        parcela = 354.80
        desc = salario * irrf - parcela - deducao_dependentes
        desconto= abs(desc)
    elif 3751.06 <= salario <= 4664.68:
        irrf = (22.5/100)
        parcela = 636.13
        desc = salario * irrf - parcela - deducao_dependentes
        desconto= abs(desc)
    else:
        irrf = (27.5/100)
        parcela = 869.36
        desc = salario * irrf - parcela - deducao_dependentes
        desconto= abs(desc)

    return desconto


def total_de_descontos(inss, irrf, vale_refeicao):
    return inss + irrf + vale_refeicao


def saida():
    print()
    print(empresa)
    print(f'Codigo colaborador: {codigo_colaborador, }Nome: {nome}, '
          f'Data de admissoa: {data_admissao}, Cargo: {cargo}')
    print(f'Salario Base: R${salario_base:.2f}')
    print(f'Numero de dependentes: {qtd_dependentes}')
    print(f'Adicionais: ')
    print(f'Comissões:')
    print(f'Horas Trabalhandas: {qtd_horas_trabalhadas}')
    print(f'Horas extras: {horas_extras}')
    print()
    print(f'Descontos:')
    inss = faixa_de_INSS(salario_base)
    salario_menos_inss = salario_base - faixa_de_INSS(salario_base)
    irrf = faixa_de_IRPF(salario_menos_inss, 0)
    print(f'Desconto de INSS: R${inss:.2f}')
    print(f'Desconto de IRRF: R${irrf:.2f}')
    total_desc = total_de_descontos(inss, irrf, vale_refeicao)
    print(f'Total descontos: R${total_desc:.2f}')
    salario_liquido = salario_base - total_desc
    print(f'Total liquido a receber: R${salario_liquido:.2f}')


    with open('holerite.csv', 'w') as file:
        file.write('Nome, Salario base, Descontos, Sal Liq')
        file.write('\n')
        file.write(nome + ',' +str(salario_base) + ',' + str(total_desc) + ',' + str(salario_liquido) + '\n')

saida()