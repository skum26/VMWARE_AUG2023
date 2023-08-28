
"""
Arithmetic
Comparison or relational
Logical
Bitwise
Ternary
"""

print("Arithematic Operators".center(60, "-"))
print(f"Add : 10 + 3 = {10 + 3}")
print(f"Sub : 10 - 3 = {10 - 3}")
print(f"Mul : 10 * 3 = {10 * 3}")
print(f"Div : 10 / 3 = {10 / 3}")
print(f"flrdiv :10 //  :{10 // 3}")
print("-" * 60)
print(f"Mod : 10 % 3 = {10 % 3}")
print(f"Exp : 10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(60,  "-"))
# =, +=, *=, -=
x = 10
print(f"x :{x}")
print("-" * 60)
x += 5
print(f"x :{x}")
print("-" * 60)
x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, >=, <=, >, <, !=
a = 10
b = 20
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("logical Operators".center(60, "-"))
# and, or and not
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 1)
print("-" * 60)

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 1)
print("-" * 60)

print(not(1 == 1 and 2 == 1))
print(not(1 == 1 or 2 == 1))
print("-" * 60)

print(f"a :{ord('a')}")     # integer representation of unicode characters
print(f"z :{ord('z')}")
print(f"A :{ord('A')}")
print(f"Z :{ord('Z')}")

print("-" * 60)
print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(60,  "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")

print(f"5 >> 1 :{5 >> 1}")
print(f"0 >> 1 :{0 >> 1}")

# ternary operator
age = 19
print("Eligible" if age >= 18 else "Not Eligible")
