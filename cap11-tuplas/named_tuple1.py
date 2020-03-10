#!/usr/bin/env python3

from collections import namedtuple


Person = namedtuple('Person', 'first_name last_name zip_code')
p1 = Person('Fabio', 'Classo', '88034350')
# print(p1.first_name)
# print(p1.last_name)
# print(p1.zip_code)
# print(len(p1))
print('Nome: {}, sobrenome:{} e codigo postal:{}'.format(p1.first_name,p1.last_name, p1.zip_code))
print(p1._fields)
print(p1._replace(zip_code='88035350'))
print('Nome: {}, sobrenome:{} e codigo postal:{}'.format(p1.first_name,p1.last_name, p1.zip_code))
p2 = p1._replace(zip_code='000000')
print(p2)
print('Nome: {}, sobrenome:{} e codigo postal:{}'.format(p2.first_name,p2.last_name, p2.zip_code))
print(p2._asdict())

# print(p1[0])
# print(p1[1])
