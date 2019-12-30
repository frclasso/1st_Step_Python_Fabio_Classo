from tkinter import *

janela = Tk()


# W x H + L + T
janela.geometry("400x300+200+200")

def bt_click():
    print('bt_click clicado')

    lb['text'] = 'E ganhe Super Poderes'


bt = Button(janela, width=20, text="ok", command=bt_click)
bt.place(x=100, y=100)

lb = Label(janela, text='Aprenda Python')
lb.place(x=150, y=150)



janela.mainloop()