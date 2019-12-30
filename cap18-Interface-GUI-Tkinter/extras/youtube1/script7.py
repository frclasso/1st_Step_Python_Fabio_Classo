from tkinter import *

janela = Tk()

janela.geometry("400x300+200+200")

ed = Entry(janela)
ed.place(x=100, y=100)


def bt_onclick():
    print(ed.get())
    lb['text'] = ed.get()


bt = Button(janela, width=18, text="ok", command=bt_onclick)
bt.place(x=100, y=130)

lb = Label(janela, text='Label')
lb.place(x=150, y=160)


janela.mainloop()
