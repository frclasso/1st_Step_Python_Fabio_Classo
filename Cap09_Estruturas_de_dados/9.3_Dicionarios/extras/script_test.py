
register = []

labels = {
    '2':'Confirmado',
    '3':'liquidado',
    '4':'cancelado'
}

rows = ['pedra', 'papel', 'tesoura', '2']
for r in rows:pass
register.append(
    {'group':rows[0],
     'campny':rows[1],
     'value':rows[2],
     'situation':rows[3]}
)

for r in register:
    print(r)

for l,value in zip(register, labels.items()):
    if l['situation'] == value[0]:
        l['situation'] = value[1]
    else:pass


print()
for r in register:
    print(r)
