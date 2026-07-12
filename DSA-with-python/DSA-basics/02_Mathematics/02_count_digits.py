num = abs(int(input("Enter an Integer: ")))
count = 0
while num > 0:
    num = num // 10
    count += 1

print(f"Number of digits: {count}")
