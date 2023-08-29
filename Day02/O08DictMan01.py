
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'Sachin', 'age': 32, 'runs': 85, 'opponent': 'AUS'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 28), ('runs', 120), ('oppo', 'Eng')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Jack', age=9, cls='3rd', school='nps')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# dictionary maniputlation

player = {'name': 'sachin', 'age': 34, 'runs': 175, 'opponent': 'WI'}
print(f"player :{player}")
print(type(player))

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

for i in player:
    print(i, "\t", player[i])

print("-" * 60)
# modify or update
player['name'] = 'Rahul'
player['opponent'] = 'SA'

print(f"player :{player}")

print("-" * 60)
# add a new key and value
player['loc'] = 'Chepauk'
player['year'] = 1998
print(f"player :{player}")

print("-" * 60)
# delete
del player['opponent']
del player['year']
print(f"player :{player}")

print("-" * 60)
print(dir(player))