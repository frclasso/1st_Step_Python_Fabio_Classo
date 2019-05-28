#!/.usr/bin/env python3

from tkinter import *

root = Tk()

root.title('Cadastro de alunos')

# 5 ------------------------------
# definindo as funções

def sair():
    root.quit()






lb1 = Label(root, text='Nome')
lb1.grid(row=0,column=0)

ed1 = Entry(root)
ed1.grid(row=0,column=1,sticky=W)

lb2 = Label(root, text='Sobrenome')
lb2.grid(row=1,column=0)

ed2 = Entry(root)
ed2.grid(row=1,column=1, sticky=W)

lb3 = Label(root, text='e-mail')
lb3.grid(row=2,column=0)

ed3 = Entry(root)
ed3.grid(row=2,column=1, sticky=W)

# 2 --------------------------------

lb4 = Label(root, text='Selecione o curso').grid(row=4, column=0, sticky=W)
c1 = Checkbutton(root, text='Python').grid(row=5, column=0, sticky=W)
c2 = Checkbutton(root, text='C#').grid(row=6, column=0, sticky=W)
c3 = Checkbutton(root, text='PHP').grid(row=7, column=0, sticky=W)
c4 = Checkbutton(root, text='Excel').grid(row=8, column=0, sticky=W)

# 3 ---------------------------------

lb5 = Label(root, text='Horario').grid(row=4, column=1, sticky=W)
r1 = Radiobutton(root, text='Manha - 08 as 12h', value=1).grid(row=5, column=1, sticky=W)
r2 = Radiobutton(root, text='Tarde - 13 as 17h', value=2).grid(row=6, column=1, sticky=W)
r3 = Radiobutton(root, text='Noite - 19 as 23h', value=3).grid(row=7, column=1, sticky=W)

lb6 = Label(root, text="Comentarios").grid(row=9, column=0, sticky=W)
ed4 = Entry(root, width=50).grid(row=9, column=1, sticky=W+E)
b1 = Button(root, text='Submit').grid(row=9,column=3,columnspan=3,sticky=W+E)

b1 = Button(root, text='Sair', command=sair).grid(row=10,column=3,columnspan=3,sticky=W+E)

# Criando um frame para imagem

from PIL import Image
from PIL import ImageTk

frame = Frame(root)
frame.grid(row=0, column=3, rowspan=5, columnspan=3)

# 4 -----------------------------

# Inserindo imagem

img = Image.open('python_logo.gif')
img = img.resize((100, 100), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
Label(frame, image=photoImg).grid(row=0, column=0)

root.mainloop()