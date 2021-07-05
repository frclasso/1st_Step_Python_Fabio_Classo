#!/usr/bin/env python3


# f = open('teste.txt', 'r')  # Error FileNotFoundError: [Errno 2] No such file or directory: 'teste.txt'
#
#
# try:
#     pass
# except:
#     pass


# # descomente o codigo abaixo
# try:
#     f = open('teste.txt', 'r')
# except Exception:
#     print('Arquivo nao encontrado, verifique se o nome foi digitado corretamente.')

# # descomente o codigo abaixo
# try:
#     f = open('teste.txt', 'r')
# except FileNotFoundError:  # podemos usar aliase "as e"
#     print('Arquivo não existe.')
# except Exception:
#     print(''Algo está errado!')


# descomente o codigo abaixo
# try:
#     f = open('test.txt', 'r')
# except FileNotFoundError:  # podemos usar aliase "as e"
#     print('Arquivo não encontrado.')
# except Exception:
#     print(''Algo está errado!')
# else: # executa código caso try nao levante uma exceção
#     print(f.read())
#     f.close()
# finally:
#     print('Finally sempre será executado, com ou sem exceções...')


#descomente o codigo abaixo
try:
    f = open('arquivo_corrompido.txt', 'r')
    if f.name == 'arquivo_corrompido.txt':
        raise Exception
except FileNotFoundError:
    print('Arquivo não encontrado.')
except Exception as e:
    print('Algo está errado!')
else:
    print(f.read())
    f.close()
finally:
    print('Finally sempre será executado, com ou sem exceções...')