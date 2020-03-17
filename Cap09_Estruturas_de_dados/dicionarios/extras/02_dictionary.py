#!/usr/bin/env python3

"""A rolodex of friends"""
rolodex = {
    'Aaron':5556069,
    'Bill':5559824,
    'Dad':5552603,
    'David':5558381,
    'Dillon':5553538,
    'Jim':5555547,
    'Mom':5552603,
    'Olivia':5556397,
    'Verne':5555309
}
#
# print(rolodex["Verne"])
# print(hash('Verne'))

# Adding new person
rolodex['Amanda'] = 5559988
#print(rolodex['Amanda'])

rolodex['David'] = (5558381, 5558866)
#print(rolodex['David'])


def caller_id(lookup_number):
    for name, num in rolodex.items():
        if num == lookup_number:
            return name

print(caller_id(5559988))
print(caller_id(5552603))