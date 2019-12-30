#!/usr/bin/env python3

"""
O método time () retorna a hora como um número de ponto flutuante expresso em segundos desde
a época, em UTC.

Sintaxe: time.time()
"""

import time

print('time.time():  %f' % time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))  # mais usado
