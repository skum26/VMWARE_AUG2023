"""
sort    = sort will sort the original list, will not return anything
sorted  = sorted will sort the list and returns a copy of it
"""

print("Sort".center(60, "-"))
l1 = [10, 5, 9, 2, 7, 8, 1, 3, 6, 4]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending Order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 60)

l2 = [10, 'zebra', 'apple', 5, 'yellow', 'blue', 9, 'white', 'cat', 2, 'violet', 'green', 7, 'pink', 'orange', 8, 'frog', 'xmas',1, 'dog', 'umbrella', 3, 6, 4, 19, 1259, 167, 28, 201, 2378]

print(f"l2 :{l2}")

print("-" * 60)
res = sorted(l2, key=ascii)
print(f"res :{res}")

print("-" * 60)
cities = ['hyderabad', 'thiruvananthapuram', 'ooty', 'delhi', 'bangalore' 'mumbai', 'pune', 'coimbatore', 'vishakapatnam', 'kolkota']
print(f"cities :{cities}")

print("-" * 60)
res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 60)
# reverse and reversed
l1 = [10, 5, 9, 2, 7, 8, 1, 3, 6, 4]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")

l1.sort()
print(f"l1 :{l1}")
