#!/usr/bin/env python3

print("Quantos animais de estimacao voce tem?")
num = input()
try:
    if int(num) >= 4:
        print("Voce tem animais demais!")
    else:
        print("Voce nao tem animais demais")
except ValueError:
    print("Ops, voce entrou com um valor invalido, digite apenas digitos numericos.")