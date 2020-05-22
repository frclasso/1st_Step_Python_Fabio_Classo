

arquivo_reader = open('my_clientes.txt', 'r') # r = read/leitura

#print(f'Conteudo do arquivo: {arquivo_reader.name}')

# for d in arquivo_reader:
#     print(d,end='')


# posicoes no arquivo
# tell() - retorna a posição atual do cursor

print(f'Lendo o arquivo: {arquivo_reader.read(18)}')
print(f'Posicao atual do cursor: {arquivo_reader.tell()}')

cursor = arquivo_reader.seek(0)
print(f'Posicao atual do cursor: {arquivo_reader.tell()}')
print()
print(f'Lendo o arquivo: {arquivo_reader.read(18)}')
print(f'Posicao atual do cursor: {arquivo_reader.tell()}')

arquivo_reader.close()