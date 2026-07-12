# itertools : product, permutations, combinations, accumulate, groupby, & infnite iterators

from itertools import combinations, combinations_with_replacement, permutations, product

# 1. product
a = [1, 2, 3]
b = [3]

# prod = product(a,b, repeat=2)
# print(list(prod))

# 2. permuations
a = [1, 2, 3]

# perm = permutations(a)
# print(list(perm))
# perm = permutations(a,2)
# print(list(perm))

# 3a. combinations

# a = [1,2,3,4]

# comb = combinations(a,2)
# print(list(comb))

# # 3b. combinations_with_replacement

# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))

# 4. accumute

# from itertools import accumulate
# import operator

# a = [1,2,5,3,4]

# acc = accumulate(a) # default ==> it does the sum
# acc = accumulate(a, func=operator.mul)
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))

# 5. groupby
from itertools import groupby

a = [1, 1, 1, 2, 3, 3, 4]


def smaller_than_3(x):
    return x < 3


# groupObj = groupby(a, key=smaller_than_3)
# groupObj = groupby(a, key=lambda x : x < 3)

# for key,val in groupObj:
#     print(key, list(val))

# example 2 =

persons = [
    {"name": "A", "age": 2},
    {"name": "B", "age": 13},
    {"name": "C", "age": 40},
    {"name": "D", "age": 50},
    {"name": "E", "age": 50},
]

# person_group = groupby(persons, key = lambda x : x['age'] <= 18) # group in adult
# person_group = groupby(persons, key = lambda x : x['age']) # group on the basis of age group

# for key, val in person_group:
#     print(key, list(val))


from itertools import count, cycle, repeat

# 6. Infinite Iterators
# for i in count(10):
#     print(i)
#     if i == 15:
#         break


a = [1, 2, 3, 4]

# for i in cycle(a):
#     print(i)

for i in repeat(1, 4):
    print(i)
