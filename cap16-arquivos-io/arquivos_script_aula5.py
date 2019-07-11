#!/usr/bin/env python3

# Retornando a data de ultima modificacao dos arquivos

from datetime import datetime
from os import scandir

caminho = '/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'cap16-arquivos-io/'

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_entries = scandir('/home/fabio-gurus/Desktop/repositories/Python/1st_Step_Python_Fabio_Classo/' \
           'cap16-arquivos-io/')
    for entry in dir_entries:
        if entry.is_file:
            info = entry.stat()
            print (f'{entry.name}\t Ultima modificacao: {convert_date(info.st_mtime)}')

print(get_files())

"""
    %d: the day of the month
    %b: the month, in abbreviated form
    %Y: the year
"""

