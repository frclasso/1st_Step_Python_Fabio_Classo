import datetime


# w x a


headers = ['nome', 'sobrenome', 'idade', 'cpf', 'email', 'fone', 'formacao', 'empresa', 'cargo', 'cidade', 'uf',
          'criado_em']

criado_em = datetime.date.today()

cliente1 = ['Fabio',
            'Classo',
            '40',
            '111222333444',
            'fabio.classo@nexxera.com'
            '(48)9999988888',
            'Sistemas de Informação',
            'Grupo Nexxera',
            'Analista de Sistemas',
            'Florianopolis',
            'SC',
            str(criado_em)]

with open('pessoas.txt', 'w') as file:
    for h in headers:
        file.write(h +',')
    file.write('\n')
    for dados in cliente1:
        file.write(dados + ',')


cliente2 = ['Giovanna',
            'Classo',
            '8',
            '1112223330000',
            'giovanna.classo@email.com'
            '(48)9999988888',
            'Series inicais',
            'Centro Educacional Santo Antonio',
            'Estudante Ensino Fundamental',
            'Florianopolis',
            'SC',
            str(criado_em)]

# with open('pessoas.txt', 'w') as file:  # TROCAR PARA 'a' - append
#     file.write('\n')
#     for dados in cliente2:
#         file.write(dados + ',')

