import datetime
import pytz

#dt = datetime.datetime(2016, 7, 27, 12, 30, 45)
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

#dt_now = datetime.datetime.now()
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

#dt_utcnow = datetime.datetime.utcnow()
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)



"""
https://pt.wikipedia.org/wiki/Tempo_Universal_Coordenado
https://time.is/pt_br/UTC

"""

# Imprimindo nosso datetime UTC
dt_br = dt_utcnow.astimezone(pytz.timezone('America/Sao_Paulo'))
#print(dt_br)

for tz in pytz.all_timezones:
    print(tz)