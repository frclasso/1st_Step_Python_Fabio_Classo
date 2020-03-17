#!/usr/bin/env python3
# -*- coding:utf-8 -*-

amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)

print("Net payable:", amount - discount)

"""
No exemplo acima, o desconto é calculado sobre o valor de entrada.
Taxa de desconto é de 5%,se a quantidade for menor que 1000 e 10% 
se for acima de 10000."""