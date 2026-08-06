a = [1,1,2,3,4,4,5,5,5,6]  #Creating a list with duplicate elements
frequency = {}  #Creating an empty dictionary to store the frequency of each element

for i in a:
    if i in frequency:
        frequency[i] += 1  #Incrementing the count of the element if it already exists in the dictionary
    else:
        frequency[i] = 1  #Initializing the count of the element to 1 if it does not exist in the dictionary

print(f"Frequency of each element in the list: {frequency}")  #Printing the frequency of each element in the list