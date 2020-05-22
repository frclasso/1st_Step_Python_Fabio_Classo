

# A função Open()

arquivo = open('teste.txt', 'w')  # em modo escrita 'w', se o arquivo não existir, será criado em tempo de execução.


# Alguns atributos básicos
# file.closed - retorna True se o arquivo está fechado, do contrário False
# file.mode - Retorna modo de acesso com o qual arquivo foi aberto (w, r, a, w+, r+, wb, ab, a+ , ab+)
# file.name  - retorna o nome do arquivo

print(f'{arquivo.closed}')
print(f'Mode de execução: {arquivo.mode}')
print(f'Nome do arquivo: {arquivo.name}')


# medoto close() - fecha o arquivo, não é possivel modificar o arquivo após fechamento, é necessario abrir novamente
arquivo.close()
if arquivo.closed:
    print(f'Arquivo fechado -- {arquivo.closed}')


def criar_arquivo():
    arquivo = open('teste2.txt', 'w')

    return

