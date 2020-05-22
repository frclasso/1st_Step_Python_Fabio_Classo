import datetime



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


# CASO 1
# with open('clientes.csv', 'w') as file:
#     for header in headers:
#         file.write(header + ',')
#     file.write('\n')
#     for cliente in cliente1:
#         file.write(cliente + ',')
#
# print(f'Arquivo: {file.name} criado com sucesso')


# CASO 2 - UTILIZANDO A BIBLIOTECA CSV
import csv
with open('clientes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerow(cliente1)
    writer.writerow(cliente2)

print(f'Arquivo: {csvfile.name} criado com sucesso')
