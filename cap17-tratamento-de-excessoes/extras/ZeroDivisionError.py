#!/usr/bin/env python3


def div42por(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print("Erro: Numero nao pode ser dividido por zero")

print(div42por(2))
print(div42por(12))
print(div42por(0))
print(div42por(1))