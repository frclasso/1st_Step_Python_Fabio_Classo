#!/usr/bin/env python3

"""O método index () retorna o índice mais baixo na lista que obj aparece.
    Sintaxe: list.index(obj)
"""

list1 = ['Physics', 'Chemistry', 'Maths']
print('Index of chemistry: ', list1.index('Chemistry'))

# o codigo a seguir retorna um erro
# ValueError: 'C#' is not in list
# print('Index of C#: ', list1.index('C#'))