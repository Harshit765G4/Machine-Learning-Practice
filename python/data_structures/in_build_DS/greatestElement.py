a = [12,15,3,45,2,7,17,9,10,38]

greatest = a[0]  # Assume the first element is the greatest

for i in a:
    if i > greatest:
        greatest = i  # Update greatest if a larger element is found

print(f"The greatest element in the list is: {greatest} found at index {a.index(greatest)}")