from tkinter import *

janela = Tk()

# W x H + L + T
janela.geometry("400x300+200+200")


def bt1_click():
    print('Botao 1 foi clicado')


def bt2_click():
    print('Botao 2 foi clicado')


bt1 = Button(janela, width=20, text='Botao 1', command=bt1_click)
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text='Botao 2', command=bt2_click)
bt2.place(x=100, y=130)


janela.mainloop()