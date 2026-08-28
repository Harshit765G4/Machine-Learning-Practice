num = int(input("Enter a Number: "))
first = 0
second = 1
for i in range(num):
    print(first,end=', ')
    first, second = second, first + second