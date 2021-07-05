# CASO1
germany_companies_1 = [

    'A. Lange & Söhne', 'Consumer goods',' 	Clothing & accessories','Glashütte',1845, ' 	Watches',
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


#CASO2
germany_companie_2= [

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



""" converter o os snipets em dicionarios"""

# Caso 2
# EXPLICACAO

chaves = ['name', 'industry', 'sector', 'headquarters', 'founded', 'notes']

company_to_dict = {}
company = germany_companie_2[0]
print(company)
for k,v in zip(chaves, company):
    #print(k,v)
    company_to_dict[k] = v

print(company_to_dict)
print()

# RESOLUCAO
count = 0
germany_companie_2_to_dict = []
while count < len(germany_companie_2):
    company_to_dict = {}
    company = germany_companie_2[count]
    for k,v in zip(chaves, company):
        company_to_dict[k] = v
    germany_companie_2_to_dict.append(company_to_dict)
    count += 1

# CONFERINDO
for companies in germany_companie_2_to_dict:
    print(companies)

print()
print()



"""2) ADICIONAR UM NOVA COLUNA QUANTIDADE DE FUNCIONARIOS"""

# caso 2

# EXPLICACAO

# print(germany_companie_2[0])
# germany_companie_2[0].append('130.000')
# print(germany_companie_2[0])


"""RESOLUCAO - Usando um loop for"""
qtd_de_funcionarios = '150.000'

# Usando um loop for

# for company in germany_companie_2:
#     # print(company)
#     # print(type(company))
#     company.append(qtd_de_funcionarios)

# CONFERINDO
# for company in germany_companie_2:
#     print(company)


"""RESOLUCAO 2 - Usando um loop while"""

# count = 0
# while count < len(germany_companie_2):
#     #print(germany_companie_2[count])
#     # print(type(germany_companie_2[count]))
#     germany_companie_2[count].append(qtd_de_funcionarios)
#     count += 1
#
# # verificando
# count = 0
# while count < len(germany_companie_2):
#     print(germany_companie_2[count])
#     count +=1








# caso 1

# print(germany_companies_1[:6])
# l = germany_companies_1[:6]
# # print(type(l))
# l2 = germany_companies_1[6:12]
# print(l2)

## RESOLVENDO O PROBLEMA DO INTEIRO NO MEIO DA STRING
# germany_companies_1_lista_string = []
# for data in germany_companies_1:
#     germany_companies_1_lista_string.append(str(data))
#print(germany_companies_1_lista_string)




# def get_um_linha(count, max):
#     count = 0
#     while count < max:
#         #print(germany_companies_1[count])
#         # company = germany_companies_1[count]
#         company_list = []
#         company = germany_companies_1[count]
#         company_list.append(company)
#         print(company_list)
#         count +=1
# print()


# get_um_linha(0, 6)
# get_um_linha(6, 12)
# # get_um_linha(12, 18)
# # get_um_linha(18, 24)
# # get_um_linha(24, 30)
# # get_um_linha(30, 36)
# # get_um_linha(36, 42)
# # get_um_linha(42, 48)
# # get_um_linha(48, 54)





# funcao, reutilizar codigo
# def get_um_linha(count, max):
#     while count < max:
#         print(germany_companies[count])
#         count +=1
# print()
# get_um_linha(0, 6)
# get_um_linha(6, 12)
#
# count = 0
# max = 6
#
# inicio = 0
# while inicio < len(germany_companies):
#     get_um_linha(count, max)
#     count += 1
#     max += 6