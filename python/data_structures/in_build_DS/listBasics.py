a = [5, 10, 15, 20]

print(f"List a: {a}")
for i in range(len(a)):  #Accessing elements of the list using a for loop
    print( f"a[{i}]: {a[i]}")

#Methods of List

a.append(25)  # Adds an element to the end of the list
print(f"Appended 25: {a}")

a.insert(2, 12)  # Inserts an element at a specific index
print(f"Inserted 12 at index 2: {a}")

a.extend([30, 35])  # Adds multiple elements to the end of the list
print(f"Extended list: {a}")

a.remove(10)  # Removes the first occurrence of an element
print(f"Removed 10: {a}")

removed_element = a.pop(3)  # Removes the element at a specific index and also it returns the removed element or you can store it in a variable like this: removed_element = a.pop(3)
print(f"Popped element at index 3: {a}")
print(f"Removed element: {removed_element}")

a.index(15)  # Returns the index of the first occurrence of an element
print(f"Index of 15: {a.index(15)}")

count_of_5 = a.count(5)  # Returns the number of occurrences of an element
print(f"Count of 5: {count_of_5}")

a.sort()  # Sorts the list in ascending order
print(f"Sorted list: {a}")

a.reverse()  # Reverses the order of the list
print(f"Reversed list: {a}")

copied_list = a.copy()  # Returns a shallow copy of the list
print(f"Copied list: {copied_list}")

a.clear()  # Removes all elements from the list
print(f"Cleared list: {a}")

