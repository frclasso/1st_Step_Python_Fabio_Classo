#!/usr/bin/env python3

import urllib.request

try:
    webpage = urllib.request.urlopen('http://www.google.com')
except:
    print('Could not access the webpage.')
else:
    for line in webpage:
        print(line)