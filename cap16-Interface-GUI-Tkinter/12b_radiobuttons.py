from tkinter import *

root = Tk()

var = IntVar()

l1 = Label(root,
           text="Escolha uma linguagem de programação:",
           justify=LEFT,
           padx=20).pack()

r1 = Radiobutton(root,
                 text="Python",
                 padx=20,
                 variable=var,
                 value=1).pack(anchor=W)

r2 =Radiobutton(root,
                text="Perl",
                padx=20,
                variable=var,
                value=2).pack(anchor=W)

root.mainloop()