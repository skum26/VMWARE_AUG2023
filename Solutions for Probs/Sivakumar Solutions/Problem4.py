# "This is problem 4 by S.Sivakumar"

# Program to generate pascals triangle

print("This program is to print 5 rows of pascal triangle".center(100,"-"))

for i in range(6):
    for j in range(5-i):
        print(' ', end='')

    C = 1
    for j in range(1, i + 1):
        print(C, ' ', sep='', end='')
        C = C * (i - j) // j
    print()

else :
    print("PGM completed")