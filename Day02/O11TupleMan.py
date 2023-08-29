
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)

t2 = (1, 2, 3, 4.2, 5.9, 6.4, 'seven', 'eight', 'nine', True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 =  tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))


# x = {'a': 1,'b': 2},
# print(x, type(x))

t1 = (1, 2, 3, 4, 5)
l1 = list(t1)
l1.extend([6, 7, 8, 9, 10])
print(f"l1 :{l1}")
t1 = tuple(l1)
print(f"t1 :{t1}")

print("-" * 60)
print(dir(t1))

