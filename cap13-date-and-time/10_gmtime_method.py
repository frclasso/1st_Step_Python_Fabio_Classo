#!/usr/bin/env python3

"""O método gmtime () converte um tempo expresso em segundos desde a época até
um struct_time em UTC em que o sinalizador dst é sempre zero. Se secs não for
fornecido ou None, a hora atual retornada por time () é usada.

Sintaxe: time.gmtime([ sec ])
"""

import time

print("gmtime: ", time.gmtime(1455508609.34375))