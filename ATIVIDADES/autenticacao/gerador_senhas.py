# desenvolver um app q gera senha

import random

minusculas = 'abcdefghijklmnopqrstuwyvxz'
maiusculas = minusculas.upper()
simbolos = '!@#$%*(){}[]+-=/\|;:,'
numeros = '0123456789'

#print(maiusculas)
#print(numeros)


caracteres = minusculas + maiusculas + simbolos + numeros
print(len(caracteres))

senha = random.sample(caracteres, 32)
senha_final = ''.join(senha)
print(f'Sua senha foi gerada com sucesso: {senha_final}')