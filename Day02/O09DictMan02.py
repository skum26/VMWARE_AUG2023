
player = {'name': 'sachin', 'age': 34, 'runs': 175, 'opponent': 'SA', 'loc': 'Chepauk', 'year': 1998}
print(f"player :{player}")

print("keys".center(60, "-"))
ky = player.keys()
print(f"keys :{ky}")
print("-" * 60)

for ky in player.keys():
    print(ky + "=>" + str(player[ky]))

print("values".center(60, "-"))
player = {'name': 'sachin', 'age': 34, 'runs': 175, 'opponent': 'SA', 'loc': 'Chepauk', 'year': 1998}
print(f"player :{player}")

vls = player.values()
print(f"values :{vls}")

print("fromkeys".center(60, "-") )
cities = ['blr', 'che', 'mum', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")

# convert a list into a dictionary
print(dict.fromkeys(cities))
print(dict.fromkeys(cities, 24))

print("get".center(60, "-"))
player = {'name': 'sachin', 'age': 34, 'runs': 175, 'opponent': 'SA', 'loc': 'Chepauk', 'year': 1998}

print(f"Name :{player['name']}")
print(f"Name :{player.get('ag', 'use an appropriate key')}")
print(f"Name :{player.get('year','use an appropriate key')}")

print("pop".center(60, "-"))
player = {'name': 'sachin', 'age': 34, 'runs': 175, 'opponent': 'SA', 'loc': 'Chepauk', 'year': 1998}
print(f"player :{player}")

res = player.pop('age')
print(f"res :{res}")

res = player.pop('loc')
print(f'res :{res}')

print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'sachin', 'age': 34, 'runs': 175, 'opponent': 'SA', 'loc': 'Chepauk', 'year': 1998}
print(f"player :{player}")

print(player.popitem())
print(player.popitem())
print(f"player :{player}")

print("setdefault".center(60, "-"))
# will allow to add only new key value pairs into the dictionary
player = {'name': 'sachin', 'age': 34, 'runs': 175}
print(f"player :{player}")

player.setdefault("runs", 150)
player.setdefault("oppo", "WI")
player.setdefault('loc', 'Sabina Park')
player.setdefault('name', 'Sourav')

print(f"player :{player}")