#OOPs - Obeject Oriented Programming is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphism, encapsulation, etc. in the programming. The main aim of OOPs is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.


# Class: A class is a blueprint for the object. It is a logical entity that contains some data members and member functions. It defines the properties and behaviors of the object.

# Syntax of class in Python:

'''

class ClassName:
    # class body

'''

class car:
    color = "red"

car1 = car()
print("Color of car1:", car1.color)


# There are 2 types of things inside class Attributes and Methods 

# - Attributes: Attributes are the variables that are defined inside a class. They represent the state of an object. They can be of any data type like int, float, string, list, etc.

# Methods: Methods are the functions that are defined inside a class. They represent the behavior of an object. They can perform operations on the attributes of the class and can also return values.

class Animal:
    species = "Dog" #Attribute

    def make_sound(self): #Method
        print("Bark!")

#Directly accessing the attribute and method of the class
print(Animal().species)         # Accessing the attribute of the class
Animal().make_sound()           # calling the method of the class

# Object: An object is an instance of a class. It is a real-world entity that has a state and behavior. The state of an object is represented by its attributes, and the behavior is represented by its methods.

# Creating an Object

obj = Animal()

# Accessing the attributes
print(obj.species)

# Accessing the Method
obj.make_sound()


# Addition Class
class Addition:
    def __init__(self, a, b):
        print("a + b =",a + b)

obj = Addition(10, 20)



# What is self? -  self is a reference to the current instance of the class

# Constructor - constructor is a method that runs automatically when we call a class and this constructor function will target the object location


class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"your object details are: {self.material}, {self.zips}, {self.pockets}")

rebook = Factory("Leather", 3, 2)

campus = Factory("nylon", 3, 3)

print(f"Pockets in Rebook Bag: {rebook.pockets}")

rebook.show()



# ---------------------------

# Types of Attributes

# 1. class attribute - A normal variabe created inside a class is class attribute and thats it.

# 2. instance attribute - A attribute created using an instance like self.name, self.age etc. it is known as instance attribute


class car:
    wheels = 4    #class attribute

    def __init__(self, color):
        self.color = color      # Instance attribute


# Types of Methods

# 1. Instance Method - An instance method works with instance (object) of the class. this method can access and modify instance attributes

class Animal:
    name = "Lion" #class attribute

    def __init__(self, age):
        self.age = age  #instance attribute

    def show(self):
        print(f"Age of our Lion is {self.age}")

    def instance_method(self):
        print("This is an instance method")


# 2. classmethod - This method works with the class itself it will not target the instance(object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.

    @classmethod
    def hello(cls):
        print("How are you Mr. Lion")

    @classmethod
    def class_method(cls):
        print("this is a class method")

# 3. Static Method - this method doesn't access class or instace directly it also uses a decortor @staticmethod it just acts like a regular function placed inside a class.

    @staticmethod
    def static_method():
        print("this is a static method.")


obj = Animal(12) 

obj.show() # instance method

obj.class_method() # class method

obj.static_method() # static method