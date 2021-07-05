

a_lang_sohne = ['A. Lange & Söhne', 'Consumer goods','Clothing & accessories','Glashütte',1845,'Watches']

chaves = ['name', 'industry', 'sector', 'headquarters', 'founded', 'notes']


a_lang_dict = {}

# a_lang_dict['name'] = a_lang_sohne[0]
# a_lang_dict['industry'] = a_lang_sohne[1]
#
# print(a_lang_dict)

for k in chaves:
    print(k)
print()
for v in a_lang_sohne:
    print(v)

for k in chaves:
    for v in a_lang_sohne:
        a_lang_dict[k] = v
print(a_lang_dict)
print()


# Modo correto
a_lang_dict_new = {}
for k,v in zip(chaves,a_lang_sohne):
    print(k, v)
    a_lang_dict_new[k] = v
print(a_lang_dict_new)

# Atividade
# converter toda liata germani_companies (caso 2) em dicionario