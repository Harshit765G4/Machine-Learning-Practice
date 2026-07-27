# Program to count total number of characters, digits and special characters in a string

# String Methods Used is isdigit() and isalpha() used to count the number of digits and characters in the string respectively and for the special characters we can use the else statement to count the number of special characters in the string becausse special characters are neither digits nor characters and specific string methods are not available to count the number of special characters in the string.


a = "ad15yu5*&425@^*$55$%4T@@gagjb1564gd"

char = 0
dig = 0
spchar = 0
totalchar = len(a)

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchar += 1

print(f"The total number of characters in the string is: {totalchar} \nin which\nThe number of characters in the string is: {char}\nThe number of digits in the string is: {dig}\nThe number of special characters in the string is: {spchar}")