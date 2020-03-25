#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a = 20
b = 20
c = a

print(f"O valor de  'a' é : {a} e seu ID: {id(a)}")
print(f"O valor de  'b' é : {b} e seu ID: {id(b)}")
print(f"O valor de  'c' é : {c} e seu ID: {id(c)}")

print(a == b)
print(a is b)
print()
print(a == c)
print(a is c)
print()
print(b == c)
print(b is c)
print()

print()

a = 21
print(f"O valor de  'a' é : {a} e seu ID: {id(a)}")
print(f"O valor de  'b' é : {b} e seu ID: {id(b)}")
print(f"O valor de  'c' é : {c} e seu ID: {id(c)}")
print(a == b)
print(a is b)
print()
print(a == c)
print(a is c)
print()
print(b == c)
print(b is c)
print()

b = 30
print(f"O valor de  'a' é : {a} e seu ID: {id(a)}")
print(f"O valor de  'b' é : {b} e seu ID: {id(b)}")
print(f"O valor de  'c' é : {c} e seu ID: {id(c)}")
print(a == b)
print(a is b)
print()
print(a == c)
print(a is c)
print()
print(b == c)
print(b is c)
print()
print("Associação multipla:")
d= e = f = 10
print(d is e)
print(d is f)
d = 11
print(d)
print(e)
print(f)
print(d is e)
print(d is f)
