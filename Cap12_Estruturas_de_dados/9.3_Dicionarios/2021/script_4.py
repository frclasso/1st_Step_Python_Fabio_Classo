# COPY
# Python program to demonstrate difference
# between = and copy()
original = {
    'id': 1001, 
    'name':'Fabio'
    }
  
# copying using copy() function
new = original.copy()
print(f'Original: {original}')
print(f'New: {new}')

