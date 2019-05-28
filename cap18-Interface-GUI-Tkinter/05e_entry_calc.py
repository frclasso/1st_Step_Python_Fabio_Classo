from tkinter import *
from math import *

def evaluate(event):
    res.configure(text='Resultado: ' + str(eval(entry.get())))

root = Tk()
Label(root, text="Your expression: ").pack()
entry = Entry(root)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(root)
res.pack()

root.mainloop()