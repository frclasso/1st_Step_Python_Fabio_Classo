#!/usr/bin/env python3

import csv


"""Continuando...
   vamos criar um arquivo a partir de bio_stats.csv separado por '-'
"""
#
# with open('bio_stats.csv', 'r') as csv_file:
#     leitor = csv.reader(csv_file)
#
#     with open('new_bio.csv', 'w') as new_file:
#        # escreve = csv.writer(new_file, delimiter='-')
#         escreve = csv.writer(new_file, delimiter='\t')  # tabs
#
#         for line in leitor:
#             escreve.writerow(line)
#
# print('Done...')


# comente o docigo acima e descomente o abaixo


with open('new_bio.csv', 'r') as csv_file:
    #leitor = csv.reader(csv_file)  # nao passamos o delimitator propositalmente
    leitor = csv.reader(csv_file, delimiter='\t')  # passando o delimitador tab

    for line in leitor:
        print(line)