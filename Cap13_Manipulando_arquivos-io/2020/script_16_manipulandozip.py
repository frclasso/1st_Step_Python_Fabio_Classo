import os

print(os.getcwd())
print(os.listdir(''))

import zipfile

with zipfile.ZipFile('json.zip', 'r') as zipobj:
    print (zipobj.namelist())


print()
data_ziped = zipfile.ZipFile('json.zip', 'r')
data_ziped.extractall()

print(os.listdir(''))