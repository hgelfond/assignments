#read veggies.csv into a variable vegetabbles 
import csv
import json

with open('veggies.csv') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)

#print vegetables
#print(vegetables)

#convert to JSON


#save json to vegetables.json
with open('testwrite.json', 'w') as f:
	json.dump(vegetables, f, indent =2)