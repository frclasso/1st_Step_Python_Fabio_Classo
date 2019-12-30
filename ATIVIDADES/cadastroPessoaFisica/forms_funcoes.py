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
