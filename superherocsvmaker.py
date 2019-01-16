import json
import csv

#read superhero.json
with open('superheroes.json') as f:
	superheroes = json.load(f)

#loop through each member
members = superheroes['members']
for member in members:
	print(member)

#get powers
# data = []
# for member in members:
#     #for each member get a list of the powers
#     powers = member['powers']
#     #print(powers)
# #loop through the powers and print each one
#     for power in powers:
#         data.append(power)

# #save data for each member into csv row


with open('members.csv', 'w') as f:
    writer = csv.writer(f)
    header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
    writer.writerow(header)
    for member in members:
        row =  [
        	member['name'],
        	member['age'],
            member['secretIdentity'],
            str(member['powers']),
            superheroes['squadName'],
            superheroes['homeTown'],
            superheroes['formed'],
            superheroes['secretBase'],
            superheroes['active']
        ]
        writer.writerow(row)