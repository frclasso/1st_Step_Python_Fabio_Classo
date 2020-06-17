
" Programa principal, onde comandaremos os demais "

# fazer o import dos módulos


import os

from my_software.downloader import cria_diretorio_saida, get_file
from my_software.field_validator import (get_file_local, get_uma_linha, get_email,
                                          valida_telefone, valida_data,
                                          cliente_valido, cria_diretorio_de_saida,
                                          validador)


# executar as tarefas conforme o planejado nas aulas

# 1) Obter a base de dados (clientes_atualizados.py)

url = 'https://f001.backblazeb2.com/file/Datasets-gurus/clientes_autalizado.py'



# 2) criar um diretorio para salvar o arquivo localmente

cria_dir = cria_diretorio_saida() # chamada da função que criar um diretorio para salvar o arquivo a ser baixado
print(f"{cria_diretorio_saida.__name__}: {cria_dir}")


file = get_file(url, cria_dir) # chamada da função que recebe a url do arquivo pra downlaod e o diretorio
# para escrever o mesmo
print(f"{get_file.__name__}: {file}")



# 3 )
# Acessar o arquivo localmente, NAO Esquecer de DESABILITAR a funcao que faz o download, do contrário vai fazer
# # download novamente (desnecessario), o mesmo para a função que cria o diretorio

local_file = get_file_local()

# 4)
# Validar campos
linha = get_uma_linha()

email = get_email()

telefone = valida_telefone()

data_valida = valida_data()


# 5)
# É hora de salvar nossos dados definitivamente, vamos criar um arquivo local com os dados salvos
# Execute o validador em todas as linhas do arquivo, nao esqueça de executar as funções
# cria_diretorio_de_saida  e cliente_valido() DENTRO do validador()



