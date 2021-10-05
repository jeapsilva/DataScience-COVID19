# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:32:45 2021

@author: jesap
"""

import pandas as pd

'''Inserindo novos datasets na nossa análise '''

#inserção de novos datasets 
death = pd.read_csv('time_series_covid_19_deaths.csv') #leitura do dataset com o número de mortos
recovered = pd.read_csv('time_series_covid_19_recovered.csv') #leitura do dataset com o número de recuperados
confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")

#visualizando os datasets
#display(death.head())
#display(recovered.head())

#função para mapear 
def latest_by_country(data):
  return data.groupby('Country/Region').sum().iloc[:,-1] #só queremos a ultima coluna

latest_by_country(confirmed)
print('\nImprimindo o número de casos confirmados no último dia do dataset de casos confirmados:\n')
print(latest_by_country(confirmed).head)
print('-------------------------------------------------------------------------')

#criando um array que contêm a última coluna (último dia) do dataset analisado
informations = [latest_by_country(confirmed), latest_by_country(death), latest_by_country(recovered)]
combined = pd.concat(informations, axis=1) #agrupando os dados em colunas e não na vertical

#renomeando as colunas do novo dataset
combined.columns= ['confirmed', 'death', 'recovered']
print('\nO dataset que contêm a última dos datasets originários é mostrado abaixo')
print('\n')
print(combined.head())
print('\n')
print('-------------------------------------------------------------------------')

# calculo da taxa de letalidade TOTAL
print('\nAnalisando métricas dentro do dataset gerado na etapa anterior:')
sum_up = combined.sum() #somando todos os valores em cada coluna
tx_letalidade_1 = sum_up['death'] / sum_up['confirmed']
tx_letalidade_2 = sum_up['death'] / (sum_up['death'] + sum_up['recovered'])

combined['tx_letalidade_1'] = tx_letalidade_1*100 #incluindo essa series no dataset combined
combined['tx_letalidade_2'] = tx_letalidade_2*100

print('\nA taxa de letalidade total levando em conta mortos/confirmados é:', tx_letalidade_1*100)
print('A taxa de letalidade total levando em conta mortos/mortos+recuperados é', tx_letalidade_2*100)
print('\n')
print('-------------------------------------------------------------------------')

# calculo da taxa de letalidade por pais
tx_letalidade_pais_1 = (combined['death']/combined['confirmed'])*100
# print('\n')
# print('A taxa de letalidade por cada país considerando mortos/confirmados é:\n')
# print(tx_letalidade_pais_1)
# print('\n')
#inserindo essa taxa de letalidade como uma coluna 
combined['tx_letalidade_pais_1'] = tx_letalidade_pais_1*100 #incluindo essa series no dataset combined
#print('-------------------------------------------------------------------------')


#calculo da taxa de letalidade por pais
tx_letalidade_pais_2 = combined['death'] / (combined['death'] + combined['recovered'])
#print(tx_letalidade_pais_2)
#inserindo essa taxa de letalidade como uma coluna
combined['tx_letalidade_pais_2'] = tx_letalidade_pais_2*100 #incluindo essa series no dataset combined

#ordenando o novo dataset do maior para o menor
combined.sort_values("tx_letalidade_pais_1", ascending=False).head()
print('\nO novo dataset contendo as colunas de taxa de mortalidade é mostrado abaixo:\n')
print(combined.head())

#extraindo dataset 

combined.to_csv('combined.csv', sep=',',index=False)