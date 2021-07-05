import csv
# criando um .csv a partir de um .txt

with open('tecnologias.txt', 'r') as file_reader:
    with open('tecnologias.csv','w',newline='') as csv_file_writer:
        for lines in file_reader:
            #print(lines,end='')
            writer = csv.writer(csv_file_writer,delimiter=' ')
            writer.writerow(lines.strip().split())
print(f'Arquivo: {csv_file_writer.name} criado com sucesso')