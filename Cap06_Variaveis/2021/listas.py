fruits_stores = [
    ["Pete’s Discount fruit", "Banana", 1, 0.23],
    ["Derek’s Fruit Stand", "Banana", 3, 0.69],
    ["Pete’s Discount fruit", "Orange", 1, 0.68],
    ["Derek’s Fruit Stand", "Orange", 2, 1.36],
    ["Pete’s Discount fruit", "Apple", 1, 0.88],
    ["Derek’s Fruit Stand", "Apple", 1, 0.88],
    ["Derek’s Fruit Stand", "Plum", 1, 0.69],
    ["Derek’s Fruit Stand", "Plum", 2, 1.92],
    ["Derek’s Fruit Stand", "Kiwi", 2, 2.24],
    ["Derek’s Fruit Stand", "Watermelon", 1, 3.98],
    ["Pete’s Discount fruit", "Blueberries", 3, 15.48],
    ["Derek’s Fruit Stand", "Dragon Fruit", 3, 15.81],
    ["Pete’s Discount fruit", "Banana", 1, 0.23],
    ["Derek’s Fruit Stand", "Banana", 1, 0.23],
    ["Pete’s Discount fruit", "Apple", 3, 2.64],
    ["Pete’s Discount fruit", "Plum", 2, 1.92],
    ["Pete’s Discount fruit", "Plum", 2, 1.92],
    ["Pete’s Discount fruit", "Plum", 2, 1.92],
]

germany_companies = [

    'A. Lange & Söhne', 'Consumer goods','Clothing & accessories','Glashütte',1845, ' 	Watches',
    'Aareal Bank','Financials','Banks','Wiesbaden',1922,'Banking and financial services',
    'Adidas','Consumer goods','Footwear','Herzogenaurach',1924,'Shoes, apparel and accessories',
    'AEG','Industrials','Electronic equipment','Frankfurt',1883, 'Defunct 1996 - now part of Electrolux',
    'Air Berlin','Consumer services','Airlines','Berlin', 1979,'Airline, defunct 2017',
    'Aldi','Consumer services','Food retailers & wholesalers','Essen',1913,'Discount retail chains',
    'Allianz','Financials','Full line insurance','Munich',1890,'Insurance and asset management',
    'Alpina','Consumer goods','Automobiles','Buchloe',1965,'Automotive manufacturer',
    'Altana','Basic materials','Speciality chemicals','Wesel',1977, 'Chemicals',
    'Aral AG','Consumer services','Specialty retailers','Bochum',1898,'Part of BP',
    'Arburg','Industrials','Industrial machinery','Loßburg',1923,'Machinery and injection molding',
    'Arcandor','Consumer services','Broadline retailers','Essen',1999,'Defunct 2009',
    'Arcor','Telecommunications','Fixed line telecommunications','Eschborn',1966,'Telecom, part of Vodafone (UK)',
    'Armedangels','Consumer goods','Clothing & accessories','Cologne',2007,'Fashion',
    'Audi','Consumer goods','Automobiles','Ingolstadt',1910,'Auto manufacturer, part of Volkswagen Group',
    'August Storck','Consumer goods','Food products','Berlin',1903,'Confectionery',
    'Aurubis','Basic materials','Nonferrous metals']

    germany_companies_2 = [

    ['A. Lange & Söhne', 'Consumer goods','Clothing & accessories','Glashütte',1845,'Watches'],
    ['Aareal Bank','Financials','Banks','Wiesbaden',1922,'Banking and financial services'],
    ['Adidas','Consumer goods','Footwear','Herzogenaurach',1924,'Shoes, apparel and accessories'],
    ['AEG','Industrials','Electronic equipment','Frankfurt',1883, 'Defunct 1996 - now part of Electrolux'],
    ['Air Berlin','Consumer services','Airlines','Berlin', 1979,'Airline, defunct 2017'],
    ['Aldi','Consumer services','Food retailers & wholesalers','Essen',1913,'Discount retail chains'],
    ['Allianz','Financials','Full line insurance','Munich',1890,'Insurance and asset management'],
    ['Alpina','Consumer goods','Automobiles','Buchloe',1965,'Automotive manufacturer'],
    ['Altana','Basic materials','Speciality chemicals','Wesel',1977, 'Chemicals'],
    ['Aral AG','Consumer services','Specialty retailers','Bochum',1898,'Part of BP'],
    ['Arburg','Industrials','Industrial machinery','Loßburg',1923,'Machinery and injection molding'],
    ['Arcandor','Consumer services','Broadline retailers','Essen',1999,'Defunct 2009'],
    ['Arcor','Telecommunications','Fixed line telecommunications','Eschborn',1966,'Telecom, part of Vodafone (UK)'],
    ['Armedangels','Consumer goods','Clothing & accessories','Cologne',2007,'Fashion'],
    ['Audi','Consumer goods','Automobiles','Ingolstadt',1910,'Auto manufacturer, part of Volkswagen Group'],
    ['August Storck','Consumer goods','Food products','Berlin',1903,'Confectionery']
]



print(type(germany_companies))
print(germany_companies)
print(germany_companies[0])
print(germany_companies[1])


print(type(germany_companies_2))
print(germany_companies_2)
print(germany_companies_2[0])
print(germany_companies_2[-2]) # indexei

audi = germany_companies_2[-2]
print(audi)
# name, industry, sector, headquarters, founded, notes
name = audi[0]
print(name)
industry = audi[1]
sector = audi[2]
headquarters = audi[3]
founded = audi[4]
notes = audi[5]

print()
print('A {} é {} do setor {} localizada em {} e fundada em {}, info: {}'.format(name, industry, sector, headquarters, founded,notes))
print(f'A {name} é {industry} do setor {sector} localizada em {headquarters} e fundada em {founded}, info: {notes}')