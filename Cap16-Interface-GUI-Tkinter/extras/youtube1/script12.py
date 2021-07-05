from tkinter import *

janela = Tk()

janela.geometry("400x300+200+200")

lb1 = Label(janela, text='Horizontal', bg='grey')
lb2 = Label(janela, text='', bg='blue')
lb3 = Label(janela, text='', bg='blue')

lb1.pack(side=TOP, fill=X) # X = horizontal
lb2.pack(side=LEFT, fill=Y) # Y = vertical
lb3.pack(side=RIGHT, fill=Y)





janela.mainloop()