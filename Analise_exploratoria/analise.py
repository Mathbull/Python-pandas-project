"""

"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

df = pd.read_excel('filtro_Dados_explorar.xlsx', sheet_name='Sales_data')

df = df.drop(columns=['SalesOrderLineKey', 'OrderDateKey', 'CustomerKey', 'ResellerKey','Sales Amount',
                    'Total Product Cost', 'Extended Amount', 'Unit Price Discount Pct', 'Product Standard Cost', 'SalesTerritoryKey'])


print()
print('--------------------------------')
print('Estrutura dos dados')
print(df.dtypes)

df = df.rename(columns={'Order Quantity':'QTD',
                        'Unit Price': 'Preco unitario'} )
print(df.head(5))


print()
print('--------------------------------')
print('Criando coluna de valor venda')
df['Valor venda'] =  (df['Preco unitario'] + (df['Preco unitario'].mul(0.3))).mul(df['QTD'])
print(df.sample(10))

print()
print('--------------------------------')
print('Receita toatal')
print(df['Valor venda'].sum())



print()
print('-'*60)
print('Custo prexo x qtd')
df['Custo'] = df['Preco unitario'].mul(df['QTD'])
print(df.sample(10))

print()
print('-'*60)
print('Custo total')
print(round(df['Custo'].sum(),2))


print()
print('--------------------------------')
print('Criando coluna de lucro')
df['Lucro'] =  df['Valor venda'] - (df['Custo'])
print(df.sample(10))

print()
print('--------------------------------')
print('TOtal de lucro')
print(round(df['Lucro'].sum(),2))

print()
print('--------------------------------')
print('Coluna tempo de envio')
df['Tempo envio'] = df['Data chegada'] - df['Data envio'] 
print(df.sample(10))

print()
print('--------------------------------')
print('Media de tempo de envio de cada produto')
print(df.groupby('Product')['Tempo envio'].mean())

print()
print('--------------------------------')
print('Verificar se há valores nulos')
print(df.isnull().sum())

print()
print('--------------------------------')
print('Lucro por ano de cada produto')
print(df.groupby([df['Data envio'].dt.year, 'Product'])['Lucro'].sum()   )

print()
print('--------------------------------')
print('Total de produtos ventidos')
print(df.groupby('Product')['QTD'].sum().sort_values(ascending=False))


print()
print('--------------------------------')
print('Lucro por ano de cada produto grafico')
print(df.groupby([df['Data envio'].dt.year])['Lucro'].sum().plot(title='Luxo x ano')   )


print()
print('--------------------------------')
print('Grafico toal de produtos vendidos')
df = df.nlargest(40, 'QTD')
df.groupby('Product')['QTD'].sum().sort_values(ascending=False).plot.barh(title='Total de produtos venditos')
plt.ylabel('Produtos')
plt.xlabel('total QTD')


print()
print('--------------------------------')
print('Grafico de Boxplot')
#plt.boxplot(df['Data envio'])
plt.show()
