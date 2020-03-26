#!/usr/bin/env python3

from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="Inside the LabelFrame")
left.pack(side=LEFT)

center = Label(labelframe, text="Inside the LabelFrame")
center.pack()


right = Label(labelframe, text="Inside the LabelFrame")
right.pack(side=RIGHT)

root.mainloop()