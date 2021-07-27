

from tkinter import *
from functools import partial
janela = Tk()

# W x H + L + T
janela.geometry("400x300+200+200")


def bt_click(botao):
    print(botao['text'])


bt1 = Button(janela, width=20, text='Botao 1')
bt1['command'] = partial(bt_click, bt1)
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text='Botao 2')
bt2['command'] = partial(bt_click, bt2)

bt2.place(x=100, y=130)


janela.mainloop()