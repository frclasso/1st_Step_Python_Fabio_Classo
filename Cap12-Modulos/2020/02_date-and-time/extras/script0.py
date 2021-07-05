import datetime

d = datetime.date(2016, 7, 25)
print(d)
data_atual = datetime.date.today()
print(data_atual)
print(data_atual.year)
print(data_atual.month)
print(data_atual.day)
print()
# dia da semana (weekday)
print(data_atual.weekday()) # Monday 0
print(data_atual.isoweekday()) # Monday 1
# Descomente a linha abaixo para corrigir  o problema
