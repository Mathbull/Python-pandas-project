"""
visualizaçao de dados com pandas
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('part1.xlsx', sheet_name='Plan1')


print('--------------------------------')
print(df['Municipio'].value_counts(ascending=False))

print('--------------------------------')
print('Usando lib pra grafico')

df['Municipio'].value_counts(ascending=False).plot(marker='v')

plt.show()