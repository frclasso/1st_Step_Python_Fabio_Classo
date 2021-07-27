#!/usr/bin/env python3

from tkinter import *

root = Tk()

canvas_width = 200
canvas_height = 100

w = Canvas(root, width=canvas_width,
           height = canvas_height)

w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0,0,50,20, fill="#476042", width=3)
w.create_line(0,100,50,80, fill="#476042", width=3)
w.create_line(150,20,200,0, fill="#476042", width=3)
w.create_line(150,80,200,100, fill="#476042", width=3)

root.mainloop()