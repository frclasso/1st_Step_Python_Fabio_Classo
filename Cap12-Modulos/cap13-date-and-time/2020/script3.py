import datetime

# 1
hoje = datetime.date.today()
time_delta  = datetime.timedelta(days=7)
#print('Daqui há 7 dias {}'.format(hoje + time_delta))

# 2
# Calcular quantos dias se passaram entre duas datas
meu_aniversario = datetime.date(2019, 11, 25)

qto_dias = meu_aniversario - hoje
#print(qto_dias.days)
print(f'Passaram-se {abs(qto_dias.days)} dias desde meu ultimo aniversario.')