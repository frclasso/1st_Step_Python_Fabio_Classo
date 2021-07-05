#!/usr/bin/env python3

# ZipFile module
import zipfile
import os

for root, subdir, files in os.walk('zips'):
    print(files)
    for file in files:
        with zipfile.ZipFile('zipados.zip', 'a') as myzip:
            caminho = f'{root}/{file}'
            print(caminho)
            myzip.write(caminho)


# Open and list
zip = zipfile.ZipFile('zipados.zip', 'r')
print(zip.namelist())  # Lista conteudo interno do arquivo zip

# Metadata in the zip file
for meta in zip.infolist():
    print(meta)

# Metadata for a specific file
info = zip.getinfo('cars.txt')
print(info)

# Access to files in zip folder
print(zip.read('techBrands.txt'))
# or
with zip.open('techBrands.txt') as f:
    print(f.read())

# Extracting files
# zip.extract('cars.txt')  # extraindo um elemento apenas
zip.extractall() # extraindo tudo


# Closing file
zip.close()

