#!/usr/bin/env python3

from tkinter import *

root = Tk()

mb = Menubutton(root, text="condiments", relief=RAISED)

mb.grid()
mb_menu = Menu(mb, tearoff=0)
mb['menu'] = mb_menu

mayoVar = IntVar()
ketchVar = IntVar()

mb_menu.add_checkbutton(label="mayo", variable=mayoVar)
mb_menu.add_checkbutton(label="ketchup", variable=ketchVar)

mb.pack()
root.mainloop()