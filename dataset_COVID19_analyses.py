# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:52:42 2021

@author: jesap
"""

import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt

confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")

print('O tamanho do dataset é de' + ' ' + str(confirmed.shape[0])+ ' '+ 'linhas.')
print('-------------------------------------------------------------------------')

print('\nO início do dataset com os casos confirmados é mostrado abaixo:\n')
print(confirmed.head())
print('-------------------------------------------------------------------------')

print('\nContando quantas vezes aparecem as cidades que estão no dataset  de casos confirmados:\n')
print(confirmed['Country/Region'].value_counts())
print('-------------------------------------------------------------------------')

confirmed['Country/Region']
print('\nOs países que possuem casos confirmados de COVID até o momento são:\n')
print(confirmed['Country/Region'].unique())
print('-------------------------------------------------------------------------')

#selecionando uma linha em específico nesse dataset
confirmed.iloc[0] #localiza pelo indice
confirmed.set_index('Province/State').loc['Anhui'] #localiza pela palavra no campo

#agrupando os valores por país
confirmed_by_country = confirmed.groupby("Country/Region").sum() #somando todos os casos de covid em cada país

print('-------------------------------------------------------------------------')

'''Plotando gráficos com o dataset de casos confirmados'''

#plotando um grafico  de linha do COVID para a CHINA
plt.figure(figsize=(18,10))
plt.title('Numero de casos confirmados de COVID na CHINA')
confirmed_by_country.loc['China'][2:].plot(ylabel='Pessoas',grid=True)
plt.savefig('casos_confirmados_CHINA.png')
plt.show()

#plot da derivada do número de casos na CHINA (velocidade de crescimento)
new_cases_china = confirmed_by_country.loc['China'][2:].diff().dropna()
plt.figure(figsize=(18,10))
plt.title('Derivada do numero de casos de COVID-19 na China')
new_cases_china.plot(ylabel='Derivada',grid=True)
plt.show()

#imprimindo grafico de barras de uma data especifica para todos os países
plt.figure(figsize=(18,10))
plt.title('Confirmados por país na data de 29/09/2021')
confirmed_by_country['9/29/21'].sort_values(ascending=False)[0:10].plot(ylabel='Derivada',kind='bar',grid=True)
plt.show()
print('-------------------------------------------------------------------------')
