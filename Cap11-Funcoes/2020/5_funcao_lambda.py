
# lambda vs funcao

lang = 'Python'
def identidade(x):
    return id(x)

print(identidade(lang))

print((lambda x: id(x))(lang))


soma = lambda x: x + 1
print(soma(2))

"""Você pode aplicar a função acima a um argumento envolvendo a 
função e seu argumento entre parênteses"""

print((lambda x: x + 3)(2))
"""O mesmo que: lambda 2: 2 + 3
                        2 + 3
                            5"""
#
# def soma_val(x):
#     return x + 3
#
# print(soma_val(2))
# print()
#
# print((lambda x, y: x + y)(2,3))
# soma_3 = lambda x, y: x + y
# soma_3(2,3)
# print(soma_3)
# print()

# div_zero = lambda x: x /0
# print(div_zero(2))

# def div_zero_func(x):
#     return x / 0
# print(div_zero_func(5))


"""Argumentos *args"""
print(f'Soma com argumentos *args:  {(lambda *args: sum(args))(1,2,3)}')

"""Argumentos **kwargs"""
print(f'Soma com argumentos **kwargs:{(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)}')




# Nome e sobrenome
nome_completo = lambda nome, sobrenome: f'Nome Completo: {nome.title()} {sobrenome.title()}'
print(nome_completo('fabio', 'CLASSO'))

email_funcional = lambda nome, sobrenome, empresa: nome.lower()+'.'+ sobrenome.lower()+'@'+ empresa.lower()+'.com'
print(email_funcional('Fabio', 'Classo','NEXXERA'))