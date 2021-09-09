from __future__ import annotations
import os
import csv

os.chdir("C:/Users/fabio.classo/Downloads/fabio/aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/9.3_Dicionarios/2021")
#print(os.getcwd())

def get_estoque():
    """Retorna o estoque na base de dados"""
    with open("intrumentos_musicais.csv", "r") as file_reader:     
        data = csv.reader(file_reader)
        
        # for line in data:
        #     print(line)
        
        keys, values = data
        #print(keys)    
        #print(values)    
        estoque = dict(zip(keys, values))
        #estoque = sorted(dict(zip(keys, values)))  # FALAR DO SORTED
        
        #print(estoque)
        return estoque 

print(get_estoque())

# 1
def verifica_qtd_instrumento_em_estoque(instrumento):
    """Verfica a quantidade existente em estoque de um produto especifico"""
    estoque = get_estoque()
    if not instrumento in estoque:
        return
    else:
        for key, value in estoque.items():
            if key == instrumento:
                return value


# 2 usando dict.get()
def verifica_qtd_instrumento_em_estoque_2(instrumento):
    """Verfica a quantidade existente em estoque de um produto especifico"""
    estoque = get_estoque()
    value = estoque.get(instrumento)
    return value

    
#print(verifica_qtd_instrumento_em_estoque("piano"))
#print(verifica_qtd_instrumento_em_estoque_2("piano"))

# 4
def atualiza_estoque_base_de_dados(velho_estoque):
    """Atualiza a base de dados"""

    #with open("estoque_atualizado.csv", "w", newline='') as csvfile: # alterar nome do arquvo
    with open("estoque_atualizado.csv", "w", newline='') as csvfile: 
        writer = csv.writer(csvfile, delimiter=',')
        #teste = {"piano":100, "sax":30 }
        writer.writerow(velho_estoque.keys())
        writer.writerow(velho_estoque.values())

#atualiza_estoque_base_de_dados()

# 3 - vendas 
def venda_intrumento(instrumento, venda=0):

    """Realiza uma venda"""

    estoque = get_estoque()
    #print(estoque)
    #print(verifica_qtd_instrumento_em_estoque_2(instrumento))
    value = int(estoque.get(instrumento))
    value -= venda
    #print(value)
    estoque[instrumento] = value
    #print(estoque)
    atualiza_estoque_base_de_dados(estoque) # 4.1
    return estoque

#print(f"Venda realizada, estoque atual: {venda_intrumento('piano', 1)}")

# 5 novo estoque


def entrada_no_estoque(**kwargs):
    """Realiza multiplas entradas no estoque"""

    # lendo velho
    estoque = get_estoque()
    
    # for k, v in estoque.items():
    #     print(k, v)
    entrada = kwargs.items()
    print("ENTRADA")
    print(entrada)
    # print(type(entrada))
    #print(dict(entrada))
    key = dict(entrada)
    print(key)
    for k, v in key.items():
        #print(k, v)
        if k in estoque:
            #print(k, estoque[k])
            qtd_atualizada = v +  int(estoque[k])
            #print(qtd_atualizada)
            print(f"Produto: {k} , old_qtd: {estoque[k]}, new:{qtd_atualizada}")
            estoque[k] = qtd_atualizada
    #print(estoque)
    atualiza_estoque_base_de_dados(estoque)
    return estoque


print(entrada_no_estoque(piano = 24, flauta = 10))

def insere_novo_produto_no_catalogo(produto, qtd=None):

    """Insere um novo produto no catalogo"""

    catalogo = get_estoque()
    catalogo.update({produto: qtd})
    atualiza_estoque_base_de_dados(catalogo)
    return catalogo

#print(insere_novo_produto_no_catalogo("clarinete", 37))

def remove_produto_do_catalogo(produto):
    """Remove um item do catalogo juntamente com seus respectivos valores"""
    catalogo = get_estoque()
    if not produto in catalogo:
        return
    catalogo.__delitem__(produto)
    print(catalogo)

remove_produto_do_catalogo("clarinete")