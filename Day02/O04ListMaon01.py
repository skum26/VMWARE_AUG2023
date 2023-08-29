
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.3, 8.2, 9.5, 10+2j, 10-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

print("-" * 60)
# Manipulate the list
# read the elements of the list
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")

for i in l1:
    print(i, end=" ")

print("-" * 60)
# Add or modify (cannot add a new element)
print(f"l1 :{l1}")
l1[3] = 3.5
l1[1] = 10
print(f"l1 :{l1}")

print("-" * 60)
# delete elements
print(f"l1 :{l1}")
del l1[2]
del l1[0]
print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))
