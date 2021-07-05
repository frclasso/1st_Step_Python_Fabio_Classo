import os
from datetime import datetime
#
# print(os.stat('teste.txt').st_size)
# print(os.path.getsize('teste.txt'))
#
# mod_time = os.stat('teste.txt').st_mtime
# print('Ultima modificacao do arquivo: {}'.format(datetime.fromtimestamp(mod_time)))

base = os.path.basename('/Users/fabio/Estudo/Prog/Python/1st_Step_Python_2020/')
for root, dir, file in os.walk(os.path.abspath('.')):
    print(root)
    print(dir)
    print(file)