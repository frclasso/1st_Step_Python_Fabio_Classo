
empty_string = ''
print(type(empty_string))
print(len(empty_string))
print()

my_string = 'Floripa Code Gurus, escola de tecnologia'
print(len(my_string))
print(f'O primeiro caractere da sttring é: {my_string[0]}')
print(f'O último caractere da sttring é: {my_string[-1]}')
print()
# Lendo parte da string
print(f'Os primeiros 7 caracteres de my_string são: {my_string[:7]}')
print(f'Os primeiros 7 caracteres de my_string são: {my_string[30:]}')
print(my_string[8:18])

# inveterndo a string
print(my_string[::-1])

# Gerando um IndexError
#print(my_string[41])

#new string
new_string = 'f' + my_string[1:]
print(new_string)


# sub funcoes da classe str
print(dir(str))
