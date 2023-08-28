
# for loop

for i in range(1, 11):
    print(i, end=" ")

print()
print("-" * 60)

for i in range(10, 0, -1):
    print(i, end=" ")

print()
print("-" * 60)

# continue - skip the iteration
# break the current iteration

for i in range(1, 26):
    if i % 2 == 1: continue
    # if i > 20: break
    print(i, end=" ")
else:
    print("\niteration completed.....")

print("While loop".center(60, "-"))
i = 1
while (i <= 10):
    print(i, end=" ")
    i += 1

print()
print(f"after :{i}")

