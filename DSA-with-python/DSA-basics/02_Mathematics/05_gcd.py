# Euclideon Approach
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(gcd(15, 17))


# Optimised Euclideon Approach
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(12, 15))
