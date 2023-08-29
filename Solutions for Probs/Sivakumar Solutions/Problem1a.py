#  "This is problem 1a by S.Sivakumar"

z = 0
for i in range(1, 5):
    for j in range(0, i ):
        z = z +1
        if (z == 10) :
            print(0, end='')
        else :
            print(z, end='')
    print(" ")
print ("*" *20)
