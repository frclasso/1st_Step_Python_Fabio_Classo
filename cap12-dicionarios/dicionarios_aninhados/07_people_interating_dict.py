#!/usr/bin/env python3

# Deletando um dicionário aninhado

people = {1:{'name': 'John', 'age': 27, 'sex': 'Male'},
          2:{'name':'Marie', 'age': 22, 'sex': 'female'},
          3:{'name': 'Luna', 'age': '24', 'sex': 'female', 'married': 'No'},
          4:{'name': 'Peter', 'age': 29, 'sex': 'male', 'married': 'Yes'}}

for p_id, p_info in people.items():
    print("\nPerson Id:", p_id)

    for key in p_info:
        print(key + ':' , p_info[key])