#!/usr/bin/env python3

import os
import time

def backup():
    # origem, dinamica  - input
    source = '/Users/fabio/Desktop/turma3_Python1_2018/Cap16_Files/imgs'

    # destino, dinamica  - input
    target_dir = '/Users/fabio/Desktop/backup'

    # zipar/compactar os arquivos
    # como nome, a data
    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

    # se o diretorio nao existir previamente, crie
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # usando o comando zip
    zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))


    # rodando zip
    print('Zipping...')
    print(zip_command)

    if os.system(zip_command) == 0:
        print("Backup executado com sucesso em: ", target)
    else:
        print("Falha ao realizar backup")


def timer():
    while True:
        seconds = 4  # QUANTIDADE DE SEGUNDOS PARA O PROXIMO BACKUP
        while seconds != 0:
            print(f"Proximo Backup em  {seconds} segundos ...")  # comentar, isso é teste
            time.sleep(4) # 4 seguns=dos
            seconds -=1
        print('Feito...')


def main():
    timer()
    backup()


if __name__=="__main__":main()