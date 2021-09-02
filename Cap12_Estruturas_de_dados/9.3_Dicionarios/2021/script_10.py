intrumentos = {
    'piano': '5', 
    'ukulele': '320', 
    'flauta': '432', 
    'guitarra': '45', 
    'violao': '56', 
    'baixo': '34', 
    'saxofone': '78',
    'xilofone':'180',
    'teclado': 84,
    'lira': 25,
    'trumpete': 55
    }

# DESORDENADO
print(intrumentos)
for intrumento in intrumentos:
    print(intrumento)
print()

#ODERNADO
for intrumento in sorted(intrumentos): # reverse=True
    print(intrumento)
print()

def soma_estoque_total():
    estoque_total = []
    for v in intrumentos.values():
        #print(v)
        estoque_total.append(int(v))
    return sum(estoque_total)


print(soma_estoque_total())