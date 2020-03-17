#!/usr/bin/env python3

import csv

with open('bio_stats.csv', 'r') as csv_file:
    leitor = csv.reader(csv_file)

    #print(leitor) # imprime o endereço de memória apenas

    # e necessário iterar sobre usando um laço for por exemplo
    # for line in leitor:
    #     #print(line)
    #     print(line[0]) # lendo apenas Name
    #
    # caso queira excluir o cabeçalho, primeira linha
    next(leitor)  # vai começar no segundo parametro, "Alex"
    for line in leitor:
        print(line[0]) # lendo apenas Name
