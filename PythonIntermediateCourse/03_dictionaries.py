# Dictionary:
# 1. Key-Value Pair
# 2. Unordered
# 3. Mutable

myDict = {"name": "Rohit", "age": 27, "role": "Data Engineer"}

print(myDict)

myDict2 = dict(name="Rohit", age=27, role="Data Engineer")

print(myDict2)
print(myDict2["name"], myDict2["age"], myDict2["role"])

myDict2["Experience"] = 2.4  # Mutability
print(myDict2)

myDict2["Experience"] = 3  # Update Value if Key Exists
print(myDict2)

myDict2["name"] = "Rohit Kumar"  # Update Value if Key Exists
print(myDict2)

# myDict2.pop('age')
# print(myDict2)

# myDict2.popitem() # Remove Last Added
# print(myDict2)

for key in myDict2.keys():
    print(key, myDict2[key], sep="-->")

for key, val in myDict2.items():
    print(key, val, sep="-->")

# Update the dict

myDict.update(myDict2)

print(myDict)

myDict3 = {3: 8, 9: 10}
print(myDict3[3])

myDict4 = {
    (1, 4): "Rohit",
    9: 10,
}  # Tuple can be assigned as key in dictionary --> Immutable --> Hashable
print(myDict4)
print(myDict4[(1, 4)])

myDict4 = {
    [1, 4]: "Rohit",
    9: 10,
}  # List can't be assigned as key in dictionary --> Immutable --> Not Hashable
# print(myDict4)
# print(myDict4[(1,4)])
