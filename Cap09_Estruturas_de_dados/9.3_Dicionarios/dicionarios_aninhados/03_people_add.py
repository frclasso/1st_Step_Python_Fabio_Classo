#!/usr/bin/env python3


people = {1:{'name': 'John', 'age': 27, 'sex': 'Male'},
          2:{'name':'Marie', 'age': 22, 'sex': 'female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'female'
people[3]['married'] = 'No'

print(people[3])