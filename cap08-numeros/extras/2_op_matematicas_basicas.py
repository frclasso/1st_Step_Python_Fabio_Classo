#!/usr/bin/env python3

# Usando o Python como calculadora

"""Operacoes matematicas:

+ adicao
- subtracao
* multiplicacao
/ divisao
// divisao exata
% modulo (resto da divisao)

"""

print("Adicao:",1 + 2)
print("Subtracao: ",3 - 4)
print("Multiplicacao:",5 * 6)
print("Potenciacao: ", 2 ** 5)
print("Divisao: ",10/3)
print("Divisao exata: ",10//3)
print("Modulo ou resto da divisao: ",10 % 3)

# Atencao para a precendencia das operacoes, sao as mesmas vistas na matematica
# Ex:

print(1 * 2 + 3 * 4)  # a multiplicacao ocerre antes da soma, resultando em 14
print(1 *(2 + 3) * 4)  # a operacao dentro dos parenteses ocorre antes, resultando em 20