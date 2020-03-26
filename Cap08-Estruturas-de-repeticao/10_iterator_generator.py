#!usr/bin/python3
import sys

lista = [1,2,3,4]

it = iter(lista) # this builds an iterator object

print(next(it)) #prints next available element in iterator
#Iterator object can be traversed using regular for statement
#
for x in it:
    print (x, end=" ")

#or using next() function
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit() #you have to import sys module for this
