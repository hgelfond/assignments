import csv
import json
#read vegetables.csv

#filter to only green vegetables
#print veggies to terminal


green_veggies = []

with open('veggies.csv') as f:
	vegetables = csv.DictReader(f)
	for vegetable in vegetables:
		if vegetable['color'] == 'green':
			green_veggies.append(vegetable['name'])


#attempt to write to csv
# with open('green_vegetables.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	header = ["vegetable"]
# 	writer.writerow(header)
# 	for veggie in green_veggies:
# 		writer.writerrow(veggie)

print(green_veggies)

