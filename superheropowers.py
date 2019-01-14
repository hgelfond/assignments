#load libraries
import json

#read superhero.json
with open('superheroes.json') as f:
	superheroes = json.load(f)

data = []

#get the members
members = superheroes['members']
#print(members)

#loop through each member
for member in members:
	#for each member get a list of the powers
	powers = member['powers']
	#print(powers)

#loop through the powers and print each one
	for power in powers:
		data.append(power)
#make the list unique
unique_powers = list(set(data))
print(unique_powers)