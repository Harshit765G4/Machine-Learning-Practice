d = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}  #Creating a dictionary with integer keys and values
sum = 0  #Initializing a variable to store the sum of all values in the dictionary

for i in d:
    sum = sum + d[i]  #Calculating the sum of all values in the dictionary

print(f"Sum of all values in the dictionary: {sum}")  #Printing the sum of all values in the dictionary