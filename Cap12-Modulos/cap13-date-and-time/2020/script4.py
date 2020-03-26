import datetime


# time retorna tempo sem data
t = datetime.time(9, 30, 45, 100000)
print(t)

dt = datetime.datetime(2016, 7, 26, 9, 30, 45, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
print()
# usando timedelta
dt2 = datetime.datetime.now()
print(dt2)
tdelta = datetime.timedelta(days=7)
print(dt2 + tdelta)

