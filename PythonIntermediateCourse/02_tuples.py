# tuples:
# 1. ordered
# 2. immutable
# 3. allows duplicate elemets
# 4. More Effiecient than Lists
# 5. Take less space than Lists

myTuple = (100,)  # Shortest Tuple
myTuple2 = (100,)  # Still a Tuple
myTuple2 = 100, 200, 300  # Still a Tuple

# myTuple2[0] = 200 # Can't Do That --> Immutable

myTuple3 = ("a", "p", "p", "l", "e")

print(myTuple3.count("p"))  # It Will give 2 --> Two Ps are there in Apple

print(myTuple3.index("p"))  # Index of 1st Occurence

# print(myTuple3.index('o')) # Value Error

print(myTuple3[2:5])  # Slicing
print(myTuple3[::2])  # Slicing with 2 as step
print(myTuple3[::-1])  # Reverse Trick

# Unpacking

myTuple4 = (0, 1, 2, 3, 4, 5, 6)

v1, *v2, v3 = myTuple4

print(v1)
print(v2)
print(v3)


# Tuple takes less space than Lists
import sys

a = [1, 2, 3, "Hello"]
b = (1, 2, 3, "Hello")

print(f"Size of List: - {sys.getsizeof(a)} Bytes")  # 88 bytes
print(f"Size of Tuple: - {sys.getsizeof(b)} Bytes")  # 72 bytes

# Tuple are more efficient than list

import timeit

print(
    timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
)  # Tuple Creation Time --> 0.005
print(timeit.timeit(stmt="[1,2,3,4,5]", number=1000000))  # List Creation time --> 0.026
