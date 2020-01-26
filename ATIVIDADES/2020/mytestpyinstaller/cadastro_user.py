import datetime

now = datetime.datetime.now()

nome = input("Digite o nome do novo registro: ")

with open('usuarios.csv', 'a') as file:
   file.write(nome + ',')
   file.write('\n')
print('Done')

with open('alteracoes.txt', 'a') as file_log:
    msg = 'Novo usuario cadastrado'
    file_log.write(f'Novo usuario cadastrado: {nome} - {now}\n')
