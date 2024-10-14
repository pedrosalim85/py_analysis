import pandas as pd
import os
import glob

bilheteria = 'C:/Users/Pedro/Desktop/PROGRAMACAO/DADOS/bilheteria/json/2024/'
arquivos_json = glob.glob(os.path.join(bilheteria, "*.json"))

dataframes = []

for arquivo in arquivos_json:

  dado = pd.read_json(arquivo)
  records = dado['data']

  records_data = [] 
  for record in records: 
    record_data = [ 
      record['DATA_EXIBICAO'], 
      record['TITULO_ORIGINAL'],
      record['PAIS_OBRA'],
      record['UF_SALA_COMPLEXO'],
      record['MUNICIPIO_SALA_COMPLEXO'],
      record['PUBLICO'],
      record['NOME_SALA'],
      ]
    records_data.append(record_data) 

  colunas = ['DATA_EXIBICAO', 'TITULO_ORIGINAL', 'PAIS_OBRA', 'UF_SALA_COMPLEXO', 'MUNICIPIO_SALA_COMPLEXO', 'PUBLICO', 'NOME_SALA']
  df = pd.DataFrame(records_data, columns=colunas)
  dataframes.append(df)

bilheteria_2024 = pd.concat(dataframes, ignore_index=True)

df_brasil = bilheteria_2024.loc[bilheteria_2024['PAIS_OBRA']=='BRASIL']
melhores_bra = df_brasil.sort_values('PUBLICO', ascending=False)

#print(melhores_bra.head(20))

df_grouped = df_brasil.groupby('TITULO_ORIGINAL')['PUBLICO'].sum().reset_index().sort_values('PUBLICO', ascending=False)
print(df_grouped.head(10))
