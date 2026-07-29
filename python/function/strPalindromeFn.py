def palindrome(str):

    rev = ""

    for i in range(len(str) - 1, -1, -1):
        rev += str[i] 

    if rev == str:
        print(f"The string '{str}' is a palindrome.")
    else:
        print(f"The string '{str}' is not a palindrome.") 


palindrome(str(input("Enter a string: ")))