friends = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37
millenials = []
for row in rows:
    if row['age'] < 37:
        millenials.append(row)

print(millenials)

cool_people = []
whitelist = ['Rachel', 'Phoebe']
for friend in friends:
    if friend['name'] in whitelist:
        cool_people.append(friend)

print(cool_people)

cool_people = []
blacklist = ['Monica']
for friend in friends:
    if friend['name'] not in blacklist:
        cool_people.append(friend)

print(cool_people)