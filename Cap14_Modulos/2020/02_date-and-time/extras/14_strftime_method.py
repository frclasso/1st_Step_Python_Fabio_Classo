#!/usr/bin/env python3

"""O método strftime () converte uma tupla ou struct_time representando uma hora
como retornada por gmtime () ou localtime () para uma string especificada pelo
argumento format.

Sintaxe: time.strftime(format[, t])
"""

import time

t=(2015, 12, 31, 10, 39,45, 1, 48, 0)
t= time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.localtime(t)))
