
cabecalho = ["store", "product_name", "quantity_purchased", "revenue"]

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
]

# cabecalho.append("total")
# print(cabecalho)
# fruits_stores[0].append(None)
# print(fruits_stores[0])

# print(fruits_stores[0][2])
# print(fruits_stores[0][3])
# total = fruits_stores[0][2] * fruits_stores[0][3]
# print(total)
# print()

# for linhas in fruits_stores:
#     print(linhas)

print()
# for linhas in fruits_stores:
#     for vendedor in linhas:
#         unidade =linhas[2]
#         valor = linhas[3]
#         total = unidade * valor
#     # print(total)
#     # print(linhas)
#     linhas.append(total)
#
# for linhas in fruits_stores:
#     print(linhas)


x = 0
new_fruits_stores = []
while x < len(fruits_stores):
    #print(x)
    #print(fruits_stores)
    #print(fruits_stores[x])
    linhas = fruits_stores[x]
    unidade = fruits_stores[x][2]
    # print(unidade)
    valor = fruits_stores[x][3]
    total = unidade * valor
    # print(total)
    linhas.append(total)
    #print(linhas)
    new_fruits_stores.append(linhas)
    x += 1

for fruits in new_fruits_stores:
    print(fruits)


# ATIVIDADES:
# ordenar por vendedores
# ordenar por produtos
# ordenar por menor preço
# ordenar por maior preço
# ordenar por maior quantidade
# ordenar por menor quantidade
