
from tkinter import *

root = Tk()

t = Text(root,height=2, width=30)

t.pack()
t.insert('end', "Just a text Widget\nin two lines.")

root.mainloop()