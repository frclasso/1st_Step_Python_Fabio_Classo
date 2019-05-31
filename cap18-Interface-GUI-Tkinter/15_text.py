#!/usr/bin/env python3

from tkinter import *

root = Tk()

t = Text(root, height=2, width=30)
t.pack()
t.insert(END, "Just a text Widget\nin tow lines")

root.mainloop()


