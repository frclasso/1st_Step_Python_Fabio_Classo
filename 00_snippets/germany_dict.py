germany_compamies = {
    'lange':{'name': 'A. Lange & Söhne', 'industry': 'Consumer goods', 'sector': 'Clothing & accessories', 'headquarters': 'Glashütte', 'founded': 1845, 'notes': 'Watches', 'qtd_funcionarios': '150.000'},
    'aareal':{'name': 'Aareal Bank', 'industry': 'Financials', 'sector': 'Banks', 'headquarters': 'Wiesbaden', 'founded': 1922, 'notes': 'Banking and financial services', 'qtd_funcionarios': '150.000'},
    'adidas':{'name': 'Adidas', 'industry': 'Consumer goods', 'sector': 'Footwear', 'headquarters': 'Herzogenaurach', 'founded': 1924, 'notes': 'Shoes, apparel and accessories', 'qtd_funcionarios': '150.000'},
    'aeg':{'name': 'AEG', 'industry': 'Industrials', 'sector': 'Electronic equipment', 'headquarters': 'Frankfurt', 'founded': 1883, 'notes': 'Defunct 1996 - now part of Electrolux', 'qtd_funcionarios': '150.000'},
    'air_berlin':{'name': 'Air Berlin', 'industry': 'Consumer services', 'sector': 'Airlines', 'headquarters': 'Berlin', 'founded': 1979, 'notes': 'Airline, defunct 2017', 'qtd_funcionarios': '150.000'},
    'aldi':{'name': 'Aldi', 'industry': 'Consumer services', 'sector': 'Food retailers & wholesalers', 'headquarters': 'Essen', 'founded': 1913, 'notes': 'Discount retail chains', 'qtd_funcionarios': '150.000'},
    'allianz':{'name': 'Allianz', 'industry': 'Financials', 'sector': 'Full line insurance', 'headquarters': 'Munich', 'founded': 1890, 'notes': 'Insurance and asset management', 'qtd_funcionarios': '150.000'},
    'alpina':{'name': 'Alpina', 'industry': 'Consumer goods', 'sector': 'Automobiles', 'headquarters': 'Buchloe', 'founded': 1965, 'notes': 'Automotive manufacturer', 'qtd_funcionarios': '150.000'},
    'altana':{'name': 'Altana', 'industry': 'Basic materials', 'sector': 'Speciality chemicals', 'headquarters': 'Wesel', 'founded': 1977, 'notes': 'Chemicals', 'qtd_funcionarios': '150.000'},
    'aral':{'name': 'Aral AG', 'industry': 'Consumer services', 'sector': 'Specialty retailers', 'headquarters': 'Bochum', 'founded': 1898, 'notes': 'Part of BP', 'qtd_funcionarios': '150.000'},
    'arburg':{'name': 'Arburg', 'industry': 'Industrials', 'sector': 'Industrial machinery', 'headquarters': 'Loßburg', 'founded': 1923, 'notes': 'Machinery and injection molding', 'qtd_funcionarios': '150.000'},
    'arcandor':{'name': 'Arcandor', 'industry': 'Consumer services', 'sector': 'Broadline retailers', 'headquarters': 'Essen', 'founded': 1999, 'notes': 'Defunct 2009', 'qtd_funcionarios': '150.000'},
    'arcor':{'name': 'Arcor', 'industry': 'Telecommunications', 'sector': 'Fixed line telecommunications', 'headquarters': 'Eschborn', 'founded': 1966, 'notes': 'Telecom, part of Vodafone (UK)', 'qtd_funcionarios': '150.000'},
    'armedangles':{'name': 'Armedangels', 'industry': 'Consumer goods', 'sector': 'Clothing & accessories', 'headquarters': 'Cologne', 'founded': 2007, 'notes': 'Fashion', 'qtd_funcionarios': '150.000'},
    'audi':{'name': 'Audi', 'industry': 'Consumer goods', 'sector': 'Automobiles', 'headquarters': 'Ingolstadt', 'founded': 1910, 'notes': 'Auto manufacturer, part of Volkswagen Group', 'qtd_funcionarios': '150.000'},
    'august_storck':{'name': 'August Storck', 'industry': 'Consumer goods', 'sector': 'Food products', 'headquarters': 'Berlin', 'founded': 1903, 'notes': 'Confectionery', 'qtd_funcionarios': '150.000'}
    }


# conveter de dicionario para lista
print(germany_compamies['lange'])
print(germany_compamies['lange'].values())
l1 = germany_compamies['lange'].values()
print(type(l1))
l2 = list(l1)
print(l2)