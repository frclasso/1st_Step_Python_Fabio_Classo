
# listas

clubes_sc = ['Figueirense', 'Avai', 'Chapecoense', 'Joiville']
print(type(clubes_sc))
print(clubes_sc)
# indices iniciam por zero (0)
print(clubes_sc[0])
print(clubes_sc[3])
print(clubes_sc[-1])
print(clubes_sc[-2])
print(clubes_sc[-3])
print(clubes_sc[-4])
# invertendo
print(clubes_sc[::-1])
# print(clubes_sc * 3)

clubes_rj = ['Flamengo', 'Vasco', 'Botafogo', 'Fluminense']

# concatenacao +
print(clubes_sc)
print(clubes_rj)
print(clubes_sc + clubes_rj)
print()
campeonato_sul_sudeste = clubes_sc + clubes_rj
print(campeonato_sul_sudeste)
print()

print(campeonato_sul_sudeste[:3]) # fatiar/slice
print(campeonato_sul_sudeste[2:6]) # limite inicial : final