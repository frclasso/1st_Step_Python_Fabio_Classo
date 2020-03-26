#!/usr/bin/python3

numbers=[11,33,55,39,55,75,37,21,23,41,13]

for n in numbers:
    if n % 2 == 0:
        print('Esse numero número par: {}'.format(n))
        break
    else:
        print('Esse numero  NAO  eh par: {}'.format(n))
