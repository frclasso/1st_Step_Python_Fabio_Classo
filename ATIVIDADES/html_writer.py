#!usr/bin/env python3


import urllib.request

my_url = input('Digite uma url: ')
page = urllib.request.urlopen(my_url)

arquivo_html = input('Digite o nome do arquivo: ')
with open(arquivo_html, 'w') as file:
    for line in page:
        file.write(str(line, encoding='utf-8'))


print('Done..')

# definir uma funcao url vamos abrir
# definir uma funcao para nomear o arquivo




