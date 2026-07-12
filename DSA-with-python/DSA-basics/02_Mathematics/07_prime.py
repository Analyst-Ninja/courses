import math


def isPrime(a):
    if a == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True


# By SQRT Time Complexity is --> O(sqrt(N))

# Super Effiecient


def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i < n:
        if (n % i == 2) or (n % (i + 2) == 0):
            return False

        i += 6

    return True


if __name__ == "__main__":
    num = 712
    print(isPrime(num))
