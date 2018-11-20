#!/usr/bin/env python3

"""O método sleep () suspende a execução pelo número de segundos especificado. O
argumento pode ser um número de ponto flutuante para indicar um tempo de sleep
mais preciso.

Sintaxe:time.sleep(t)
"""

import time

print("Start:  %s" % time.ctime())

time.sleep(3)
print("End:  %s" % time.ctime())