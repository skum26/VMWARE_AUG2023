# "This is problem 2 by S.Sivakumar"

# Program to display the Fibonacci sequence

print("Program to print Fibonacci series".center(100,"-"))

total_terms = int(input("Please enter the terms you want to print? "))

# To check +ve number
if total_terms <= 0:
   print("Please enter a positive number")
n1, n2 = 0, 1 # first two terms are fixed
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, total_terms):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

