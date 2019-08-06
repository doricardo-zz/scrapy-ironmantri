import eel
import scrapy
import json
import time
import os
import sys

eel.init('web')

@eel.expose
def loadRaces():
	#j = json.dumps(scrapy.all_results())
	return scrapy.all_results()

@eel.expose
def loadResults(race):
	agegroups = ['PRO','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','C']
	genders = ['M','F']
	year = '2019'
	print(race)
	for gender in genders:
		for agegroup in agegroups:
			scrapy.results_full(year, race, gender, agegroup)

	time.sleep(3)
	print('===> Gerando um unico arquivo')

	files = os.listdir('files/')
	filenames = [f for f in files if f.endswith('.csv') ]
	
	#os.remove('files/' + year + '-' + race + '-all-athletes.csv')
	
	with open('files/' + year + '-' + race + '-all-athletes.csv', 'w') as outfile:
	    for fname in filenames:
	        with open('files/' + fname) as infile:
	            outfile.write(infile.read())

	for r in filenames:             
		os.remove('files/' + r)

eel.start('index.html')