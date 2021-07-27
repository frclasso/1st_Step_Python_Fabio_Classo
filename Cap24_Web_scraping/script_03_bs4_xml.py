import requests
import bs4
import lxml

url = 'https://f001.backblazeb2.com/file/Datasets-gurus/informacoes_tributarias.xml'
response = requests.get(url)
print(response.status_code)
print(response.headers)
print(response.content)
for conteudo in response.content.decode('latin-1'):
    print(conteudo, end='')

# Escrevendo localmente
open('arquivo_tributario.xml', 'w').write(response.content.decode('latin-1'))
