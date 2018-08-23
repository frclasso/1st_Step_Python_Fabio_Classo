#!/usr/bin/env python3

"""Ordering pizza"""

diet_restriction = set(['meat', 'cheese'])

# decide wich pizza to order
# if 'meat' in diet_restriction:
#     print('Geat a cheese pizza.')
# elif 'meat' and 'cheese' in diet_restriction:
#     print('Get a vegan pizza.')
# else:
#     print('Get something else')

# invertendo a ordem
if 'meat' and 'cheese' in diet_restriction:
    print('Get a vegan pizza.')
elif 'meat' in diet_restriction:
    print('Geat a cheese pizza.')
else:
    print('Get something else')
