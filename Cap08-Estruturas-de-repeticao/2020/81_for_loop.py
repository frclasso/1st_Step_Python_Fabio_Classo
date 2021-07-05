#!/usr/bin/env python3

all_companies = ['Toyota', 'Audi', 'BMW','Lexus', 'Jeep', 'Honda','Kia', 'Mazda']

for company in all_companies:
    print(company)


about_jeep = 'Jeep é uma marca atualmente em nome da FCA US LLC. O termo jipe virou sinônimo ' \
             'de automóveis destinados ao uso fora de estrada, ou off road, normalmente ' \
             'com tração nas quatro rodas.'

for company in all_companies:
    if company == 'Jeep':
        print(about_jeep)
    else:
        pass

