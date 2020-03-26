from tkinter import *


janela = Tk()

janela.geometry("400x300+200+200")

lb1 = Label(janela, text='Linha 1', bg='blue')
lb2 = Label(janela, text='Linha 2', bg='yellow')
lb3 = Label(janela, text='Linha 3', bg='green')
lb4 = Label(janela, text='Linha 4', bg='white')

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)


janela.mainloop()