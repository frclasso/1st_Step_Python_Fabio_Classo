#!/usr/bin/env python3


# Criando um programa para manipular imagens

import os


os.chdir('/Users/fabio/Desktop/turma3_Python1_2018/Cap16_Files/imgs')
# print(os.getcwd())

# checando os arquivos
# for file in os.listdir():
#     print(file)

# Manipular arquivos em Python, biblioteca pilow
from PIL import Image
#image1 = Image.open('aguia - natureza selvagem - #2.jpg')
#image1.show()

# salvando em .png
#image1.save('aguia.png')

# Salvando todos em .png

import os

size_300 = (300,300)
size_500 = (500,500)
for f in os.listdir():
    if f.endswith('jpg'):
        #print(f)
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        #print(fn)

        # salvar em back_up_imgs
        i.thumbnail(size_500)
        i.save('/Users/fabio/Desktop/turma3_Python1_2018/Cap16_Files/'
               'size_500/{}_500{}'.format(fn, fext))


        i.thumbnail(size_300)
        i.save('/Users/fabio/Desktop/turma3_Python1_2018/Cap16_Files/'
               'size_300/{}_300{}'.format(fn, fext))


print('Feito...')