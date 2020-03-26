#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print(format(a, '08b'))
print(format(b, '08b'))


print('a AND B => ',a & b,'binario => ', format(a & b, '08b'))
print('a OR B => ', a | b,'binario => ', format(a | b, '08b'))
print('a XOR B => ',a ^ b,'binario => ', format(a ^ b, '08b'))
print('Complemento de a = >',~a,'binario = >', format(~a, '09b'))
print('Deslocamento para esquerda a << 2', a << 2, 'binario', format(a << 2, '08b'))
print('Deslocamento para direita a >> 2', a << 2, 'binario', format(a >> 2, '08b'))


print()

