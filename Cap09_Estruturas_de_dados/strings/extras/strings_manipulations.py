#!/usr/bin/env python3


# Concatenacao
s ='foo'
t = 'bar'
u = 'baz'

print(s + t +u)
print("Go team" + "!!!")

# Criando multiplas copias de uma string

print(s * 4) # o multiplicando tem que ser um numero inteiro e positivo
print(4 * t)
print(u * -8) # reotorna uma string vazia

# Operadores in e not in

print(s in "That's food for thought. ")
print(s in "That's good for now.")

# Funcoes internas (Built in functions)
"""chr() - converte inteiro em caracter
   ord() - converte caracter em inteiro
   len() - retorna o comprimento da string
   str() - retorna a representacao da string em um objeto"""

# Convertendo caracteres em formato ASCII
print("odr() function")
print(ord('a'))  # 97
print(ord('#'))  # 35
print(ord('€'))  # 35
print(ord('∑'))  # 35
print()

print("chr() function")
print(chr(97))
print(chr(35))
print(chr(8364))
print(chr(8721))
print()

print("len()function")
n = "I am a string."
print(len(n))
print()

print("str() function")
print(str(49.2))
print(str(3+4j))
print(str(3+29))
print()

# String Indexing

string = 'foobar'
# print(string[0])
# print(string[1])
# print(string[3])
# print("len:",len(string)) # 6, de 0 a 5

#print(string[6]) # IndexError: string index out of range

# print(string[-1])
# print(string[-2])

# String slicing
print()
print(string[:4] + string[4:])
print(string[:4] + string[4:] == string) # True

''' Omitindo os indices retorna  a string original, nao uma copia mas
 uma referencia a string original'''

s = 'foobar'
t = s[:]
print(id(s))
print(id(t))
print(s is t) # True, mesmo 'id'
print()
# Especificando o pulo do fatiamento
print(s[0:6:2])
print(s[0:6:1])

num = '12345' * 5
print(num)
print(num[::5]) # 11111  do inicio, de cinco em cinco, exclusivo
print(num[4::5]) # 55555  a partir do quarto elemento de cinco em cinco exclusivo

print(s[5:0:-2])  # inicia do ultimo caractere, de dois em dois, nao
                  #   incluindo o primeiro caratere

# Invertendo uma string
minhaString = "If Comrade Napoleon says it, it must be right."
print(minhaString[::-1])
print()

# Usando formating string "f-string"
n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m}  is {prod}.')
print()

var = 'Bark!'
print(f"The Dog say's {var}!")
print()

"""Modificando strings, na verdade strings sao imutaveis
se realmente houver a necessidade de altera-la, o melhor
eh fazer uma copia da string orignal com a devida modificacao."""
# s[3] = 'x'
# print(s) # TypeError: 'str' object does not support item assignment

# s = s[:3] + 'x'+s[4:]
# print(s)  # fooxar

"""No entanto ha um metodo interno(Built-in) para fazer a subsituicao"""
s = 'foobar'
s = s.replace('b', 'x')
print(s) # fooxar

