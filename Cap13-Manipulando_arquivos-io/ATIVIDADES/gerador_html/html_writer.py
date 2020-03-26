#!usr/bin/env python3


import urllib.request
page = urllib.request.urlopen('https://docs.python.org/')

with open('arquivo.html', 'w') as file:
    for line in page:
        file.write(str(line, encoding='utf-8'))


print('Done..')

