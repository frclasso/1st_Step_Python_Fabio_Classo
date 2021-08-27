# SET DEFAULT METHOD


# Dictionary with single item
usuario = { 'id': 1001, 'nome': 'Fabio', 'cargo': 'Desenvolvedor de Software'}
 
# using setdefault() method
# quando a chave ewsta presente
identificador = usuario.setdefault('id')
print("User:", usuario)
print("Id:", identificador)


# quandoa chave nao esta presente
print('=' * 60)
email = usuario.setdefault('email')
print("User:", usuario)
print("email:", email)
 
# using setdefault() method
# when key is not in the Dictionary
# but default value is provided
telefone = usuario.setdefault('telefone', '(48)08009001000')
print("User:", usuario)
print("telefone:", telefone)

