texto = """
    Former French President Nicolas Sarkozy is to face trial for corruption and influence peddling, prosecutors say.
The case centres on wiretapped phone-calls in 2014, in which Mr Sarkozy allegedly sought to influence a judge who was looking into suspected illegal funding of his 2007 campaign.
The judge and Mr Sarkozy's lawyer have also been ordered to stand trial.
They have all denied wrongdoing. Mr Sarkozy's team says he will appeal against the decision.

In a separate case, the ex-president is accused of receiving campaign funding from late Libyan leader Muammar Gaddafi.

What is Sarkozy accused of?
In 2014, two years after being voted out of office, the former French president reportedly contacted Mr Azibert, then a senior magistrate at France's highest court, the Court of Cassation.

Mr Sarkozy is accused of phoning him and offering to use his contacts to secure a prestigious role in Monaco for Mr Azibert, in exchange for the information on a financing case.

Profile: Nicolas Sarkozy
The call - in which Mr Sarkozy allegedly used the alias Paul Bismuth - was wiretapped by police.

In the funding scandal, Mr Sarkozy was accused of taking cash from L'Oreal heiress Liliane Bettencourt to help him win the 2007 election. He was eventually cleared.

What other investigations does Sarkozy face?
Last week Mr Sarkozy was placed under formal investigation over allegations that he received campaign funding from late Libyan leader Muammar Gaddafi in 2007.

He denies the claims, saying his Libyan accusers want revenge for his decision to send French warplanes during the 2011 uprising.

Mr Sarkozy also faces criminal proceedings over claims that he engaged in accounting fraud to exceed the limit for campaign expenditure in his failed bid for re-election in 2012.

The case is known in France as the Bygmalion affair, after the name of the firm that allegedly provided false invoices to Mr Sarkozy's party rather than the campaign. Mr Sarkozy again denies any wrongdoing.


"""
# contando caracteres
# print(len(texto))
#
#
# # removendo os espacos
# lista_de_caracteres = []
# for num , char in enumerate(texto):
#     if char != ' ':
#         lista_de_caracteres.append(char)
#
# print(len(lista_de_caracteres))
# print(lista_de_caracteres)
#
#
#
# # removendo os espaços
# lista_palavras = texto.split()
# print(lista_palavras)
# for num, palavra in enumerate(lista_palavras):
#     print(num,':', palavra)
#
# print()
# print(f'Qtd de palavras encontradas no texto: {len(lista_palavras)} palavras')




# Procurar o nome Sarkozy
# quantas vezes ele aparece
# 1
contador = 0
for value in texto.split():
    if value == 'Sarkozy':
        #print(value)
        contador += 1
print(contador)
print()

# 2
new_texto  = texto.split()
print(new_texto.count('Sarkozy'))
print()



# 3, contando todas as palavras

# contador = 0
for num, palavra in enumerate(new_texto, start=1):
    print(num, '==>', palavra)

# qt de palavras
#print(len(new_texto))

# lista_de_palavras = []
# for palavra in new_texto:
#     #print(palavra, new_texto.count(palavra))
#     palavras =  {}
#     palavras[palavra] = new_texto.count(palavra)
#     #print(palavras)
#     lista_de_palavras.append(palavras)
#
# print(lista_de_palavras)

#

# print(texto.find('Sarkozy'))

