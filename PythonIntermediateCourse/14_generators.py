# Generators:->
# Generators return a object that can be iterated over.
# It generate the items inside the Object Lazily
# Means it generates the items one at a time, only when required/ asked
# Much more memmory effiecient when we have deal with the large dataset


def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
# print(g)

# for i in g:
#     print(i)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# print(sum(g))

# print(sorted(g, reverse=True))


# def countdown(num):
#     print('Starting...')
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(6)

# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

# Example - Generator vs Iterators

# import sys

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1


# print(sys.getsizeof(firstn(1000000)))
# print(sys.getsizeof(firstn_generator(1000000)))

# Example - Fibonacci Sequence

# def fibonacci(limit):
#     a, b = 0,1
#     while a < limit:
#         yield a
#         a, b  = b, a + b

# print(list(fibonacci(30)))

# Generator Comprehension

my_generator = (x for x in range(10) if x % 2 == 0)

print(tuple(my_generator))
