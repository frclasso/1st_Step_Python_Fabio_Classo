#!/usr/bin/env python


import os

os.chdir('/Users/fabio/Desktop/imgs')

#print(os.getcwd())

# lendo os arquivos

# for f in os.listdir():
#     #print(f)
#     print(os.path.splitext(f))

# # descomente o codigo
# for f in os.listdir():
#     file_name, file_extension = os.path.splitext(f)
#     print(file_name)

# descomente o codigo
# for f in os.listdir():
#     f_name, f_extension = os.path.splitext(f)
#     #print(f_name.split('-'))  # usando o - como separador
#
#     #vamos definir 3 variáveis
#     f_animal, f_title, f_num = f_name.split('-')
#     print(f_animal)


# descomente o codigo
# for f in os.listdir():
#     f_name, f_extension = os.path.splitext(f)
#     f_animal, f_title, f_num = f_name.split('-')
#     print('{}-{}-{}{}'.format(f_num, f_title, f_animal,f_extension))

# eliminando os espaços entre os parametros
# for f in os.listdir():
#     f_name, f_extension = os.path.splitext(f)
#     f_animal, f_title, f_num = f_name.split('-')
#
#     f_animal = f_animal.strip()
#     f_title = f_title.strip()
#     #f_num = f_num.strip()
#     #f_num = f_num.strip()[1:]  # pegando a partir do primeiro caracter
#     f_num = f_num.strip()[1:].zfill(2)  # preenche com 0 os que possuem apenas um digito
#
#     print('{}-{}-{}{}'.format(f_num, f_title, f_animal,f_extension))

# renomeando os arquivos
for f in os.listdir():
    f_name, f_extension = os.path.splitext(f)
    f_animal, f_title, f_num = f_name.split('-')

    f_animal = f_animal.strip()
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)

    # retirei f_title
    novo_nome = '{}-{}{}'.format(f_num,f_animal,f_extension)

    os.rename(f, novo_nome)


# https://www.youtube.com/watch?v=ve2pmm5JqmI