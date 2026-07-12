# lambda arguements : expression

# add10 = lambda x : x+10
# mul = lambda x,y : x*10

# print(add10(5))
# print(mul(2,5))

# points2D = [(1,2),(1,1),(6,-7),(-1,4)]

# sortedPoints = sorted(points2D) # Sort basis on the first value then the subsequent values
# print(sortedPoints)

# # Using Lambda

# def sort_basis_y(x):
#     return x[1]

# sortedPoints2 = sorted(points2D, key= lambda x : x[1])

# # Sorting according to the sum

# sortedPoints2 = sorted(points2D, key= lambda x : x[1] + x[0])
# sortedPoints2 = sorted(points2D, key=sort_basis_y)
# print(sortedPoints2)

# Map Function

# map(function, sequence)

a = [1, 2, 3, 4]

b = list(map(lambda x: x * 2, a))

print(b)

# List Comprehension

c = [x * 2 for x in a]

print(c)

# Filter Function
# filter(function, sequence)

b = list(filter(lambda x: x % 2 == 0, a))  # get only the even number

print(b)

c = [x for x in a if x % 2 == 0]

print(c)

# Reduce --> Only Reduce a single Value
# reduce(function, sequence)

from functools import reduce

product_a = reduce(lambda x, y: x * y, a)

print(product_a)
