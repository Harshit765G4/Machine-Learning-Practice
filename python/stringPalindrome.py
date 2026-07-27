# This program checks whether a given string is a palindrome or not.
# A palindrome is a string that reads the same backward as forward. For example, "NAMAN" is a palindrome because it remains the same when reversed.

# Method used: The program reverses the string and compares it with the original string. If both are the same, it confirms that the string is a palindrome; otherwise, it is not.


a = "12344321"

b = ""

for i in range(len(a) - 1, -1, -1):
    b += a[i]

print(b)

if b == a:
    print("The string is a palindrome.")

else:
    print("The string is not a palindrome.")

