import sys
import scrapy
import time
import os

categorias = ['PRO','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','C']
lista = ['M','F']
ano = '2019' #sys.argv[1]
corrida = 'uruguay70.3'

#os.remove('files/' + ano + '-' + corrida + '-full.csv')

print('===> Início Scrap ironmantri.com FULL')
#for corrida in scrapy.all_results():

for sexo in lista:
    for categoria in categorias:    
        scrapy.results_full(ano, corrida, sexo, categoria)

time.sleep(3)
print('===> Gerando um único arquivo')

files = os.listdir('files/')
filenames = [f for f in files if f.endswith('.csv') ]

with open('files/' + ano + '-' + corrida + '-full.csv', 'w') as outfile:
    for fname in filenames:
        with open('files/' + fname) as infile:
            outfile.write(infile.read())

time.sleep(5)
#for fname in filenames:
#    os.remove('files/' + fname)

time.sleep(1)
print('===> Início Upload ftp.doricardo.com')
scrapy.upload()
print('===> Fim')
#To-do: baixar PDFs de start list nos links abaixo
#http://www.ironman.com/triathlon/organizations/pro-membership/event-registration/start-lists.aspx
