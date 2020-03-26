from tkinter import *

counter = 0


def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

root = Tk()
root.title("Contando de segundos")
label = Label(root, fg='red', bg='yellow', font="Helvetica 22 bold italic")
label.pack()
counter_label(label)
button = Button(root, text='Stop',fg='blue', width=25, command=root.destroy)
button.pack()

root.mainloop()