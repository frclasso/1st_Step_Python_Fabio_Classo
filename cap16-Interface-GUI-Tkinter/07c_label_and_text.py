from tkinter import *

root = Tk()

l1 = Label(root, text="Red Text in Times font", fg='red', font="Times").pack()

l2 = Label(root,
           text="Gree Text in Helvetica font",
           fg='light green',bg='dark green',
           font="Helvetica 16 bold italic").pack()

l3 = Label(root,
           text="Blue Text in Verdana Bold font",
           fg='blue',
           bg='yellow',
           font="Verdana 10 bold").pack()



root.mainloop()