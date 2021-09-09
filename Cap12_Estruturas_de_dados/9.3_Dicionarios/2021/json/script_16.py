import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/"\
"aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/"\
    "9.3_Dicionarios/2021/json"
os.chdir(file_path)

print(os.getcwd())

from my_apy import get_data


# for data in get_data():
#     print(data)