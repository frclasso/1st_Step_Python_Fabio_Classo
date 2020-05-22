

# metodo next() - recupera o proximo item do iterador



techs = open('tecnologias.txt', 'r')
print(f'Nome do arquivo: {techs.name}')
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# 10
for indice in range(10):
    tecnologia = next(techs)
    print(f'{indice} ==> {tecnologia}', end='')

techs.close()


# https://en.wikipedia.org/wiki/List_of_programming_languages