#!/usr/bin/env python3

print(3, -1, 3.14159, -2.8) # imprimindo numeros simples

# identificando os tipos de numeros, usando a funcao 'type'
print(type(3))  # int
print(type(-1))  # int
print(type(3.14159))  # float
print(type(-2.8))  # float
print(type(301j))  # complex

# fazendo a conversao entre os tipos
print(int(3.14159)) # converte float em int usando a funcao interna 'int'
print(int(-2.8))
print(float(3)) # converte int em float, usando a funcao interna 'float'