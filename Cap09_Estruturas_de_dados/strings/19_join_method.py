#!/usr/bin/python3


"""Description
The join() method returns a string in which the string elements of sequence have been
joined by str separator.

Syntax
str.join(sequence)
"""
s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print(s.join(seq))
print()

print(', '.join(['foo', 'bar','baz', 'qux']))
print()

# Quando uma string e iterada, eh interpretada como uma lista de caracteres
print(list('corge'))
print(':'.join('corge'))
print()

# No entanto, caso um dos elementos nao seja uma string, gera um erro
#print(','.join(['foo', 23, 'bar'])) # TypeError: sequence item 1: expected str instance, int found

# Podemos consertar da seguinte maneira
print(','.join(['foo', str(23), 'bar']))
