import tkinter as tk

janela = tk.Tk()  # 1

janela.title("Janela principal")  # 1

janela['bg'] = 'green'    # 2  # atribuimos como um dicionario

# Largura x Altura X Distancia Esq + Distancia Top
janela.geometry("300x300+100+100")  # 3



janela.mainloop()   # 1


