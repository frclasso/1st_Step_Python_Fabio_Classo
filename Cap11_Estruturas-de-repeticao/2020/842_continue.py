#!/usr/bin/python3

for letter in 'Python': # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

print()

var = 10 # Second Example

while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")
