

# gerenciador de contexto
"""
    with open('nome do arquivo', 'w') as file:
        operações...

"""

# read - lê todo o conteúdo do arquivo re uma vez
with open('my_clientes.txt', 'r') as file:
    linha = file.read()
    #linha = file.read(10)
    print(linha)



# readline() - se nao for declarado a quantidade de caracteres, lê até o conteúdo da primeira linha
# with open('my_clientes.txt', 'r') as file:
#     linha = file.readline()
#     print(linha)


# readlines() - retorna uma lista com conteudo do arquivo
# with open('my_clientes.txt', 'r') as file:
#     linha = file.readlines()
#     #linha = file.readlines(36)
#     #linha = file.readlines(48)
#     print(linha)

