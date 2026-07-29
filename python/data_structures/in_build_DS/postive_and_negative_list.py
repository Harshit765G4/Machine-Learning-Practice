a = [12,-35, 45, -67, 89, -23, 56, -78, 90, -12]

print("Positive numbers in the list:")
for num in a:
    if num > 0:
        print(num, end=" ")
print()  # Print a newline at the end

print("Negative numbers in the list:")
for num in a:
    if num < 0:
        print(num, end=" ")