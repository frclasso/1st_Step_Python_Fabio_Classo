#!/usr/bin/env python3

from tkinter import *

root = Tk()

C = Canvas(root, bg='Blue', height=250, width=300)

coord = 10, 50, 240, 210

# desenhando um arco
arc = C.create_arc(coord, start=0, extent=150, fill='red')

#criando uma linha
line = C.create_line(10,10,200,200,fill='white')

C.pack()
root.mainloop()
