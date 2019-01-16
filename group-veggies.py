import csv
import json

vegetables_by_color = {}

with open('veggies.csv') as f:
	vegetables = csv.DictReader(f)
	for veggie in vegetables:
		color = veggie['color']
		if color in vegetables_by_color:
			vegetables_by_color[color].append(veggie)
		else:
			vegetables_by_color[color] = [veggie]
	with open('vegetables_by_color.json', 'w') as f:
		json.dump(vegetables_by_color, f, indent = 2)
