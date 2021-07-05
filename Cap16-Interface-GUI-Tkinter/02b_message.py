from tkinter import *

root = Tk()

gandhi_msg = "Whatever you do will be insignificant, but it is very important" \
      "that you do it.\n(Mahatma Gandhi)"

msg = Message(root, text=gandhi_msg)
msg.config(bg='light green',font=('Times', 24, 'italic'))
msg.pack()

root.mainloop()