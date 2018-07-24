#!/usr/bin/env python3

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'courge']
a[2:2] = [1,2,3]
a += [3.14159]
print(a)

# removendo itens
a[2:3] = [] # '1'
del a[0] # 'foo'
print(a)