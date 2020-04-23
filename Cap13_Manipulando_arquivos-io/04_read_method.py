#!/usr/bin/env python3

# Abrindo o arquivo
fo =open('foo.txt', 'r+')
str = fo.read(28)  # Altere esse valor
print("Read String is: ", str)

# Fechando
fo.close()