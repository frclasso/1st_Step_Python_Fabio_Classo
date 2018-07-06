#!/usr/bin/env python3

"""O método mktime () é a função inversa do localtime (). Seu argumento é o
struct_time e retorna um número de ponto flutuante, para compatibilidade com time ().

Sintaxe:time.mktime(t)"""

import time

t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)

d = time.mktime(t)
print('time.mktime(): %f' % d)
print('asctime(localtime(secs)): %s' % time.asctime(time.localtime(d)))