
from tkinter import *

root = Tk()

t = Text(root,height=4, width=50)
s = Scrollbar(root)
s.pack(side=RIGHT, fill=Y)
t.pack(side=LEFT, fill=Y)
s.config(command=t.yview)
t.config(yscrollcommand=s.set)

quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""

t.insert('end',quote)

root.mainloop()