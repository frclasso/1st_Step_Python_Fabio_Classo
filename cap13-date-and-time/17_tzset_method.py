#!/usr/bin/env python3

"""O método tzset () redefine as regras de conversão de tempo usadas pelas rotinas
da biblioteca. A variável de ambiente TZ especifica como isso é feito.

Sintaxe: time.tzset()"""

import time
import os

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))