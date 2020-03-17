from tkinter import *

janela =Tk()

janela.geometry("400x300+200+200")

lb1 = Label(janela, text='Label 1')
lb2 = Label(janela, text='Label 2')


lb1.grid(row=1000, column=1000)
lb2.grid(row=2000, column=2000)


janela.mainloop()