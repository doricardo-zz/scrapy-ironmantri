import sys
import scrapy
import time

lista = ['M','F']
ano = sys.argv[1]

print('===> Início Scrap ironmantri.com')
for corrida in scrapy.all_results():
#for corrida in scrapy.live_results():
    for sexo in lista:
       scrapy.results(ano, corrida, sexo, 'PRO')

    scrapy.results_brasil(ano, corrida)

time.sleep(1)
print('===> Gerando indíce de corridas. PENDENTE')


time.sleep(1)
print('===> Início Upload ftp.doricardo.com')
scrapy.upload()
print('===> Fim')
#To-do: baixar PDFs de start list nos links abaixo
#http://www.ironman.com/triathlon/organizations/pro-membership/event-registration/start-lists.aspx
