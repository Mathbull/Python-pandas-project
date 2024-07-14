"""
Usando python para trabalhar com dados do xlsx

"""
import pandas as pd

df1 = pd.read_excel('part1.xlsx', sheet_name='Plan1')
df2 = pd.read_excel('part2.xlsx', sheet_name='Plan1')
df3 = pd.read_excel('part3.xlsx', sheet_name='Plan1')
# todas os xlsx tem q ter a msm estrutura

print(df1.head())

print('----------------------------------------------------------------')
print("Concatenando todas as 3 execels")
print('----------------------------------------------------------------')
df = pd.concat([df1, df2, df3])
print('----------------------------------------------------------------')
print("Cabeçalho")
print(df.head())
print('----------------------------------------------------------------')
print("Rodapé")
print(df.tail())

print('----------------------------------------------------------------')
print('Amostra')
print(df.sample(4))

print('----------------------------------------------------------------')
print('Tpos de dados de cada coluna')
print(df.dtypes)


print('----------------------------------------------------------------')
print('Alterando tipos de dados de coluna')
df["Id"] = df["Id"].astype("object")
print(df.dtypes)


print('----------------------------------------------------------------')
print('Verificando valores null')
print(df.isnull().sum())

print('----------------------------------------------------------------')
print('Alterando valores null para Sem emails')
df["Email"].fillna('Sem emails', inplace=True)
print(df['Email'].count())

print('----------------------------------------------------------------')
print('Apagando valores null')
print(df.dropna())

print('----------------------------------------------------------------')
print('Apgando os valores null apenas de uma coluna')
print(df.dropna(subset=['Email']))

print('----------------------------------------------------------------')
print('Criando novas colunas')
df['new_column'] = df["_id"] / (df['Id'])
print(df.head())

print('----------------------------------------------------------------')
print('Pegar o max de uma coluna')
print(df['Id'].max())

print('----------------------------------------------------------------')
print('PEgando o max de 3 coluna e a linha com esse max')
print(df.nlargest(3, "Ano"))

print('----------------------------------------------------------------')
print('PEgando o max de as 3 coluna e a linha com esse min')
print(df.nsmallest(3, "Ano"))

print('----------------------------------------------------------------')
print('Agrupando por municipio e contanto')
print(df.groupby('Municipio')['Escola'].count())


print('----------------------------------------------------------------')
print('Ordenando')
print(df.sort_values('Municipio', ascending=False).head())