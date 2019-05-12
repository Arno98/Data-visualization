import json

filename = 'population_data_3.json'
with open(filename) as datafile:
	data = json.load(datafile)
	
for dictionary in data:
	if dictionary['Year'] == 2016:
		country_name = dictionary['Country Name']
		population = dictionary['Value']
		print(country_name + " : " + str(population))
