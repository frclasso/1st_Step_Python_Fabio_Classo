#!/usr/bin/env python3

"""Built-in String Methods"""

"""s.capitalize() , Os métodos nesse grupo executam a conversão de
 maiúsculas e minúsculas na cadeia de destino."""

s = 'foO BaR BAZ quX'
print(s.capitalize())

s = 'foo123#BAR#'
print(s.capitalize())
print()

# s.lower(), converte em minuscula uma cadeia de caracteres
print('Foo Bar 123 baz Qux'.lower())
print()

# s.swapcase(), inverte os caracteres
print('Foo Bar 123 baz Qux'.swapcase())
print()

#s.title(), retorna  a primeira letra de cada palavre em maiusculo.
print('the sun also  rises'.title())
print()

# s.upper(), converte caracteres alfabeticos em maiusculo.
print('foo bar 123 quX'.upper())
print()

# s.count(<sub>[,<start>[,<end>]]) , conta a ocorrencia de uma substring em uma string alvo.
print('foo goo moo'.count('oo'))
print('foo goo moo'.count('oo', 0, 8))
print()

#s.endswith(<sufix>[,<start>[,<end>]]), determina se a string termina
                   # com a substring fornecida
print('foobar'.endswith('bar'))
print('foobar'.endswith('baz'))
print('foobar'.endswith('oob', 0, 4))
print('foobar'.endswith('oob', 2, 4))

# s.find(<sub>[,<start>[,<end>]]), busca na string alvo a substring fornecida
print('foo bar 123 quX'.find('foo')) # retorna a posicao quando encontra a substring
print('foo bar 123 quX'.find('bar'))
print('foo bar 123 quX'.find('grault')) # -1, False, quando nao encontra
print()


