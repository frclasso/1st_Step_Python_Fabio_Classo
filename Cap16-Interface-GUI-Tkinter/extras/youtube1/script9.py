from tkinter import *

janela = Tk()

janela.geometry("400x300+200+200")

ed1 = Entry(janela)    # 1
ed1.place(x=100, y=100)

ed2 = Entry(janela)       # 1
ed2.place(x=100, y=130)


def bt_click():    # 4
    print('bt_clicked')

    if ed1.get().isnumeric() and ed2.get().isnumeric():
        num1 = int(ed1.get())
        num2 = int(ed2.get())

        lb['text'] = num1 + num2
    else:
        lb['text'] = 'Valores informados inválidos'


bt = Button(width=18, text='soma', command=bt_click)  # 2
bt.place(x=100, y=150)

lb = Label(janela, text='Label 1')     # 3
lb.place(x=100, y=200)

janela.mainloop()
