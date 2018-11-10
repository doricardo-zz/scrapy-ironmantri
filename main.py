import sys
import scrapy
#import pandas as pd

lista = ['M','F']
ano = sys.argv[1]
for corrida in scrapy.all_results():
    for sexo in lista:
       scrapy.results(ano, corrida, sexo, 'PRO')

    scrapy.results_brasil(ano, corrida)

#df = pd.read_csv('20180826-sunshinecoast70.3-pro-feminino.csv')
#df['Total'] = pd.to_datetime(df['Total'])
#df['totalsegundos'] = df['Total'].dt.total_seconds()
#print(df.head())

#To-do: baixar PDFs de start list nos links abaixo
#http://www.ironman.com/triathlon/organizations/pro-membership/event-registration/start-lists.aspx
