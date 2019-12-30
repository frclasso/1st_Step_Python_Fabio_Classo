#!/usr/bin/env python


import os

os.chdir('/Users/fabio/Estudo/Prog/Python/Python_tutorial_by_Corey_Schafer/'
         '01_Beginners/imgs/back_up_imgs')

print(os.getcwd())

# lendo os arquivos

# for f in os.listdir():
#     print(f)

from PIL import Image

image1 = Image.open('01-coruja.png')
#image1.show()

# ratacionando uma imagem
#image1.rotate(90).save('01-coruja_rotated.png') # cria m cópia rotacionada 90 graus

#image1.convert(mode='L').save('01-coruja_black_white.png')


# Inserindo filtro Gaussiano Blur
from PIL import ImageFilter

# o padrao do GaussianBlur é 2
image1.filter(ImageFilter.GaussianBlur(10)).save('01-coruja_Glaussian_Blur.png')

print('Done...')