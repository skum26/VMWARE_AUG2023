
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 'nine', True, False, 12+1j, 12-0j}
print(f's2 :{s2}')

print("-" * 60)
s3 = set(range(1, 6))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
s1 = {1,2,3}
print(f"s1 :{s1}")
# add, update
s1.add(2)
s1.add(4)
s1.add(1)
s1.add(5)
print(f"s1 :{s1}")
s1.update([1, 2, 3])
s1.update([4, 5, 6])
s1.update([7, 8, 9])
s1.update([5, 6, 10])
print(f"s1 :{s1}")

print("-" * 60)
# pop, remove, discard

res = s1.pop()
print(f"res: {res}")
res = s1.pop()
print(f"res: {res}")

print(f"s1 :{s1}")
print("-" * 60)

s1.remove(8)
s1.remove(10)
# s1.remove(1)
print(f"s1 :{s1}")

print("-" * 60)
s1.discard(6)
s1.discard(4)
s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")
print("-" * 60)

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"B intresection A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozenset - immutable
fr1 = frozenset({1, 2, 3, 4, 5})
print(f"fr1 :{fr1}")
print(type(fr1))