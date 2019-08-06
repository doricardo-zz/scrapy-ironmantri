from bs4 import BeautifulSoup
import json
import urllib.request as request
import csv

pagina = 1
url = ('http://www.smartsource.com.br/unlimited/resultado.php?id=24&pagina={}'.format(10))
response = request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
#atletas = soup.find_all("table", class_="table table-condensed table-hover", href=True)
atletas = soup.find_all("tbody")
##atletas = []
#atletas = soup.find_all("table")

print(atletas)