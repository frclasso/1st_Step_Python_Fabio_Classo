#!usr/bin/env python3


import urllib.request
import requests
#page = urllib.request.urlopen('https://docs.python.org/')
page = requests.get('https://docs.python.org/')

with open('arquivo.html', 'w') as file:
    for line in page:
        file.write(str(line, encoding='utf-8'))


print('Done..')

