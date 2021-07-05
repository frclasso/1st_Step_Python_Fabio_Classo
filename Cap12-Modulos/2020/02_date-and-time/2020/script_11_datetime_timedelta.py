import datetime

# usando timedelta
dt2 = datetime.datetime.now()
print(f'Hoje e agora: {dt2}')
tdelta = datetime.timedelta(days=7)
print(f'Data daqui 7 dias: {dt2 + tdelta}')
print()

# sutação do D-1
hoje = datetime.datetime.now()
print(f'Hoje: {hoje}')
delta = datetime.timedelta(days=1)
d1 = hoje-delta
print(f'D-1: {d1.date()}')



# Calculating future times
from datetime import datetime, timedelta
now = datetime.now()

twoDays = now + timedelta(days=2)

treeWeeksAgo = now - timedelta(weeks=3)

print(f'Daqui a dois dias:{twoDays.date()}')

print(f"Tree weeks ago: {treeWeeksAgo.date()}")

print()