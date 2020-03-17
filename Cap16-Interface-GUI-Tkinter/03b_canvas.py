#!/usr/bin/env python3

from tkinter import *

root = Tk()

canvas_width = 80
canvas_height = 40

w = Canvas(root, width=canvas_width,
           height = canvas_height)

w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")

root.mainloop()