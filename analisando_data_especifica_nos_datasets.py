# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:09:06 2021

@author: jesap
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


combined = pd.read_csv('combined.csv')
confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")
death = pd.read_csv('time_series_covid_19_deaths.csv') #leitura do dataset com o número de mortos
recovered = pd.read_csv('time_series_covid_19_recovered.csv') #leitura do dataset com o número de recuperados

#função para mapear 
def latest_by_country(data):
  return data.groupby('Country/Region').sum().iloc[:,-1] #só queremos a ultima coluna

#fazendo uma selecao de um valor minimo
combined.sort_values('tx_letalidade_pais_1', ascending=True).query('confirmed>40').head()

#analisando para um dia em específico
def latest_by_country_at(data, date):
  return data.groupby('Country/Region').sum()[date] #só queremos a ultima coluna

print('-------------------------------------------------------------------------')
dia='2/20/20'
print('Vamos analisar os dados para o dia'+ ' '+ dia)
latest_by_country_at(confirmed, dia)
latest_by_country_at(confirmed, dia).head

informations = [latest_by_country_at(confirmed, '2/20/20'), latest_by_country_at(death,'2/20/20'), latest_by_country_at(recovered,'2/20/20')]
combined_2_20_20 = pd.concat(informations, axis=1)
combined_2_20_20.columns= ['confirmed', 'death', 'recovered']
print('O dataset construído para esse dia é mostrado abaixo')
print(combined_2_20_20.head())
print('-------------------------------------------------------------------------')

# calculo da taxa de letalidade TOTAL
#sum_up = combined_2_20_20.sum()
print('\nAnalisando as taxas de mortalidade TOTAIS para o dia'+ ' ' + dia)
sum_up = combined_2_20_20.loc['China'] #selecionando só a China
tx_letalidade_1_2_20_20 = sum_up['death'] / sum_up['confirmed']
tx_letalidade_2_2_20_20 = sum_up['death'] / (sum_up['death'] + sum_up['recovered'])

#inserindo as taxas de mortalidade TOTAL 
combined_2_20_20['tx_letalidade_1'] = tx_letalidade_1_2_20_20*100 #incluindo essa series no dataset combined
combined_2_20_20['tx_letalidade_2'] = tx_letalidade_2_2_20_20*100

print('A taxa de letalidade desse conjunto de dados para o dia'+ ' ' + dia + ' ' + 'é de:', tx_letalidade_1_2_20_20*100)
print('A taxa de letalidade desse conjunto de dados para o dia'+ ' ' + dia + ' ' + 'é de:', tx_letalidade_2_2_20_20*100)
print('-------------------------------------------------------------------------')

#lendo o banco de dados com datas diferentes para o número de mortes no dia X 
#e o numero de casos x-T, onde T é o período onde esse caso foi diagnosticado

def latest_by_country_at(data, date):
  return data.groupby('Country/Region').sum()[date] #só queremos a ultima coluna

latest_by_country_at(confirmed, dia)
latest_by_country_at(confirmed, dia).head

#aqui vamos captar uma data para o campo de confirmed e outra em death
informations = [latest_by_country_at(confirmed, '2/8/20'), latest_by_country_at(death,'2/20/20'), latest_by_country_at(recovered,'2/20/20')]
combined_12 = pd.concat(informations, axis=1)

combined_12.columns= ['confirmed', 'death', 'recovered']
print('Analisando as taxas de mortalidade com mais acertividade. Aqui vamos considerar a morte no dia X e o diagnóstico para o dia X-12 dias\n')
print(combined_12)
print('----------------------------------------------------------------------')

# calculo da taxa de letalidade TOTAL
#sum_up = combined_2_20_20.sum()
# print(display(sum_up))
print('\nMostrando a nova taxa de mortalidade apenas para a China\n')
sum_up = combined_12.loc['China'] #selecionando só a China
tx_letalidade_1_12 = sum_up['death'] / sum_up['confirmed']

combined_12['tx_letalidade_1'] = tx_letalidade_1_12*100 #incluindo essa series no dataset combined
print(combined_12.head())
print('\n')
print('\nA taxa de letalidade desse conjunto de dados para a China é de:', tx_letalidade_1_12*100)

