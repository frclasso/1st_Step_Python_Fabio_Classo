
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