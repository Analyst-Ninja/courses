def fun(n):
    return int(n * (n + 1) / 2)


if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter number: "))

            if num >= 0:
                print(f"Sum of {num} natural number:- {fun(num)}")
            else:
                print(f"Please enter a Positive Integer Number")

        except Exception as e:
            print(f"Error: {e}, Please enter a Positive Integer Number")
