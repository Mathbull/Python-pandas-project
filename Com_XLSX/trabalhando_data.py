"""
Usando python para trabalhar com dados do xlsx
trabalahndo com datas

"""
import pandas as pd

df1 = pd.read_excel('part1.xlsx', sheet_name='Plan1')
df2 = pd.read_excel('part2.xlsx', sheet_name='Plan1')
df3 = pd.read_excel('part3.xlsx', sheet_name='Plan1')
# todas os xlsx tem q ter a msm estrutura

df = pd.concat([df1, df2, df3])

df["data"] = '19/07/2015'

print(df.dtypes)

print('----------------------------------------------------------------')
print('Convertendo para data e hora')
df["data"] = pd.to_datetime(df["data"])
print(df.dtypes)