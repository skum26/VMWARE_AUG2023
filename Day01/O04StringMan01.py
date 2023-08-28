
st = "Hello World"
print(f"st :{st}")
print(type(st))

# strings are stored like an array or list
print(f"st[0] : {st[0]}")
print(f"st[6] : {st[6]}")
print(f"st[10] : {st[10]}")

print(f"string length :{len(st)}")
# Slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[O:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f":st[-11] :{st[-11]}")

# slicing in reverse order
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)

# print(f"st :{st}")
# st[0] = "h"

print(dir(st))