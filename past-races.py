import scrapy

lista = ['M','F']

for corrida in scrapy.races_results():
    for sexo in lista:
        scrapy.results(2018, corrida, sexo, 'PRO')
