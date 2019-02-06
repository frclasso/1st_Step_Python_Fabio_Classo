#!/usr/bin/env python3

"""Desenvolver uma ferramenta de criptografia
"""
str = ''''Lorem Ipsum is simply dummy text of the printing and typesetting 
industry. Lorem Ipsum has been the industry's standard dummy text ever 
since the 1500s, when an unknown printer took a galley of type and scrambled
 it to make a type specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of Letraset
 sheets containing Lorem Ipsum passages, and more recently with desktop 
 publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

# replace
for ch in str:
    if ch == 'a':
        str = str.replace('a', '@')
    elif ch == 'e':
        str = str.replace('e', '3')
    elif ch == 'i':
        str = str.replace('i', '1')
    elif ch == 'm':
        str = str.replace('m', '#')

#print(str)

# modulos cap 15
f = open('cripto.txt', 'w')  # nome do arquivo e modo de abertura, w = 'write'
f.write(str)
f.close()