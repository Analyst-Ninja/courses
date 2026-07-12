def palindrom(num):
    temp = num
    rev = 0
    while temp > 0:
        rev = 10 * rev + temp % 10
        temp = temp // 10

    return num == rev


if __name__ == "__main__":
    try:
        num = int(input("Enter a Positive Number: "))
        print(palindrom(num))
    except Exception as e:
        print(f"{e}")
