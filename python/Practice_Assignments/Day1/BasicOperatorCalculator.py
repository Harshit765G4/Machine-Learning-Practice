num1 = int(input("Enter Your First Number: "))
num2 = int(input('Enter Your Second Number: '))

operator = input("Chose your Operator(+,-,*,/): ")

match operator:
    case '+':
        print('Sum of your numbers is:',num1+num2)
    case '-':
        print('Difference of your numbers is:',num1 - num2)
    case '*':
        print('Product of your numbers is:',num1*num2)
    case '/':
        print('Division of your numbers is:',num1/num2)
    