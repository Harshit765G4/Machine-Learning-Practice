a = int(input("Enter a number: "))

while a > 0:
    digit = a % 10
    print(digit)
    a = a // 10