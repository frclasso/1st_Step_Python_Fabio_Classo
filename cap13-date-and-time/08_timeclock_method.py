#!/usr/bin/env python3

"""O método clock () retorna a hora atual do processador como um número de ponto
flutuante expresso em segundos no Unix. A precisão depende da função C do mesmo
nome, mas em qualquer caso, essa é a função a ser usada para o benchmarking
Python.

Sintaxe: time.clock()
"""
import time


def procedure():
    time.sleep(2.5)

# measure process time


t0 = time.clock()

procedure()
print(time.clock() - t0,'seconds process time')


# measure wall time
t0 = time.time()
procedure()
print(time.time() - t0, "seconds wall time")
