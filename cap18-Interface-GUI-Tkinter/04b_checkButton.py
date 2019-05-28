#!/usr/bin/env python3


from tkinter import *
root = Tk()


def var_states():
    print("Python: {} \nPearl: {}".format(var1.get(), var2.get()))


var1 = IntVar()
c1 = Checkbutton(root, text="Python", variable=var1).grid(row=0, sticky=W)

var2 = IntVar()
c2 = Checkbutton(root, text="Pearl", variable=var2).grid(row=1, sticky=W)

# Adicionando dois botões
b1 = Button(root, text="Exibir", command=var_states).grid(row=4, sticky=W,pady=4)
b2 = Button(root, text="Fechar", command=root.quit).grid(row=3, sticky=W,pady=4)

root.mainloop()