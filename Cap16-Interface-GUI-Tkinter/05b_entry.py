#!/usr/bin/env python3

from tkinter import *

root = Tk()


def show_fields():
    print("First name: {}, Lastname: {}".format(E1.get(), E2.get()))


L1 = Label(root, text="First Name").grid(row=0)
L2 = Label(root, text="Last Name").grid(row=1)

E1 = Entry(root, bd=2)
E2 = Entry(root, bd=2)

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)

b1 = Button(root, text="Sair", command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
b2 = Button(root, text="Exibir", command=show_fields).grid(row=3, column=1, sticky=W, pady=4)


root.mainloop()