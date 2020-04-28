import os

print(f'Sistema operacional: {os.name}')
print(f'Diretorio atual: {os.getcwd()}')
print(f'Conteudo do diretorio atual: {os.listdir()}')
print(os.system('ls -la'))