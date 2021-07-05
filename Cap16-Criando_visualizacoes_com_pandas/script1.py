import pandas as pd

data = pd.read_csv('feira.csv')
#print(data.info)
#print(data.head)

# df = pd.DataFrame(data)
# print(df.head())
# print(df.info())

df2 = pd.DataFrame(data, columns=['PRODUCE', 'COST PER POUND','POUNDS SOLD','TOTAL'])
#print(df2.head(10))
#print(df2.tail(100))

produtos = df2['PRODUCE']
custo_por_libra = df2['COST PER POUND']
libras_vendidas = df2['POUNDS SOLD']
# total = df2['TOTAL']
# print(total.head().fillna(0))
# total =total.head().fillna(0)


df3 = pd.DataFrame(data, columns=['PRODUCE', 'COST PER POUND','POUNDS SOLD'])
#print(df3.head())

total = custo_por_libra * libras_vendidas
df3['TOTAL'] = total
print(df3.head(10))

print()
print('Informações do produto mais caro')
print(max(df3['TOTAL']))
print()
print(df3.loc[df3['TOTAL'].idxmax()])
print()
print('Produto mais barato')
print(min(df3['TOTAL']))
print()

#total de vendas
print(f"Total vendido: {sum(df3['TOTAL']):.2f}")

soma_totais = df3['TOTAL'].sum(axis=0, skipna=True)
# print(soma_totais)

soma_totais2 = df3['TOTAL'].sum().round(2)
print(soma_totais2)




# gerando arquivos .csv atualizado
#df3.to_csv('feira_atualizado.csv')

import matplotlib.pyplot as plt

ax = plt.gca()
df3.plot(kind='bar', x='COST PER POUND', y='POUNDS SOLD')
# df3.plot(kind='line', x='COST PER POUND', y='POUNDS SOLD',color='red', ax=ax)
plt.show()