import requests

"""LENDO CSV FILES"""

url = 'https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/baby_names.csv'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.encoding)
#
# for lines in response.text:
#     print(lines, end='')


# Outras urls de arquivos csv
"https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/deniro.csv"
"https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/oscar_male.csv"
"https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/oscar_female.csv"
"https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/Titanic_2.csv"
"https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/world_dev_ind.csv"


"""LENDO JSON FILES"""

url_json = 'https://f001.backblazeb2.com/file/Datasets-gurus/json/a_movie.json'
# response_json = requests.get(url_json)
# print(response_json.status_code)
# print(response_json.text)


# Outras urls de arquivos JSON
'https://f001.backblazeb2.com/file/Datasets-gurus/json/glossary.json'
'https://f001.backblazeb2.com/file/Datasets-gurus/json/peopledata.json'
'https://f001.backblazeb2.com/file/Datasets-gurus/json/webapp.json'
'https://f001.backblazeb2.com/file/Datasets-gurus/json/widget.json'


"""BAIXANDO ARQUIVOS EXCEL"""
urls_xlsx = 'https://f001.backblazeb2.com/file/Datasets-gurus/xlsx_files/fruit_stores.xlsx'
# response_xlsx = requests.get(urls_xlsx)
# print(response_xlsx)
#criando um arquivo local com a copia do conteudo remoto
# open('dados_fruits_store.xlsx', 'wb').write(response_xlsx.content)

# Outras urls de arquivos xlsx
'https://f001.backblazeb2.com/file/Datasets-gurus/xlsx_files/censuspopdata.xlsx'
"https://f001.backblazeb2.com/file/Datasets-gurus/xlsx_files/Data+Refresh+Sample+Data.xlsx"
"https://f001.backblazeb2.com/file/Datasets-gurus/xlsx_files/movie_theater_sales_data.xlsx"




"""BAIXANDO IMAGENS"""
urls_imagens = 'https://f001.backblazeb2.com/file/Datasets-gurus/imagens_download/aguia+-+natureza+selvagem+-+%232.jpg'
# response_for_imgs = requests.get(urls_imagens)
# print(response_for_imgs)
#print(response_for_imgs.content)
#criando um arquivo local com a copia do conteudo remoto
#open('aguia_local.jpg', 'wb').write(response_for_imgs.content)



"""
    Mais informacoes sobre a biblioteca requests
    https://requests.readthedocs.io/en/master/
"""