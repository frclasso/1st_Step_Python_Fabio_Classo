#!/usr/bin/env python3

# in and not in operators
b = b'abcde'

print(b'cd' in b)
print(b'foo' not in b)

print()

# Concatenacao e replicacao
print(b + b'fghi')
print(b * 3)
print()

# Indice e fatias
print(b[2])
print(b[1:3])
print()

# Built-in functions
print(len(b))
print(min(b))
print(max(b))
print()

# Varios metodos de string soa vlidos para bytes objects

b = b'foo bar foo baz foo qux'
print(b.count(b'foo'))
print(b.endswith(b'qux'))
print(b.find(b'baz'))
print(b.split(sep=b','))
print(b.center(30, b'-'))

# Representacao em ASCII
b =b'foo\xddbar'
print(b[3])
print(hex(b[3]))
print(min(b))
print(max(b))
print()

print(b[2:3])
print(list(b))
print()

# Hexadecimal
b = bytes.fromhex(' aa 68 4682cc ')
print(b)
print(list(b))
print()

print(b.hex())
print(type(b.hex()))
print()

# Bytearray objects, eh um outro tipo de sequencia de bytes

ba = bytearray('foo.bar.baz', 'utf-8')
print(ba)
print(bytearray(6))
print(bytearray([100,102,104,106,108]))
print()

# Bytearrays sao mutaveis
ba[5] = 0xee
print(ba)

ba[8:11] = b'qux'
print(ba)

ba = bytearray(b'foo')
print(ba)