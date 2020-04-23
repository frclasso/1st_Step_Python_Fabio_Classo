
import os
# print(os.name)
# print(f'Diretorio atual: {os.getcwd()}')
# print(f'Listando arquivos: {os.listdir()}')
#
#
# print('Crianod um diretorio, os.mkdir()')
# #os.mkdir('aula_07') # comentar para nao executar novamente
# print()
#
# print('Mudando de diretorio: o.chdir()')
# os.chdir('aula_07')
# print(os.getcwd())
# print(f'Listando arquivos: {os.listdir()}')
#
#
# print('Voltando para o diretorio acima...')
# os.chdir('../')
# print(f'Diretorio atual: {os.getcwd()}')
# print()

print('Renomeando diretorio... os.reanme')
#os.rename('aula_07', 'aula_07_new')  # comentar
print(f'Diretorio atual: {os.getcwd()}')
print(f"Listando arquivos: {os.listdir('.')}")
print()

print('Deletando um diretorio, os.rmdir')
#os.rmdir('aula_07_new')  ## comentar
for files in os.listdir('.'):
    print(files)

print()

print('Criando diretorios e subdiretorios')
#os.makedirs('temp/aula_07/os_sys/arquivos')

if not os.path.exists('temp/aula_07/os_sys/arquivos'):
    os.makedirs('temp/aula_07/os_sys/arquivos')
else:
    print('#### Diretorios repetidos ####')


print('Listando conteudo do diretorio e subdiretorio acima')
for root, dirs, files in os.walk('../', topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root,name))


"""Capturando variaveis de ambiente"""
# USER
# HOME
# LOGNAME

print(os.getenv('USER'))