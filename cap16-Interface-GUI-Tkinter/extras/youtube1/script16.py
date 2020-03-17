from tkinter import *

janela =Tk()

lb1 = Label(janela, text='ESPAÇO', width=15, height=3,bg='blue')
lb_horizontal = Label(janela, text="Horizontal", bg='yellow')
lb_vertical = Label(janela, text='Vertical', bg='yellow')

lb1.grid(row=0, column=0)
lb_horizontal.grid(row=1, column=0, sticky=E)
lb_vertical.grid(row=0, column=1, sticky=N)

janela.geometry("200x100+100+100")


janela.mainloop()