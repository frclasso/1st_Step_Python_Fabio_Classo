from tkinter import *

root = Tk()

logo = PhotoImage(file="python_logo.gif")

w1 = Label(root, image=logo).pack(side='right')

mytext = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum."""


w2 = Label(root, justify=LEFT, padx=10, text=mytext).pack(side="left")


root.mainloop()