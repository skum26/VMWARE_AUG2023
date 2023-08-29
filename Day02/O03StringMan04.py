
# Conversions
print("Conversion".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=3667567555))

print("-" * 60)
# Alignment
print("{num:15}Sachin".format(num=36))
print("{num:15}Sachin".format(num="Ramesh"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("Alignment".center(60, "-"))
# right
print("{fname:>15} Tendukar".format(fname = "Sachin"))
# left
print("{fname:<15} Tendukar".format(fname = "Sachin"))
# Center
print("{fname:^15} Tendukar".format(fname = "Sachin"))

print("{:*^20}".format("Sachin"))
print("Sachin".center(20, "*"))

print("{0:10.2f}\n{1:5.3f}".format(pi, -pi))
print("-" * 60)
print("{0:10.2f}\n{1:=10.3f}".format(-pi, -pi))

