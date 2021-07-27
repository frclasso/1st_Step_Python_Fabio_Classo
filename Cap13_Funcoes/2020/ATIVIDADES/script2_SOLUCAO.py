

pessoas = {
    1:{'nome':'John', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    2:{'nome':'Jane', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    3:{'nome':'Mary', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    4:{'nome':'Peter', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    5:{'nome':'Harry', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    6:{'nome':'Susan', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    7:{'nome':'Michael', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    8:{'nome':'Jimmy', 'sobrenome':'', 'idade':20, 'sex':'M'},
}

# 1) Inserir um campo, telefone
# print(pessoas[1])
# pessoas[1]['telefone'] = '(48)99177777'
# print(pessoas[1])


def insere_telefone():
    for k, v in pessoas.items():
        # print(k, v)
        v['telefone'] = '(48)99997777'

# 2) Sobrenomes
# pessoas[1]['sobrenome'] = 'Lennon'

lista_de_sobrenomes = ['Lennon', 'Fonda', 'Jane','Parker', 'Potter','Sarandon', 'Jackson', 'Hendrix']


def insere_sobrenome():
    count = 0
    for k, v in pessoas.items():
        #print(k, v)
        v['sobrenome'] = lista_de_sobrenomes[count]
        count += 1
        #print(v)

# 3) email
# nome = pessoas[1]['nome']
# sobrenome = pessoas[1]['sobrenome']
# empresa = 'apple'
#
# email = nome.lower() + '.' + sobrenome.lower() + '@'+ empresa.lower() +'.com'

#print(email)

# criar uma lista de empresas, semelhante o caso (2)
lista_de_empresas = ['Audi', 'VolksWagen', 'Ford', 'BMW', 'FIAT', 'GMC', 'Apple', 'Fender']



lista_de_nomes = []

def get_nomes():
    for k, v in pessoas.items():
        #print(v['nome'])
        lista_de_nomes.append(v['nome'])


lista_de_emails = []
def gera_emails():
    for nome, sobrenome,emp in zip(lista_de_nomes,lista_de_sobrenomes,lista_de_empresas):
        #print(nome, sobrenome, email)
        email = nome.lower() + '.' + sobrenome.lower() + '@'+ emp.lower() + '.com'
        #print(email)
        lista_de_emails.append(email)



def insere_email():
    count = 0
    for k, v in pessoas.items():
        v['email'] = lista_de_emails[count]
        count += 1
        #print(v)



# remover coluna sex
# print(pessoas[1]['sex'])
# # pessoas[1]['sex']
# # print(pessoas[1]['sex'])

def deleta_campo():
    for k, v in pessoas.items():
        #v.pop('sex')
        #v.__delitem__('sex')
        del v['sex']


def atualiza_conteudo():
    for k, v in pessoas.items():
        print(k, v)


def main():
    insere_telefone()
    get_nomes()
    insere_sobrenome()
    gera_emails()
    deleta_campo()
    insere_email()
    atualiza_conteudo()

main()