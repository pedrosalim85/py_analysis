import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import numpy as np

tree = ET.parse('C:/Users/Pedro/Desktop/PROGRAMACAO/DADOS/ciclones/stormreport.xml')
root = tree.getroot()

data = []
columns = ['StormName', 'Year', 'Basin']  # Altere conforme necessário

for child in root:
    row_data = {col: child.find(col).text if child.find(col) is not None else None for col in columns}
    data.append(row_data)

# Criar o DataFrame
df = pd.DataFrame(data, columns=columns)

# Converter 'Year' para int
df['Year'] = df['Year'].astype(int)

le = LabelEncoder()
df['local'] = le.fit_transform(df['Basin'])

contagem = df['StormName'].value_counts().reset_index()
contagem.columns = ['StormName', 'contagem']

# Mesclar as contagens de volta ao DataFrame original
df_merged = df.merge(contagem, on='StormName')

# Selecionar os últimos 30 anos
ultimos_30_anos = df_merged['Year'].drop_duplicates().sort_values().tail(30)

# Filtrar o DataFrame pelos últimos 30 anos
df_filtrado = df_merged[df_merged['Year'].isin(ultimos_30_anos)]

# Contar a frequência dos itens de coluna1 nos últimos 30 anos
contagem_furacoes = df_filtrado.groupby('Year')['StormName'].count().reset_index()
contagem_furacoes.columns = ['Ano', 'Numero de Furacoes']

X = contagem_furacoes[['Ano']].values.reshape(-1, 1)  # Ano como variável independente
y = contagem_furacoes['Numero de Furacoes'].values  # Número de Furacões como variável dependente

# Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Prever o número de furacões para os próximos 30 anos
anos_futuros = np.arange(contagem_furacoes['Ano'].max() + 1, contagem_furacoes['Ano'].max() + 31).reshape(-1, 1)
previsoes = modelo.predict(anos_futuros)

# Criar um DataFrame para os resultados
df_previsoes = pd.DataFrame({'Ano': anos_futuros.flatten(), 'Numero de Furacoes': previsoes})

# Plotar os dados históricos e as previsões
plt.figure(figsize=(12, 6))

plt.scatter(contagem_furacoes['Ano'], contagem_furacoes['Numero de Furacoes'], color='blue', label='Dados Históricos')
plt.plot(df_previsoes['Ano'], df_previsoes['Numero de Furacoes'], color='red', linestyle='--', label='Previsão')

plt.xlim([contagem_furacoes['Ano'].min() - 1, anos_futuros.max() + 1])
plt.xticks(np.arange(contagem_furacoes['Ano'].min(), anos_futuros.max() + 1, step=2), rotation=45)

plt.xlabel('Ano')
plt.ylabel('Número de Furacões')
plt.title('Previsão do Número de Furacões para os Próximos 30 Anos')
plt.legend()

'''
contagem_furacoes.plot(kind='bar', x='Ano', y='Numero de Furacoes', legend=False, color='blue', title='Número de Furacões por Ano nos Últimos 30 Anos')
plt.xlabel('Ano')
plt.ylabel('Número de Furacões')
plt.xticks(rotation=45)
plt.tight_layout()
'''

plt.show()

