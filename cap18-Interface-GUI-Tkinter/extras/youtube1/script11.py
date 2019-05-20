from tkinter import *

janela = Tk()

janela.geometry("400x300+200+200")


lb1 = Label(janela, text='SIDE 1', bg='green')
lb2 = Label(janela, text='SIDE 2', bg='red')
lb3 = Label(janela, text='ANCHOR 3', bg='yellow')
lb4 = Label(janela, text='ANCHOR 4', bg='blue')

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side=BOTTOM, anchor=SW)

janela['bg'] = 'black'


janela.mainloop()