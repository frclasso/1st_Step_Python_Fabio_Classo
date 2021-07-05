my_string = 'Floripa Code Gurus, escola de tecnologia, cursos de Python e Django'
print(enumerate(my_string))
# retorna o endereco de memoria da funcao
#<enumerate object at 0x104c63880>

print(list(enumerate(my_string)))

# usando o for
for num, char in enumerate(my_string):
    print(num, char)