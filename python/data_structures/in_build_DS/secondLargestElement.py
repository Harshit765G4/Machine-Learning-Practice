a = [12,15,3,45,21,7,17,9,10,38]

greatest = a[0]  # Assume the first element is the greatest
second_greatest = None  # Initialize second greatest as None

for i in a:
    if i > greatest:
        second_greatest = greatest # Update second greatest before updating greatest
        greatest = i  # Update greatest if a larger element is found
    elif second_greatest is None or (i>second_greatest and i < greatest):
        second_greatest = i  # Update second greatest if a larger element is found

print(f"The second largest element in the list is: {second_greatest} found at index {a.index(second_greatest)}")