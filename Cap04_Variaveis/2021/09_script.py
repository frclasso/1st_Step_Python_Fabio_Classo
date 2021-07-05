
campos = ["store", "product_name", "quantity_purchased", "revenue"]

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

# imprimir os valores
# imprimir apenas a primeira sub-lista
# atribuir a sublista a uma variavel
# remover  o primeiro campo da sublista
# loop for para fazer em todas as linhas(sublistas)
# for v in fruits_stores:
#     print(v)
#
# print()
# for v in fruits_stores[0]:
#     print(v)

print()
# banana = []
# for v in fruits_stores[0]:
#         banana.append(v)
# print(banana)

# remover  o primeiro campo da sublista
# fruits_stores[0].pop(0)
# print(fruits_stores[0])


# for values in fruits_stores:
#     values.pop(0)
# print(fruits_stores)

# for c in fruits_stores:
#     print(c)

campos.append('total')
# print(campos)
total = fruits_stores[0][2] * fruits_stores[0][3]
# # # print(total)
# # #
# for linha in fruits_stores:
#     print(linha)
#     for vendedor in linha:
#         unidade = linha[2]
#         valor = linha[3]
#         total = unidade * valor
#     linha.append(total)
# #
# print()
# print()
# print()
# # print(campos)
# # for c in fruits_stores:
# #     print(c)


# while
# print(len(fruits_stores))

count = 0
while count < len(fruits_stores):
    #print(count)
    #print(fruits_stores[count])
    unidade = fruits_stores[count][2]
    valor = fruits_stores[count][3]
    total = unidade * valor
    fruits_stores[count].append(total)
    count += 1

for v in fruits_stores:
        print(v)