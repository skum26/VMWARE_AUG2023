

print("append".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.append(11)
l1.append(12)
l1.append(13)
print(f"l1 :{l1}")

l1.append([14, 15, 16, 17, 18])
print(f"l1 :{l1}")
print(l1[13][1:4])

print("extend".center(60, "-"))
l2 = list(range(5, 56, 5))
print(f"l2 :{l2}")

l2.extend([60, 65, 70, 75, 80, 85])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(2, 17, 2))
print(f"l1 :{l1}")
res = l1.pop(3)
print(f"res :{res}")
res = l1.pop(5)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

# res = l1.pop(5)
# print(f"res :{res}")
# print(f"l1 :{l1}")

print("remove".center(60,"-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
l1.remove(5)
l1.remove(8)
print(f"l1 :{l1}")

# l1.remove(8)
l1 = [1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2,2,2,2, 2, 1, 2, 3, 2, 2,2 ,2, 2,2,1, 1,1,1,1,1, 1, 1, 1, 2, 3, 1, 1,1, 1, 1, 1, 1, 1, 2,2, 2, 2, 2, 1,1,1,1,1,1]

while 1 in l1:
    l1.remove(1)

print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
l1.clear()

print(f"l1 :{l1}")

