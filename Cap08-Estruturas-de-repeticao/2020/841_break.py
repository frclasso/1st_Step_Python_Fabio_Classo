#!/usr/bin/python3

all_companies = ['Jaguar', 'Tesla', 'Porsche', 'Ferrari', 'Audi', 'Jeep', 'Ford']

for company in all_companies:
    if company == 'Audi':
        continue
    print('Company name:', company)

print()
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

print()
var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!")
