#!/usr/bin/env python3


people = {1:{'name': 'John', 'age': 27, 'sex': 'Male'},
          2:{'name':'Marie', 'age': 22, 'sex': 'female'},
          3:{'name': 'Luna', 'age': '24', 'sex': 'female', 'married': 'No'}}

people[4] = {'name':'Peter', 'age':29, 'sex':'male', 'married':'Yes'}

print(people[4])