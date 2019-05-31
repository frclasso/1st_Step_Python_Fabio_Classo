from tkinter import *

canvas_width = 200
canvas_height = 200

python_green = "#476042"

root = Tk()

w = Canvas(root,
           width=canvas_width,
           height=canvas_height)

w.pack()

points = [0,0, canvas_width, canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green, fill='yellow', width=3)

root.mainloop()