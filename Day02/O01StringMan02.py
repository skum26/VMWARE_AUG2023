
st = "hello world"

# upper, lower
res = st.upper()
print(f"uppper_case :{res}")

res1 = res.lower()
print(f"Lower_case :{res1}")

print("-" * 60)
# maketrans and translate
st = 'hello world'
print(f"st :{st}")
# the length of a and b should be the same
a = 'helowrd'
b = 'HELOWRD'
resTbl = st.maketrans(a, b)
print(resTbl)

res = st.translate(resTbl)
print(f"res :{res}")

print("-" * 60)
st = ('the quick brown fox jumps over the lazy dog')
print(f"st :{st}")

print("find".center(60, "-"))
pos1 = st.find("fox")
print(f"pos1 :{pos1}")

pos2 = st.find('the', 5)
print(f"pos2 :{pos2}")

print("replace".center(60, "-"))
print(f"st :{st}")
res = st.replace("fox", "tiger")
print(f"res :{res}")

res1 = st.replace("the", "The", 1)
print(f"res1 :{res1}")

print("split".center(60, "-"))
# convert the string into a list
resLst = st.split()
print(f"res :{resLst}")
print(type(resLst))

print("join".center(60, "-"))
resStr = " ".join(resLst)
print(f"resStr :{resStr}")
print(type(resStr))

