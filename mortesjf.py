import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/Pedro/Desktop/PROGRAMACAO/DADOS/sim_cnv_obt10mg101735179_178_228_149.csv', sep=';')

mortesjf = pd.DataFrame(dados)
mortesjf = mortesjf.fillna(0)

cid10_grupos = {
    'Cap I': 'Algumas doenças infecciosas e parasitárias',
    'Cap II': 'Neoplasias (tumores)',
    'Cap III': 'Doenças sanguíneas e dos órgãos hematopoéticos',
    'Cap IV': 'Doenças endócrinas, nutricionais e metabólicas',
    'Cap V': 'Transtornos mentais e comportamentais',
    'Cap VI': 'Doenças do sistema nervoso',
    'Cap VII': 'Doenças do olho e anexos',
    'Cap VIII': 'Doenças do ouvido e da apófise mastoide',
    'Cap IX': 'Doenças do sistema circulatório',
    'Cap X': 'Doenças do sistema respiratório',
    'Cap XI': 'Doenças do sistema digestivo',
    'Cap XII': 'Doenças da pele e do tecido subcutâneo',
    'Cap XIII': 'Doenças do sistema osteomuscular e do tecido conjuntivo',
    'Cap XIV': 'Doenças do sistema geniturinário',
    'Cap XV': 'Gravidez, parto e puerpério',
    'Cap XVI': 'Certas condições originadas no período perinatal',
    'Cap XVII': 'Malformações congênitas e anomalias cromossômicas',
    'Cap XVIII': 'Sintomas, sinais e achados anormais clínicos e laboratoriais',
    'Cap XX': 'Causas externas de morbidade e mortalidade'
}



mortes = pd.DataFrame()

mortes['Cid 10'] = cid10_grupos
mortes['Causalidades'] = mortesjf.iloc[0][1:]

mortes.loc['Cap VII', 'Causalidades'] = 0

print(mortes)
mortes = mortes.sort_values(by='Causalidades', ascending=True)



plt.barh(mortes['Cid 10'], mortes['Causalidades'], color='red')
plt.title('Óbitos no Município de Juiz de Fora em 2023')
plt.tight_layout()
plt.show()