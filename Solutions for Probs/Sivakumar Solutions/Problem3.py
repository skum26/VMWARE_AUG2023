# "This is problem 3 by S.Sivakumar"

# Program to print next  strong number after 145

print("This program is to print the next strong number after 1, 2, 145".center(100,"-"))

for number in range(1, 100000) :
    sum = 0 ;  temp = number
    while (number):
        i = 1 ;  fact = 1
        rem = number % 10
        while (i <= rem):
            fact = fact * i  # factorial of each number
            i = i + 1
        sum = sum + fact
        number = number // 10
    if (sum == temp):
        if (temp > 145 ) :
            print("The next strong number in the series 1, 2, 145 is ", temp)

#validation -
# 145! = 1! + 4! + 5!       = 1  + 24 + 120        = 145
#40585 = 4! +0 ! +5! + 8! +5! = 24 +1+ 120+ 40320+ 120 = 40585