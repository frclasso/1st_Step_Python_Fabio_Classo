#!/usr/bin/env python3

"""Quado tentamos acessar um valor de uma variavel local antes de defini-la (setting)
obtemos como resultado o erro UnboundLocalError"""

money = 2000


def AddMoney():
    # descomente  a linha abaixo para corrigir o problema
    #global money
    money = money + 1

print(money)

AddMoney()
print(money)