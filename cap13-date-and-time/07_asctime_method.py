#!/usr/bin/env python3

"""O método asctime () converte uma tupla ou struct_time representando uma hora
como retornada por gmtime () ou localtime () para uma cadeia de 24 caracteres da
seguinte forma: 'Ter 17 de fev 23:21:05 2009 '.

Sintaxe: time.asctime([t]))
"""

import time

t = time.localtime()
print("asctime: ", time.asctime(t))