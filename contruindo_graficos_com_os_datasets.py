# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:52:42 2021

@author: jesap
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

combined = pd.read_csv('combined.csv')
confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")
death = pd.read_csv('time_series_covid_19_deaths.csv') #leitura do dataset com o número de mortos
recovered = pd.read_csv('time_series_covid_19_recovered.csv') #leitura do dataset com o número de recuperados

print('-------------------------------------------------------------------------')
print('\nGráfico de scatterplot extraido com a taxa de letalidade 1 de morte por países com casos confirmados entre 40 e 5000')
plt.figure(figsize=(10,7))
plt.title('Taxa de letalidade 1 de morte por países com casos confirmados entre 40 e 5000')
sns.scatterplot(data=combined.query('confirmed > 40 and confirmed <50000'), x='confirmed', y='tx_letalidade_pais_1')
plt.savefig('taxa_let_1_casos_entre_40_5000')
plt.show()

print('-------------------------------------------------------------------------')
print('\nGráfico de scatterplot extraido com a taxa de letalidade 1 de morte por países com casos confirmados entre 40 e 5000')
plt.figure(figsize=(10,7))
plt.title('Taxa de letalidade 2 de morte por países no total com casos confirmados entre 40 e 5000')
sns.scatterplot(data=combined.query('confirmed > 40 and confirmed <50000'), x='confirmed', y='tx_letalidade_pais_2', color='r')
plt.savefig('taxa_let_2_casos_entre_40_5000')
plt.show()
print('-------------------------------------------------------------------------')

#grafico de distribuição normal padrão
print('\nGráfico de scatterplot extraido com a taxa de letalidade 1 de morte por países com casos confirmados entre 40 e 5000')
plt.figure(figsize=(10,7))
sns.distplot(combined.query('confirmed>40')['tx_letalidade_pais_1'], kde=False, bins=10, color='green')
plt.savefig('taxa_let_2_dist_casos_entre_40_5000')
plt.show()
print('-------------------------------------------------------------------------')

