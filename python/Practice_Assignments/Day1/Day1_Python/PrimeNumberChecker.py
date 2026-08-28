num = int(input("Enter a Number: "))

is_prime = True

for i in range(2,(num//2)+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")