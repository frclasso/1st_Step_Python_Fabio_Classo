#!/usr/bin/env python3


from tkinter import *
root = Tk()

var1 = IntVar()
c1 = Checkbutton(root, text="Python", variable=var1).grid(row=0, sticky=W)

var2 = IntVar()
c2 = Checkbutton(root, text="Pearl", variable=var2).grid(row=1, sticky=W)

root.mainloop()