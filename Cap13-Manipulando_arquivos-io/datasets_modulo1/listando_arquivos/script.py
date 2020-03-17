#!/usr/bin/env python3


import os

# print(os.getcwdb())
#
# arquivos = os.listdir()
# #print(arquivos)
# for names in arquivos:
#     print(names)

# print()
#
#
# # ABRINDO ARQUIVOS ZIP
# import zipfile
#
# # # listanbdo conteudo do arquivo zip
# with zipfile.ZipFile('arquivos_txt_mat_dta.zip', 'r') as zipobj:
#     for name in zipobj.namelist():
#         print(name)
#     #print (zipobj.namelist())
#
# print()
#
# # Metadata in the zip file
#
# zip = zipfile.ZipFile('archive.zip', 'r')
# # for meta in zip.infolist():
# #     print(meta)
#
#
# # Metadata for a specific file
# info = zip.getinfo('cars.txt')
# print(info)
#
#
# # Access to files in zip folder
# print(zip.read('cars.txt'))
# # or
# with zip.open('techBrands.txt') as f:
#     print(f.read())


# #extraindo
#
#
# ziped = zipfile.ZipFile('arquivos_txt_mat_dta.zip', 'r')
# ziped.extractall()

# extrair o img.zip


# for nomes in os.listdir():
#     print(nomes)


# Separando os arquivos por tipo
# diretorio para .csv - arquivos_csv
#os.mkdir('arquivos_csv')

# arquivos = os.listdir()
# for names in arquivos:
#     print(names)


# diretorio para txt, arquivos_txt
#
# alterar o nome do diretorio xlsx_files  para arquivos_xlsx os.rename(velho, novo)
# alterar o nome do diretorio imgs  para arquivos_imagens os.rename(velho, novo)

# remover arquivos .zip - os.remove()

# lendo diretorios e sub diretorios
# for dirpath, dirnames, files in os.walk('.'):
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         print(file_name)

# coping files

arquivos = os.listdir()
# #print(arquivos)
lista_csv = []
for names in arquivos:
    #print(names)
    if names.endswith('.csv'):
        lista_csv.append(names)

#print(lista_csv)
import shutil
# print(os.getcwdb())
# origem = '/Users/fabio/Estudo/Prog/Python/1st_Step_Python_Fabio_Classo/Cap13-Manipulando_arquivos-io/datasets_modulo1/listando_arquivos/*.csv'
# destino = '/Users/fabio/Estudo/Prog/Python/1st_Step_Python_Fabio_Classo/Cap13-Manipulando_arquivos-io/datasets_modulo1/listando_arquivos/arquivos_csv/'
# shutil.copy2(origem, destino)
# print(os.listdir('/Users/fabio/Estudo/Prog/Python/1st_Step_Python_Fabio_Classo/Cap13-Manipulando_arquivos-io/datasets_modulo1/listando_arquivos/arquivos_csv'))