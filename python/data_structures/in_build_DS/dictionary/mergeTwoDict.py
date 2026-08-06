a = {'name': 'Alice', 'age': 25}
b = {'city': 'New York', 'country': 'USA'}

for i in b:
    a[i] = b[i]  #Adding key-value pairs from dictionary b to dictionary a

print(f"Merged Dictionary: {a}")  #Printing the merged dictionary