# set comprehension

numbers = { n for n in range(100)}
#print(type(numbers))
#print(numbers)

def pares():
    new_set = set() # set vazio
    for n in range(100):
        if n % 2 == 0:
            new_set.add(n)
    return new_set


def get_pares():
    numbers = { n for n in range(100) if n % 2 == 0} # mais limpo, uma linha de codigo
    return numbers


def nested_sets():
    values = {(x,y) for x in range(3) for y in range(3,6)}
    return values


#print(pares())
#print(get_pares())
print(nested_sets())