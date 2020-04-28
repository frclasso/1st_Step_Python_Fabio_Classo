import time
print(time.localtime())

t1 = time.localtime()
ano = t1[0]
mes = t1[1]
dia = t1[2]
horas = t1[3]
minutos = t1[4]
segundos = t1[5]

print(f'Data atual: {ano}/{mes}/{dia}, e hora {horas}:{minutos}:{segundos}')