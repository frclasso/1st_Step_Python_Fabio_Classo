from tkinter import *

janela = Tk()

janela.geometry("400x550")
janela.title("Cadastro de usuarios")

dados = []


def salvaDados():
    nome = ed1.get()
    sobrenome = ed2.get()
    email = ed3.get()

    lb4['text'] = nome + ',' + sobrenome + ','+ email
    dados_recebidos = [nome + ',' + sobrenome + ','+ email + '\n']
    dados.append(dados_recebidos)

def apagar():
    return dados.pop()

def clear_text():
    return ed1.delete(0, 'end'),ed2.delete(0, 'end'), ed3.delete(0, 'end')


def clear_label():
    lb4['text'] = 'Voce apagou os dados'
    clear_text()


def close():
    print('Bye bye!')
    janela.quit()


def exportar_dados():
    with open('dados.csv', 'a') as file:
        for data in dados:
            file.writelines(data)

    print('Dados exportados com sucesso')
    lb5['text'] = 'Dados exportados com sucesso'

def ultimos_inseridos():
    for linha in dados:
        lb5['text'] = linha

def apagar_ultimo():
    try:
        lb5['text'] = 'Voce apagou o último registro'
        ultimo = dados.pop()
        return ultimo
    except Exception:
        lb5['text'] = 'Não há mais registros'



lb1 = Label(janela, text='Nome')
lb1.place(x=100, y=40)
ed1 = Entry(janela)
ed1.place(x=100, y=60)

lb2 = Label(janela, text='Sobrenome')
lb2.place(x=100, y=100)
ed2 = Entry(janela)
ed2.place(x=100, y=130)

lb3 = Label(janela, text='E-mail')
lb3.place(x=100, y=160)
ed3 = Entry(janela)
ed3.place(x=100, y=180)

bt1 = Button(janela, width=21, text='Salvar', command=salvaDados)
bt1.place(x=100, y=210)

bt2 = Button(janela, width=21, text='Limpar campos', command=clear_label)
bt2.place(x=100, y=240)

lb4 = Label(janela, text='Dados do cliente')
lb4.place(x=130, y=300)


bt4 = Button(janela, width=21, text='Listar cadastros recentes', command=ultimos_inseridos)
bt4.place(x=100, y=350)

lb5 = Label(janela, text='Últimos dados inseridos')
lb5.place(x=110, y=390)

bt6 = Button(janela,width=21, text='Apagar último registro', command=apagar_ultimo)
bt6.place(x=100, y=440)

bt5 = Button(janela, width=21, text='Exportar', command=exportar_dados)
bt5.place(x=100, y=470)

bt3 = Button(janela, width=21, text='Sair', command=close )
bt3.place(x=100, y=500)


janela.mainloop()
