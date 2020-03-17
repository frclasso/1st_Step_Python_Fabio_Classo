#!/usr/bin/env python3

import csv


# Trabalhando com dicionarios

# with open('bio_stats.csv', 'r') as csv_file:
#     leitor = csv.DictReader(csv_file)
#
#     for line in leitor:
#         #print(line)
#         print(line['Name'])

# # comente acima, descomente abaixo
# with open('bio_stats.csv', 'r') as csv_file:
#     leitor = csv.DictReader(csv_file)
#
#
#     # Escrevendo em outro arquivo
#     with open('new_bio.csv', 'w') as new_file:
#         # necessario criar fieldnames
#         fieldnames = ['Name', 'Sex', 'Age',"Height(in)","Weight(lbs)"]
#
#         escreve = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')  # tabs
#
#         escreve.writeheader() # escreve a primeira linha, header
#
#         for line in leitor:
#             escreve.writerow(line)
#
# print('Done...')

# comente acima, descomente abaixo

# deletando uma coluna

with open('bio_stats.csv', 'r') as csv_file:
    leitor = csv.DictReader(csv_file)

    with open('new_bio_del.csv', 'w') as new_file:

        fieldnames = ['Name', 'Sex', 'Age',"Height(in)"] # retirei "Weight(lbs)"

        escreve = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')  # tabs

        escreve.writeheader() # escreve a primeira linha, header

        for line in leitor:
            del line["Weight(lbs)"] # deletando "Weight(lbs)"
            escreve.writerow(line)

print('Done...')

