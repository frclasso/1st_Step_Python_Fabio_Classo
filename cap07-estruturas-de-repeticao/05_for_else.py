#!/usr/bin/python3

numbers=[11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num % 2 == 0:
        print('the list CONTAINS an even number')
        break
else:
    print('the list DOES NOT contain even number')