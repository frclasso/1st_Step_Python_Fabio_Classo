#!/usr/bin/env python3

# exibindo o tamanho da tupla utilizando a funcao len()
tup1 = (1,2,3,4)
print(len(tup1))

# Concatenacao
tup2 = (5,6,7,8,9)
print(tup1+tup2)

# Repeticao
tup3=('Hi!',)*4
print(tup3)

# Verifica se eh membro (Membership operation)
print(3 in tup1)

# Iteracao
for x in tup1:print(x, end=', ')