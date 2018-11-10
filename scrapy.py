import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse
import csv

def nome_arquivo(data, corrida, sexo, categoria):

    if sexo.upper() == 'M':
        sexo = 'masculino'
    elif sexo.upper() == 'F':
        sexo = 'feminino'
    else:
        sexo = 'todos'

    return '{}-{}-{}-{}.csv'.format(data.replace('-',''), corrida, categoria.lower(), sexo )

def live_results():
    url = ('http://www.ironman.com/triathlon/coverage/live.aspx')
    r = requests.get(url)
    #status = r.status_code
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all("a", class_="imageLink", href=True)
    corridas = []
    for link in links:
        href = link['href']
        corridas.append(urlparse(href).query.split('&')[0].split('=')[1])
    return corridas

def races_results():
    url = ('http://www.ironman.com/triathlon/coverage/past.aspx')
    r = requests.get(url)
    #status = r.status_code
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all("a", class_="imageLink", href=True)
    corridas = []
    for link in links:
        href = link['href']
        corridas.append(urlparse(href).query.split('&')[0].split('=')[1])
    return corridas

def all_results():
    corridas = live_results()
    corridas += races_results()

    return corridas

def results_brasil(ano, corrida):

    return results(ano, corrida, '', '', 'BRA')

def results_todos(ano, corrida):

    return results_novo(ano, corrida)

def results(ano, corrida, sexo, categoria, pais=''):
    #pais=> &loc=BRA
    #http://m.ironman.com/Handlers/EventLiveResultsMobile.aspx?year=2017&race=worldchampionship70.3&loc=BRA
    url = ('http://m.ironman.com/Handlers/EventLiveResultsMobile.aspx?year={}&race={}&sex={}&agegroup={}&loc={}'.format(ano, corrida, sexo, categoria, pais))

    r = requests.get(url)
    status = r.status_code

    if status == 200 :

        dictionary = json.loads(r.content)

        if dictionary['records'] and len(dictionary['records']) > 1:

            data = dictionary['raceDate']
            resultados = dictionary['records']
            arquivo = nome_arquivo(data, corrida, sexo, categoria)
            with open('files/' + arquivo, 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)#, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)

                linha = [ 'Pos', 'Nome', 'Pais', 'Swim', 'Bike', 'Run', 'Total' ]

                if categoria == 'PRO':
                    linha[2] = 'Pais'
                else:
                    linha[0] = 'Pos Categ'
                    linha[2] = 'Categ'
                spamwriter.writerow(linha)

                for resultado in resultados:

                    if resultado['Time'].find('--') != 0:

                        if categoria == 'PRO':
                            linha = [ resultado['AgeRank'], resultado['Name'].upper(), resultado['Country'], resultado['SwimTime'],
                                      resultado['BikeTime'], resultado['RunTime'], resultado['Time'] ]
                        else:

                            if categoria == '':
                                linha = [ resultado['OverallRank'], resultado['Name'].upper(), resultado['AgeGroup'], resultado['SwimTime'],
                                          resultado['BikeTime'], resultado['RunTime'], resultado['Time'] ]
                            else:
                                linha = [ resultado['AgeRank'], resultado['Name'].upper(), resultado['AgeGroup'], resultado['SwimTime'],
                                          resultado['BikeTime'], resultado['RunTime'], resultado['Time'] ]

                        if linha[0] != '99999':
                            spamwriter.writerow(linha)

                if linha != '':
                    print("OK.: " + arquivo)
        else:

            print('ERR: Não disponível: {} {} {}'.format(corrida, sexo, categoria))

def results_brasil(ano, corrida):

    categoria = 'brasileiros'
    country = 'BRA'
    pagina = 1
    total  = 1
    sexo = 'todos'

    url = ('http://m.ironman.com/Handlers/EventLiveResultsMobile.aspx?year={}&race={}&loc={}'.format(ano, corrida, country))
    r = requests.get(url)
    status = r.status_code

    if status == 200:

        dictionary = json.loads(r.content)

        if dictionary['records'] and len(dictionary['records']) > 1:
            total = dictionary['lastPage']
            data = dictionary['raceDate']
    #####
            arquivo = '{}-{}-{}-{}.csv'.format( data.replace('-',''), corrida, categoria.lower(), sexo )
            with open('files/' + arquivo, 'w', newline='') as csvfile:
    #####
                while pagina < total:

                    url = ('http://m.ironman.com/Handlers/EventLiveResultsMobile.aspx?year={}&race={}&loc={}&p={}'.format(ano, corrida, country, pagina))
                    r = requests.get(url)
                    status = r.status_code

                    if status == 200:

                        dictionary = json.loads(r.content)

                        if dictionary['records'] and len(dictionary['records']) > 1:

                            resultados = dictionary['records']
        #####
        #####
                            spamwriter = csv.writer(csvfile)#, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                            linha = [ 'Pos', 'Nome', 'Pais', 'Swim', 'Bike', 'Run', 'Total' ]

                            if categoria == 'PRO':
                                linha[2] = 'Pais'
                            else:
                                linha[2] = 'Categ'
                            spamwriter.writerow(linha)

                            for resultado in resultados:

                                if resultado['Time'].find('--') != 0:

                                    if categoria == 'PRO':
                                        linha = [ resultado['AgeRank'], resultado['Name'].upper(), resultado['Country'], resultado['SwimTime'],
                                                  resultado['BikeTime'], resultado['RunTime'], resultado['Time'] ]
                                    else:

                                        if categoria == '':
                                            linha = [ resultado['OverallRank'], resultado['Name'].upper(), resultado['AgeGroup'], resultado['SwimTime'],
                                                      resultado['BikeTime'], resultado['RunTime'], resultado['Time'] ]
                                        else:
                                            linha = [ resultado['AgeRank'], resultado['Name'].upper(), resultado['AgeGroup'], resultado['SwimTime'],
                                                      resultado['BikeTime'], resultado['RunTime'], resultado['Time'] ]

                                    if linha[0] != '99999':
                                        spamwriter.writerow(linha)

                            #if linha != '':
                            #    print("OK.: " + arquivo)
                        else:

                            print('ERR: Não disponível: {} {} {}'.format(corrida, sexo, categoria))

                    pagina += 1

                if pagina > 0:
                    print("OK.: " + arquivo)

if __name__ == "__main__":
    ano = 2018
    corridas = live_results()
    corridas += races_results()
    corrida = corridas[ int(input('Informe a corrida {}: '.format(corridas))) ]
    sexo = input('Informe (M)asculino (F)eminino: ')
    categoria = input('Informe a categoria (PRO, 25-29): ')
    results(ano, corrida, sexo, categoria)