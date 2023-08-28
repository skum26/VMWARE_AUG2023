
"""
int
float
complex
"""

player_count = 11
rating = 8.7
has_won_WC = True
team_name = "India"
print("Player Count :", player_count)
print("Rating :", rating)
print("Has won the World Cup :", has_won_WC)
print("Team_name :", team_name)

# module
# double under score
print(__name__)         # dunder name

a, b, c = 1, 2, 3
print(a, b, c, sep=", ")

# interpolation
print(f"The team {team_name} has a rating of {rating}")

print(f"The sum of {a}, {b} and {c} is {a + b + c}")

print("This is 'Team India'")
print('This is "Team India"')
print('This is "Team India"')
print('This is \'Team India\'')

print("-" * 60)

a = 10
b = -10
print(f"a :{a}")
print(f"type(a) :{type(a)}")        # RTTI - Run Time Type Identifier
print(f"b :{b}")
print(f"type(b) :{type(b)}")

print("-" * 60)
c = 10.0
d = -10.0
print(f"c :{c}")
print(f"type(c) :{type(c)}")

print(f"d :{d}")
print(f"type(d) :{type(d)}")

print("-" * 60)
e = +2e3
f = -2e3
print(f"e :{e}")
print(f"type(e) :{type(e)}")

print(f"f :{f}")
print(f"type(f) :{type(f)}")

print("-" * 60)
g = 3.141j
h = -3.141j

print(f"g :{g}")
print(f"type(g) :{type(g)}")

print(f"h :{h}")
print(f"type(h) :{type(h)}")

print("-" * 60)

x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 60)

x = 1
y = 2.5
z = x + y
print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("conversion".center(40, "-"))
a = 100
print(f"type(a)\t\t{a}")
print(f"type(float(a))\t\t{float(a)}")
print(f"type(complex(a)\t\t{complex(a)}")
print(f"type(bool(a))\t\t{bool(a)}")

print("Number System".center(60,"-"))
print(11)       # decimal number
print(0b11)     # Binary
print(0b101)    # binary    # 101 = 1 + 4
print(0o11)     # octal
print(0o15)     # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number Conversion System".center(60, "-"))
a = 100
print(f"Binary :{bin(a)}")
print(f"Octal :{oct(a)}")
print(f"Hexadecimal :{hex(a)}")



