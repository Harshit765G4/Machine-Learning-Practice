a = int(input("Enter a number: "))

digit = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if digit==rev:
    print(f"The number {digit} is a palindrome.")
else:
    print(f"The number {digit} is not a palindrome.")