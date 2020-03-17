import datetime


today = datetime.date.today()
print(today)
t1 = str(today).split('-')
t2 = ''.join(t1)
print(t2)
ano = t2[:4]
mes = t2[4:6]
dia = t2[6:8]
print(ano)
print(mes)
print(dia)