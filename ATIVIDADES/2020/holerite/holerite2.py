from snippet import *

print(empresa)
print(competencia)
linha = '='*135
print(linha)


def faixa_de_INSS(salario):
    if salario < 1693.72:
        inss = (8/100)
        desconto = salario * inss
    elif 1693.73 < salario < 2822.90:
        inss = (9/100)
        desconto = salario * inss
    elif 2822.91 < salario < 5645.80:
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
    elif 1903.9 < salario < 2826.65:
        irrf = (7.5/100)
        parcela = 142.80
        # print(f'Salario atual: R${salario:.2f}')
        desc = salario * irrf - parcela - deducao_dependentes
        desconto= abs(desc)
    elif 2826.65 < salario < 3751.05:
        irrf = (15/100)
        parcela = 354.80
        desc = salario * irrf - parcela - deducao_dependentes
        desconto= abs(desc)
    elif 3751.05 < salario < 4664.68:
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


def saida(nome, data_admissao, cargo, qtd_horas_trabalhadas, vale_refeicao, horas_extras, salario_base,
          qtd_dependentes, codigo_colaborador):

    print(f'Codigo colaborador: {codigo_colaborador}')
    print(f'Nome: {nome}')
    print(f'Data de admissoa: {data_admissao}')
    print(f'Cargo: {cargo}')
    print(f'Salario Base: R${salario_base:.2f}')
    print(f'Numero de dependentes: {qtd_dependentes}')
    print(f'Adicionais: ')
    print(f'Comissões:')
    print(f'Horas Trabalhandas: {qtd_horas_trabalhadas}')
    print(f'Horas extras: {horas_extras}')
    print(f'Descontos: ' + '>' * 15)
    inss = faixa_de_INSS(salario_base)
    salario_menos_inss = salario_base - faixa_de_INSS(salario_base)
    irrf = faixa_de_IRPF(salario_menos_inss, 0)
    print(f'Desconto de INSS: R${inss:.2f}')
    print(f'Desconto de IRRF: R${irrf:.2f}')
    total_desc = total_de_descontos(inss, irrf, vale_refeicao)
    print(f'Total descontos: R${total_desc:.2f}')
    salario_liquido = salario_base - total_desc
    print(f'Total liquido a receber: R${salario_liquido:.2f}')
    print(linha)
    print()
    # formatar depois dos calculos

    salario_base = f'{salario_base:.2f}'
    total_desc = f'{total_desc:.2f}'
    salario_liquido = f'{salario_liquido:.2f}'

    file_name = nome.lower()+ str(codigo_colaborador) + '.csv'
    with open(file_name, 'w') as file:
        file.write('Nome, Salario base, Descontos, Sal Liq')
        file.write('\n')
        file.write(nome + ',' + salario_base + ',' + total_desc + ',' + salario_liquido + '\n')

# print(colaboradores[0])
# saida(nome=colaboradores[0]['nome'],
#       data_admissao=colaboradores[0]['data_admissao'],
#       cargo=colaboradores[0]['cargo'],
#       qtd_horas_trabalhadas=colaboradores[0]['qtd_horas_trabalhadas'],
#       vale_refeicao=colaboradores[0]['vale_refeicao'],
#       horas_extras=colaboradores[0]['horas_extras'],
#       salario_base=colaboradores[0]['salario_base'],
#       qtd_dependentes=colaboradores[0]['qtd_dependentes'],
#       codigo_colaborador=colaboradores[0]['codigo_colaborador']
#       )


def geraHolerites():
    import os
    dir_raiz = '/Users/fabio/Estudo/Prog/Python/1st_Step_Python_2020/ATIVIDADES/2020/holerite'
    new_dir = 'holerites2020'

    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    os.chdir('holerites2020')

    for col in colaboradores:
            # print(col)
            for k,v in col.items():
                saida(nome=col['nome'],
                      data_admissao=col['data_admissao'],
                      cargo=col['cargo'],
                      qtd_horas_trabalhadas=col['qtd_horas_trabalhadas'],
                      vale_refeicao=col['vale_refeicao'],
                      horas_extras=col['horas_extras'],
                      salario_base=col['salario_base'],
                      qtd_dependentes=col['qtd_dependentes'],
                      codigo_colaborador=col['codigo_colaborador']
                      )
    os.chdir(dir_raiz)


geraHolerites()