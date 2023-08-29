
print("items".center(60, "-"))
# items is a combination of keys and values function => items returns both at the same time

emp = {
    'emp1': {'name':'jack', 'age': 27, 'dept': "MKT", 'des': 'bdm', 'loc': 'che', 'sal':35000},
    'emp2': {'name':'jane', 'age': 30, 'dept': "HR", 'des': 'HRE', 'loc': 'Hyd', 'sal':45000},
    'emp3': {'name':'Mark', 'age': 38, 'dept': "IT", 'des': 'PM', 'loc': 'blr', 'sal':85000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>" , v)
    print("-" * 40)

print("update".center(60, "-"))
emp1 = {'name':'jack', 'age': 27, 'dept': "MKT", 'des': 'bdm', 'sal':35000}
emp2 = {'name':'jane', 'age': 30, 'dept': "HR", 'des': 'HRE', 'loc': 'Hyd'}
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")


