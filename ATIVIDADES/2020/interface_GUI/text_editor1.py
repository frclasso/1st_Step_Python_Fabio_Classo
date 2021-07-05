# https://realpython.com/python-gui-tkinter/#building-a-text-editor-example-app

import tkinter as tk


window = tk.Tk()

window.title("Simple Text Editor")
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open")
btn_save = tk.Button(fr_buttons, text="Save As...")
