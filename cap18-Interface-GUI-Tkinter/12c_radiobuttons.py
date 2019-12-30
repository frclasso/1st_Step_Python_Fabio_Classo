from tkinter import *

root = Tk()


var = IntVar()

var.set(0)  # inicializando com a opção Python marcada

languages = [
    "Python",
    "Perl",
    "Java",
    "C++",
    "C",
]


def ShowChoice():
    print(var.get())  # captura o valor da opção escolhida

l1 = Label(root,
           text="""Escolha sua linguagem de programação favorita:""",
           justify=LEFT,
           padx=20).pack()

for val, language in enumerate(languages):
    r1 = Radiobutton(root,
                     text=language,
                     padx=20,
                     variable=var,
                     command=ShowChoice,
                     value=val).pack(anchor=W)


root.mainloop()