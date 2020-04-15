
# chaves
# name, industry, sector, headquarters, founded, notes
chaves = ['name', 'industry', 'sector', 'headquarters', 'founded', 'notes']

#valores
audi = ['Audi','Consumer goods','Automobiles','Ingolstadt',1910,
        'Auto manufacturer, part of Volkswagen Group']

# nome = chaves[0]
# nome_v = audi[0]
#
# audi_dicionario = {}
# audi_dicionario[nome] = nome_v
#
# for k in chaves:
#     print(k)
# for v in audi:
#     print(v)

audi_dicionario_new = {}
for k, v in zip(chaves, audi):
    audi_dicionario_new[k] = v

for k,v in audi_dicionario_new.items():
    print(k, v)
print()
print()
print()
germany_companies = [

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
    ['August Storck','Consumer goods','Food products','Berlin',1903,'Confectionery']]


new_germany_companies = []

company_dict = {}
for company in germany_companies:
    for k, v in zip(chaves, company):
        company_dict[k] = v
    print(company_dict)
print()

