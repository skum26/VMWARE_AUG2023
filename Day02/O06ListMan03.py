
print("index".center(60, "-"))
l1 = [1, 1, 1, 1, 2, 2, 2, 3, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1]

print(f"l1 :{l1}")
print("Index of 3:", l1.index(3))

print("-" * 60)
print("Index of 2nd 3:", l1.index(3, l1.index(3) + 1))

print("-" * 60)
print("Index of 3rd 3:", l1.index(3, l1.index(3, l1.index(3) + 1) + 1))

print("count".center(60, "-"))
l1 = [1, 1, 1, 1, 2, 2, 2, 3, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1]

print(f"l1 :{l1}")
print(f"1's :{l1.count(1)}")
print(f"2's :{l1.count(2)}")
print(f"3's :{l1.count(3)}")
print(f"5's :{l1.count(5)}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

l2 = l1       # shallow copy - l2 copies the address of l1 with data

print(f"l2 before :{l2}")
l2.extend([6, 7, 8, 9, 10])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 40)
l3 = list(range(2, 17, 2))
print(f"l3 before :{l3}")

l4 = l3.copy()          # deep copy - only data gets copied
print(f"l4 before :{l4}")

l4.append(18)
l4.append(19)
l4.append(20)
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 40)
l5 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"l5 before :{l5}")

l6  = l5.copy()     # deep copy

print(f"l6 before :{l6}")
l6[4].append(60)
l6[4].append(70)
l6[4].append(80)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 40)
l7 = [10, 20, 30, 40, [1, 2, 3, 4, 5], 50]
print(f'l7 before :{l7}')

from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[4].extend([6, 7, 8, 9])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")