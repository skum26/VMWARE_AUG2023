# "This is problem 1c by S.Sivakumar"

# first pattern
for x in range (0,5) :
    for k in range(1, 5-x):
        print(" ", end="")
    for y in range(0, x):
        print(y+1, end=" ")
    print()
for x in range (5,0, -1) :
    for k in range(1, 5-x):
        print(" ", end="")
    for y in range (0,x) :
        print (y+1, end=" ")
    print()

print("*"*60)
# second pattern
print()
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
for i in range(2, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print ("*" *20)
