"""
Projeto de uso de pandas
"""

import pandas as pd

# Definindo os dados
df = pd.read_csv(r"dados_analise_FII_24.csv", encoding="latin-1", sep=";")

print(df.head())

print("------------------------------------------------")

df = df.rename(columns={"CNPJ_Fundo":"CNPJ_Fundo",
                "Nome_Fundo": "Fundo_Nome",
                "Data_Referencia": "Referencia",
                "Versao": "Versao",
                "Data_Entrega": "Entrega",
                "Link_Download": "Link_Download",
                "Parecer_Auditor": "Parecer_Auditor"
                })

print(df.head(10))

print("------------------------------------------------")

print(f"Total de linhas e colunas: { df.shape}")

print("------------------------------------------------")

print(f"Colunas: {df.columns}")

print("------------------------------------------------")

print(f"TIpos de dados em uma coluna: {df.dtypes}")

print("------------------------------------------------")
print("Ultimas linhas:")
print(df.tail())

print("------------------------------------------------")
print("Retorna informações estátisticas do conjuto de dados")
print(df.describe())

print("------------------------------------------------")
print("Usando filtro")
print(df['Fundo_Nome'].unique()) # Retorna tudo q for único nessa coluna

centro_textil = df.loc[df['Fundo_Nome'] == 'FUNDO DE INVESTIMENTO IMOBILIï¿½RIO CENTRO TEXTIL INTERNACIONAL']
# EStamos pegando sobre os caso em q a coluna nome tenha o respectivo nome
print(centro_textil.head(3))

print("\n------------------------------------------------\n")
print("Poder tbm usar o grup by")
print(df.groupby('Fundo_Nome')["Parecer_Auditor"].count()) # Retorna a contatem por fundo nome de parecer audiotor

print("\n------------------------------------------------\n")
print(df["Versao"].mean()) # Retorna
