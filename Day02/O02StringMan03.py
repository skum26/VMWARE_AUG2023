
# emulate printf of c language
format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")       # tuple
print(values)

print(format % values)
print("-" * 60)

format = "Welcome %s, with a rating of %.3f what a %s player"

print(format % ('Sachin', 9, 'class'))
print(format % ('Sachin', 9.2, 'class'))
replace = format % ('Sachin', 9.28, 'class')
print(replace)
print(format % ('Sachin', 9.2855567567, 'class'))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Sachin", 9.2567575, "class"))

print("-" * 60)
# emulate unix shell style
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name = "sachin", adj = "superb"))

print("-" * 60)
# format strings from python
print("Welcome {}, what a {} player".format("Sachin", "superb"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb","India"))
print("Welcome {2}, what a {0} player for {1}".format("Sachin", "superb","India"))
print("Welcome {name}, what a {adj} player for {ctry}".format(name="Sachin", adj="superb",ctry="India"))

print("Welcome {name}, your rating of {rating} what a {adj} player".format(name="Sachin", rating = 8, adj="superb"))

print("Welcome {name}, your rating of {rating:.3f} what a {adj} player".format(name="Sachin", rating = 8.27895681, adj="superb"))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant :{e}")

# python string format
print("PI = {} and Eulers Constant = {}".format(pi, e))
print("PI = {}, magic number is {} and Eulers Constant = {}".format(pi, 40585, e))
print("PI = {0}, magic number is {1} and Eulers Constant = {2}".format(pi, 40585, e))

print("-" * 60)
fullname = ["Sachin", "Tendulkar"]
print("Mr.{name}".format(name=fullname))
print("Mr.{name[0]} {name[1]}".format(name = fullname))

print("-" * 60)
import math
print(__name__)
print(math.__name__)
print("The {mod.__name__} module gives the value of pi = {mod.pi} and eulers e = {mod.e}".format(mod=math))

