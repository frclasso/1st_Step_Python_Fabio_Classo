

# metodo write

fabio = {'nome':'Fabio', 'sobrenome':'Classo', 'nacionaldade':'Brasileiro', 'estado_civil':'divorciado',
         'formacao':'Sistemas de Informacao'}


arquivo = open('my_clientes.txt', 'w')
arquivo.write('Arquivo que contem dados de clientes')
arquivo.write('\n')

for k, v in fabio.items():
    print(k, v)
    arquivo.write(k + ' ' + v + '\n')

arquivo.write('\n')

arquivo.close()