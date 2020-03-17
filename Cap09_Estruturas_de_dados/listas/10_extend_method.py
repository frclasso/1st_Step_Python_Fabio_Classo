#!/usr/bin/env python3

"""O método extend () acrescenta o conteúdo de seq a lista.
    Sintaxe: list.extend(seq)
"""
list1 = ['Physics', 'Chemistry','Maths' ]
list2 = list(range(5))
list1.extend(list2)
print('Extended list: ', list1)