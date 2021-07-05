#lista
audi = ['Audi',
        'Consumer goods',
        'Automobiles',
        'Ingolstadt',
        1910,
        'Auto manufacturer, part of Volkswagen Group']

print(type(audi))
print(audi)

# tupla
audi_2 = ('Audi',
        'Consumer goods',
        'Automobiles',
        'Ingolstadt',
        1910,
        'Auto manufacturer, part of Volkswagen Group')

print(type(audi_2))
print(audi_2)
print(audi_2[0])
print(audi_2[-1])
print(audi_2[::-1])


# alterar o conteudo da lista
del audi[-1]
print(audi)
print(audi_2 * 2)

# imutavel
# del audi_2[-1]
# print(audi_2)

t = ('agua', 'fogo')
t2 = ('terra', 'ar')
t3 = t + t2
print(t3)