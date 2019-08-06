import scrapy

lista = ['M','F']

for corrida in scrapy.live_results():
    for sexo in lista:
        scrapy.results(2019, corrida, sexo, 'PRO')
