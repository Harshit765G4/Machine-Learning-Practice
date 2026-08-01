#tuples are immutable data structures in python. They are similar to lists but cannot be modified after creation. Tuples are defined using parentheses ().
#Tuples can contain elements of different data types, including numbers, strings, and other tuples
#tuples are immutable , can have duplicates, Ordered, can be nested, and can be accessed using indexing and slicing.

a = (1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)  #Creating a tuple with elements 1, 2, 3, 4, and 5

print(f"Tuple a: {a}")


#Methods available for tuples:
#1. count(): This method returns the number of occurrences of a specified element in the tuple

count_4 = a.count(4)  #Counting the occurrences of the element 4 in the tuple
print(f"Count of 4 in tuple a: {count_4}")

#2. index(): This method returns the index of the first occurrence of a specified element in the tuple
index = a.index(3)  #Finding the index of the first occurrence of the element 3 in the tuple
print(f"Index of 3 in tuple a: {index}")

#tuple Unpacking: This feature allows you to assign the elements of a tuple to multiple variables in a single statement. The number of variables must match the number of elements in the tuple.
b = (10, 20, 30)  #Creating a tuple with elements 10, 20, and 30
x, y, z = b  #Unpacking the tuple into variables x, y, and z
print(f"Unpacked values from tuple b: x={x}, y={y}, z={z}")