#!/usr/bin/env python3

"""O método ctime () converte um tempo expresso em segundos desde época até uma
string representando a hora local. Se secs não for fornecido ou None, a hora atual
retornada por time () é usada. Esta função é equivalente a asctime (localtime (secs)).
Informações de localidade não é usado pelo ctime ().

Sintaxe:time.ctime([ sec ])
"""

import time

print("ctime: ", time.ctime())