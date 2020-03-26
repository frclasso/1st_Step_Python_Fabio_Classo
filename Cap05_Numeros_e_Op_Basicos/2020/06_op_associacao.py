# in e not in

minhaLista = ['Python', 'Django', 'Kivy', 'Go', 'Julia', 'R']

print('Python' in minhaLista)
print('Java' in minhaLista)
print('Java' not in minhaLista)

for linguagem in minhaLista:
    if linguagem == 'Python':
        print('Hello Python World!')

pessoa = {'nome':'Fabio', 'empresa':'Nexxera', 'profissao':'Analista de Sistemas'}
print('Fabio' in pessoa.values())
print('nome' in pessoa.keys())
print('nome' in pessoa)