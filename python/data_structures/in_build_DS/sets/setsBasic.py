'''

#sets are unordered collections of unique elements in python. They are defined using curly braces {} or the set() constructor.
#Sets can contain elements of different data types, including numbers, strings, and other sets. However, sets cannot contain mutable elements like lists or dictionaries.
#Sets are unordered, cannot have duplicates, can be nested, and can be accessed using membership testing.

s = {1, 2, 3, 4, 4, 4, 5, 5}  #Creating a set with elements 1, 2, 3, 4, and 5
print(f"Set s: {s}")


a = {1, 2, 3, 4, 5}  #Creating another set with elements 1, 2, 3, 4, and 5

for i in a:
    print(i)  #Iterating through the set and printing each element


# set Methods 

s.add(6)  #Adding an element to the set
print(f"Set s after adding 6: {s}")

s.remove(3)  #Removing an element from the set
print(f"Set s after removing 3: {s}")   

s.discard(4)  #Removing an element from the set using discard method
print(f"Set s after discarding 4: {s}")

pop_element = s.pop()  #Removing and returning an arbitrary element from the set
print(f"Set s after popping an element: {s}, Popped element: {pop_element}")

s.clear()  #Removing all elements from the set
print(f"Set s after clearing: {s}")


'''

'''


# Set Operations

# 1. Union of Sets
a = {1, 2, 3, 4, 5} 
b = {4, 5, 6, 7, 8}

s = a.union(b)  #Creating a new set that contains all elements from both sets
print(f"Union of sets a and b: {s}")

#or

s = a | b  #Using the | operator to perform union operation
print(f"Union of sets a and b using | operator: {s}")


# 2. Intersection of Sets
s = a.intersection(b)  #Creating a new set that contains only the elements that are common to both sets
print(f"Intersection of sets a and b: {s}")

#or

s = a & b #Using the & operator to perform intersection operation   
print(f"Intersection of sets a and b using & operator: {s}")


# 3. Difference of Sets
s = a.difference(b)  #Creating a new set that contains only the elements that are in set a but not in set b
print(f"Difference of sets a and b: {s}")   

#or 

s = a - b  #Using the - operator to perform difference operation
print(f"Difference of sets a and b using - operator: {s}")


# 4. Symmetric Difference of Sets
s = a.symmetric_difference(b)  #Creating a new set that contains only the elements that are in either set a or set b but not in both
print(f"Symmetric difference of sets a and b: {s}")

#or

s = a ^ b  #Using the ^ operator to perform symmetric difference operation
print(f"Symmetric difference of sets a and b using ^ operator: {s}")

'''