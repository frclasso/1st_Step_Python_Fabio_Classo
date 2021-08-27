
def get_nomes_das_colunas():
    pass



def extrac_values_1(dict):
    """Extrai apenas od valores de um dicionario"""
    values = []
    for k , v in dict.items():
        #print(k, v)
        values.append(v)
    return values

def extract_values_2(dict):
    """Extrai apenas od valores de um dicionario"""
    values = list(dict.values())
    return values


def salva_em_csv():
    pass


peter_parker =  {'sobrenome':'Parker', 'nome':'Peter', 'idade':44,'sexo':'M', 'cpf':'045045045', 'telefone':9999888,
                    'cartaoCredito':'MasterCard', 'numeroCartao':'12345-0', 'dataValidade':'10/19',
                    'codigoSeguranca':215}

bruce_wayner = {'sobrenome':'Wayne','nome':'Bruce','idade':28,'sexo':'F','cpf':'345665045','telefone':99998888,
                     'cartaoCredito':'VISA', 'numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}


michael_jackson =  {'sobrenome':'Jackson','nome':'Michael','idade':39,'sexo':'M','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'Nubank','numeroCarato':'12345-0', 'dataVailidade':'10/19','codigoseguranca' :215}


# usar para inserir em um banco de dados

# 1
#print(extract_values(peter_parker))

# 2
#print(extrac_values_2(peter_parker))


