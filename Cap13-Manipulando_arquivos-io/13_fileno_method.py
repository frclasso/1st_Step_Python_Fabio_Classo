#!/usr/bin/env python3

fo = open('foo.txt','wb')
print("Nome do arquivo: ", fo.name)
fid =  fo.fileno()
print("Descritor do arquivo: ", fid)
fo.close()

"""Para saber o que eh um descritor:
https://pt.wikipedia.org/wiki/Descritor_de_arquivo
"""