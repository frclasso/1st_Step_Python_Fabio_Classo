#!/usr/bin/env python3

"""
O método strptime () analisa uma string representando um tempo de acordo com um formato. o
valor de retorno é um struct_time conforme retornado por gmtime () ou localtime ().
Sintaxe: time.strptime(string[, format])
"""

import time

struct_time = time.strptime("30 12 2015", "%d %m %Y")
print("tuple: ", struct_time)