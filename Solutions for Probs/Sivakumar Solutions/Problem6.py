# "This is problem 6 by S.Sivakumar"

# Program to generate armstrong numbers between 1 and 500

print("Program to generate armstrong numbers between 1 and 500".center(100,"-"))

print("Armstrong numbers between 1 and 500 are")
for num in range(1, 500):

    order = len(str(num))
    sum = 0; temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num,end=" ")

# validation
# 153 = 1 ** 3 + 5 ** 3 + 3 ** 3  = 1 + 125 + 27      = 153
# 370 = 3**3   +7 **3  + 0 **3 = 370