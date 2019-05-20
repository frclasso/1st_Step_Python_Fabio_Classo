from tkinter import *

janela = Tk()

lb = Label(janela, text='Floripa Code Gurus')
lb.place(x=100, y=100)

# W x H + L + T
janela.geometry("400x300+200+200")

janela.mainloop()