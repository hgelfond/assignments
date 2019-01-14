import csv
# #write a csv
# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])

# #read from a csv

# with open('testwrite.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# for row in rows:
#     print(rows)

# from pprint import pprint
# pprint(rows)

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('veggies.csv', 'w') as f:
	#write first row
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])
	#loop through veggies
	for v in vegetables:
		length_of_veggie = len(v['name'])
		#write veggie to csv
		writer.writerow([v['name'], v['color'], length_of_veggie])

		