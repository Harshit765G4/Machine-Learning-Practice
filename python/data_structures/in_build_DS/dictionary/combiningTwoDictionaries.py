a = {10: 100, 20: 200, 40: 300}
b = {40: 400, 50: 500, 60: 600}

for i in b:
    if i in a.keys():
        a[i] += b[i]  #If the key already exists in dictionary a, add the value from dictionary b to the existing value in dictionary a
    else:
        a[i] = b[i]  #If the key does not exist in dictionary a, add the key-value pair from dictionary b to dictionary a

print(f"Combined Dictionary: {a}")  #Printing the combined dictionary