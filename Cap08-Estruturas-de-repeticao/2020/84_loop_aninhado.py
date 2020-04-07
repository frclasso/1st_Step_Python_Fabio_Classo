

carros_lot_3d = [
    [
        ['Tesla', 'Fiat', 'BMW'],
        ['Honda', 'Jeep'],
        ['Porsche', 'Kia','Ford']
    ],
    [
        ['Subaru', 'Nissan'],
        ['Volvo']
    ],
    [
        ['Mazda', 'Chevy'],
        ['Audi'],
        ['Volkswagen']
    ]
]
#primeiro nivel
print(type(carros_lot_3d))
print(carros_lot_3d)

#segundo nivel
print(type(carros_lot_3d[0]))
print(carros_lot_3d[0])

#terceiro nivel
print(type(carros_lot_3d[0][0]))
print(carros_lot_3d[0][0])



# for floor in carros_lot_3d:
#     for row in floor:
#         for car in row:
#             print(car)
#
# print()
# print("Done.")