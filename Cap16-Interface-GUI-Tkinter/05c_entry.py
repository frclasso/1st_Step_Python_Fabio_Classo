#!/usr/bin/env python3

from tkinter import *

root = Tk()


def show_fields():
    print("First name: {}, Lastname: {}".format(E1.get(), E2.get()))
    E1.delete(0, END)
    E2.delete(0, END)


L1 = Label(root, text="First Name").grid(row=0)
L2 = Label(root, text="Last Name").grid(row=1)

E1 = Entry(root, bd=2)
E2 = Entry(root, bd=2)

E1.insert(10, "Miller")  # Exibindo nomes padrão
E2.insert(10, "Jill")

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)

b1 = Button(root, text="Sair", command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
b2 = Button(root, text="Exibir", command=show_fields).grid(row=3, column=1, sticky=W, pady=4)


root.mainloop()

"""E quanto a deletar a entrada de um objeto Entry, toda vez, estamos mostrando o conteúdo
 em nossa função show_entry_fields ()? Sem problemas! Podemos usar o método delete. 
 O método delete () tem o formato delete (first, last = None). Se apenas um número é dado,
  ele exclui o caractere no índice. Se dois forem dados, o intervalo de "primeiro" a 
  "último" será excluído. Use delete (0, END) para excluir todo o texto no widget."""