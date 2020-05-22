# lendo um arquivo json

# with open('a_movie.json', 'r') as json_rader:
#     # print(json_rader.read())
#     for lines in json_rader.readlines():
#         print(lines, end='')


# caso queira alterar o conteudo do arquivo


import json

dados = []
with open('a_movie.json', 'r') as json_reader:
    with open('copia_movie.json', 'w') as json_writer:
        data = json.load(json_reader)
        #print(f'Type: {type(data)}')
        #print(data)
        data['Country'] = 'Brasil'
        json.dump(data, json_writer, indent=1)



# Conferindo
with open('copia_movie.json', 'r') as json_to_read:
    for line in json_to_read.readlines():
        print(line, end='')
