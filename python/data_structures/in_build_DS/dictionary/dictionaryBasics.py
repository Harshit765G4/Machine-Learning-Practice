#Dictionary are unordered collections of key-value pairs in Python. They are defined using curly braces {} or the dict() constructor. Each key in a dictionary must be unique and immutable, while the values can be of any data type and can be mutable. Dictionaries are mutable, meaning that their contents can be changed after they are created. They can be nested, meaning that a dictionary can contain other dictionaries as values. Dictionaries are accessed using keys, and they support various methods for adding, removing, and modifying key-value pairs.

# dictionary follows insertion order as of Python 3.7, meaning that the order in which key-value pairs are added to the dictionary is preserved. This allows for predictable iteration over the items in a dictionary.

dict = {'name': 'John', 'age': 30, 'city': 'New York'}  #Creating a dictionary with keys 'name', 'age', and 'city' and their corresponding values
print(f"Dictionary: {dict}")

print(f"Name: {dict['name']}")  #Accessing the value associated with the key 'name'

#Dictionary methods for adding, removing, and modifying key-value pairs:

dict.update({'age': 31})  #Updating the value associated with the key 'age'
print(f"Updated Dictionary: {dict}")

dict['country'] = 'USA'  #Adding a new key-value pair to the dictionary
print(f"Dictionary after adding a new key-value pair: {dict}")

#or

dict.update({'country': 'USA'})  #Adding a new key-value pair to the dictionary using the update() method
print(f"Dictionary after adding a new key-value pair using update(): {dict}")


del dict['city']  #Removing the key-value pair with the key 'city' from the dictionary
print(f"Dictionary after removing the key-value pair with the key 'city': {dict}")


#Traversing a dictionary can be done using a for loop to iterate over the keys, values, or key-value pairs. Here are some examples:
print("\n")
d = {10:100, 20:200, 30:300, 40:400, 50:500}  #Creating a dictionary with integer keys and values
print("Traversing the dictionary using a for loop:")

for i in d:
    print(f"Key: {i}, Value: {d[i]}")  #Accessing the value associated with each key in the dictionary
print("\n")

for i in d.keys():
    print(f"Key: {i}")  #Iterating over the keys of the dictionary
print("\n")

for i in d.values():
    print(f"Value: {i}")  #Iterating over the values of the dictionary
print("\n")

for i in d:
    print(i, d[i])  #Iterating over the key-value pairs of the dictionary
print("\n")

#shallow copy and deep copy of dictionary
import copy

#Shallow copy of a dictionary creates a new dictionary object that references the same key-value pairs as the original dictionary. Changes made to the shallow copy will affect the original dictionary and vice versa.
original_dict = {'a': 1, 'b': 2, 'c': 3}
shallow_copy_dict = original_dict.copy()  #Creating a shallow copy of the original dictionary   


help(dict)