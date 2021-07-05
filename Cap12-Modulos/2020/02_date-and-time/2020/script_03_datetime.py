import datetime

print(dir(datetime))
agora = datetime.datetime.now()
print(f'Agora: {agora}')
print()

data_atual = datetime.date.today()
print(f'Data de hoje: {data_atual}')
print(f'Ano: {data_atual.year}')
print(f'Mês: {data_atual.month}')
print(f'Dia: {data_atual.day}')


# passando argumentos para datetime

my_date = datetime.datetime(2019, 9, 25, 12, 30, 45)
print(f'Data pré definida: {my_date}')
print(f'Data pré definida - Ano : {my_date.year}')
print(f'Data pré definida - Mês : {my_date.month}')
print(f'Data pré definida - Dia : {my_date.day}')
print(f'Data pré definida - Hora : {my_date.hour}')
print(f'Data pré definida - Minuto : {my_date.minute}')
print(f'Data pré definida - Segundo : {my_date.second}')
print()

# limpando data
today = datetime.date.today()
print(f'Today: {today}')
t1 = str(today).split('-')
print(t1)
t2 = ''.join(t1)
print(t2)