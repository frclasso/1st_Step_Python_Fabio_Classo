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
                     indicatoron=0,
                     padx=20,
                     variable=var,
                     command=ShowChoice,
                     value=val).pack(anchor=W)


root.mainloop()

"""Em vez de ter botões de rádio com orifícios circulares contendo espaço em branco,
podemos ter botões de opção com o texto completo em uma caixa. Podemos fazer isso 
definindo a opção indicatoron (significa "indicador ligado") como 0, o que significa
que não haverá indicador de botão de opção separado. O padrão é 1."""