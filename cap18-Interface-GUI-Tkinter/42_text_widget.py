
from tkinter import *

root = Tk()
root.geometry("670x180")

text1 = Text(root,height=20, width=30)
photo = PhotoImage(file='william_shakespeare.gif')

text1.insert('end', '\n')
text1.image_create('end', image=photo)
text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root,command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow','<1>', lambda e, t=text2:t.insert('end', "Not now,maybe latter!"))
text2.insert('end', '\nWilliam Shakespeare\n', 'big')


quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""

text2.insert('end', quote, 'color')
text2.insert('end', 'follow-up\n', 'follow')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)


root.mainloop()