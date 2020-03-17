#!/usr/bin/env python3

"""Essas funções são chamadas anônimas porque não são declaradas de maneira
padrão usando a palavra-chave def . Você pode usar a palavra-chave lambda para
criar pequenas funções anônimas.

Sintaxe: lambda [arg1 [,arg2,.....argn]]:expression
Ex: sum = lambda arg1, arg2: arg1+ arg2
"""
# definicao da funcao
sum =lambda arg1, arg2 : arg1 + arg2

# Chamando a funcao
print("value of total: ", sum(10, 20))
print("value of total: ", sum(20, 20))