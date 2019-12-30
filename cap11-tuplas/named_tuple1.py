#!/usr/bin/env python3

from collections import namedtuple


Person = namedtuple('Person', 'first_name last_name zip_code')
p1 = Person('Joe', 'Lacey', '93002')
print(p1.first_name)
print(p1.last_name)
print(p1.zip_code)
print(len(p1))