#!/usr/bin/env python3

from tkinter import *

root = Tk()

L1 = Label(root, text="First Name").grid(row=0)
L2 = Label(root, text="Last Name").grid(row=1)

E1 = Entry(root, bd=2)
E2 = Entry(root, bd=2)

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)


root.mainloop()