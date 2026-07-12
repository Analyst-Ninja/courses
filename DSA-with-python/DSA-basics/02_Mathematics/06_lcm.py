def lcm(a, b):

    res = max(a, b)

    while True:
        if res % a == 0 and res % b == 0:
            return res
        else:
            res += 1


print(lcm(15, 12))
# Time Complexity - Theta(a*b - max(a,b))

# Efficient Way

# Formula ===> a*b = lcm(a,b) * gcd(a,b)


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


print(lcm(15, 12))

# Time Complexity --> Theta(log(min(a,b))) ==> Same as GCD
