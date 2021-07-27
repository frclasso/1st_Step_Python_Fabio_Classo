#!/usr/bin/env python


import os

os.chdir('/Users/fabio/Estudo/Prog/Python/Python_tutorial_by_Corey_Schafer/01_Beginners/imgs')

print(os.getcwd())

# lendo os arquivos

# for f in os.listdir():
#     print(f)

from PIL import Image

#image1 = Image.open('aguia - natureza selvagem - #2.jpg')
#image1.show()

# salvando em .png
#image1.save('aguia.png')


# # Salvando varios arquivos
# import os
#
# for f in os.listdir():
#     if f.endswith('jpg'):
#         #print(f)
#         i = Image.open(f)
#         fn, f_ext = os.path.splitext(f)
#         #print(fn)
#
#         # criar back_up_imgs folder
#         i.save('back_up_imgs/{}.png'.format(fn))

# # Descomente o código abaixo
#
# # Salvando varios arquivos
# import os
#
# # definindo um tamanho de arquivos
# size_300 = (300,300)
#
# for f in os.listdir('.'):
#     if f.endswith('jpg'):
#         i = Image.open(f)
#         fn, f_ext = os.path.splitext(f)
#
#         i.thumbnail(size_300)
#         i.save('300/{}_300{}'.format(fn, f_ext))



# Descomente o código abaixo

# Salvando varios arquivos
import os

# definindo um tamanho de arquivos
size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir(''):
    if f.endswith('jpg'):
        i = Image.open(f)
        fn, f_ext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, f_ext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, f_ext))




print('Done...')