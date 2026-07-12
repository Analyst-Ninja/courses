def sum_of_natural_nums(n):
    return n * (n + 1) / 2


def sum_of_natural_nums_v2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


n = 100000000
print(sum_of_natural_nums(n))
print(sum_of_natural_nums_v2(n))
