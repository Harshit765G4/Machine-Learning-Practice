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


# Four Pillars of OOPs

# 1. Inheritance - Inheritence allows a class to inherit properties and behaviours (attributes and methods) from another class (parent class). 


# Syntax of Inheritance

class Parent:
    def speak(self):
        print("I can Speak!")

class Child(Parent):
    pass

obj = Child

obj.speak(Child)



# -----------------------------------


class FactoryMumbai:
    a = "I am an attribute mentioned inside factory"

    def hello(self):
        print("Hello I am a Method mentioned inside factory.")

class FactoryPune(FactoryMumbai):
    pass

obj = FactoryPune()

obj.hello()


# --------------------------------------

# Constructor in Inheritance

# - Lets say we have created a parent class with a constructor function inside it and then this class is inherited by another class then the constructor function of parent class will work for the child class as well

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(f"My name is {self.name}")

obj = Child("Harshit")

obj.display()


# --------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"you are my {self.name}")

class Human(Animal):
    pass

person1 = Human("dog")

person1.show()


# Now Lets say you need a new parameter in your child class you have to create a constructor function for your child class but the parameters that can be initialized in the parent class will be initialized using the super() function. Super function will target the parent class. 


class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age 

    def display(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

obj = Child("Harshit", 21)

obj.display()




# -----------------------------------


# Types of Inheritance

# 1. Single Inheritance
# --> All the inheritance we saw above was single level

# 2. Multiple Inheritence
# --> Multiple Inheritance means there will be 2 parent classes and only 1 child class and the child will inherit all the attributes and methods of both parents. 

# --> Note: The constructor function will be inherited of the first class that has been Inherited. This is MRO(Method Resolution Order) followed by python. 


class Animal:
    name1 = "Lion"

class Human:
    name2 = "Harsh"

class Robots(Animal,Human):
    name3 = "charlie"

obj = Robots()

print(obj.name2)


# ---------------------------------

class Animal:
    def __init__(self, name):
        self.name = name 

class Human:
    def __init__(self, name, age):
        self.age = age

class Mammal(Human, Animal):
    pass

obj = Mammal("Harsh", 21)

print(obj.age)



# ----------------------------------

class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def show(self):
        print("I have multiple skills.")



# 3. Multilevel Inheritance
# --> This is a basic case where we will have
#     grandfather class -> parent class -> child class

#     The attributes and methods are passed on through all the classes.


class Grandparent:
    def heritage(self):
        print("Heritage from Grandfather")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

obj = Child()

obj.heritage()


# ---------------------------------


class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color 

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = PuneFactory("Cotton", 2, "Blue", 4)

print("The Bag is made up of",obj.material)

print("The Bag has in total of",obj.pockets, "Pockets")




# ---------------------------

# Polymorphism - it is a core concept in oops the word means "many formns" - and in programming, it allows the same interface or method name to behave differently depending on the object or context.

def show():
    print("How are you")

def show():
    print("You are Best")

show()

# -------------------

# Types of Polymorphism

# -> Polymorphim can be achieved in python in two ways well if we talk  about compile time languages there are 3 types but python does not support method overloading.

# -> Method overloadind means having the same name methods inside a class but parameters will be different but in python the latest defination will overide the previous one.


class Car:
    def show(self, name=None):
        if name is None:
            print("Car")
        else:
            print(name)


obj1 = Car()

obj1.show()
obj1.show("BMW")


    
# -> Method Overriding - this is where a child class overrides a method of the parent class and python decides at runtime which method to call based on the object type.

class Animal:
    def show(self):
        print("Hello How are you")

class Human(Animal):
    def show(self):
        print("Hope you are fine")

obj = Human()

obj.show()



# -----------------------

# Duck Typing - python follows a philosophy
# 'If it walks like a duck and quacks like a duck, it must be a duck'

class Duck:
    def talk(self):
        print("Quack")

class Human:
    def talk(self):
        print("Hello!")

def speak(obj):
    obj.talk()


duck = Duck()
human = Human()

speak(duck)
speak(human)

# In the speak() function, we donot care if it is a duck or a human - we only care that the object has a talk() method.

class Animal:
    def show(self):
        print("Hello I am from class Animal")

class Human:
    def show(self):
        print("Hey I am from class Human")

obj = Animal()
obj1 = Human()

obj.show()
obj1.show()


# -----------------------------

# Encapsulation - Encapsulation means putting data(variables) and code (functions) together in one place - inside a class
# - it also means hiding the internal details of how things qork and only showing what is needed

# It keeps data safe from being changed by mistake
# It makes your code clean and easy to use 
# It gives control over what others can access or change.


# Access modifiers in python 
# - Access modifiers means how we give access of our attributes and methods to the object or inherited classes. there are 3 types lets see them one by one.

# - Public Attributes and Methods
# Till now every attribute and methods we have created are public means the inherited classes and objects can access them no matters what.

class Factory:
    a = "pune"

    def show(self):
        print("Hello I am a pune Factory")

class Bhopal(Factory):
    def show(self):
         print(super().a)

obj = Bhopal()

obj.show()



# - Protected Attributes and Methods
# - python protected members are created using a single underscore but it still can be accessed from outside the class so you might wonder whats the point of using them
# - python doesnot enforce protected access like other languages(eg java or cpp). but it uses a naming convention to tell developers



class Factory:
    _a = "pune"

    def _show(self):
        print("Hello I am a pune Factory")

class Bhopal(Factory):
    def _show2(self):
         print(super()._a)

obj = Bhopal()

obj._show()

obj._show2()

# - what we are trying to say is that there is no such difference in between public and protected in python it works same as public]

# - So how we can protect our attributes and method so we use this 

# Private Attributes and Methods
# - A Private variable or Method means:
# - It cannot be accessed from outside the class - only from inside the class where it is defined 
# - In python we use two underscores(__) before the name to make it private.

class Demo:
    def __init__(self):
        self.name = "Public Member"         # Public
        self._age = 21                      # Protected
        self.__salary = 50000               # Private

    def show(self):
        print("Inaide the class:")
        print("Public: ",self.name)
        print("Protected: ",self._age)
        print("Private: ",self.__salary)

obj = Demo()

print(obj.name)
print(obj._age)
# print(obj.__salary)
obj.show()


# --------------------------------------

# Abstraction - Abstraction doesnot exists in python but we can achieve it using a library we will see what is a libray later.
# Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.
# It is used to define a common interface for different subclasses.

# Abstract Classes and methods 

# -> Abstract classes are classes that contains one or more abstract methods.
# -> A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.


from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass

class Square:
    def __int__(self, side):
        self.side = side 

    def perimeter(self):
        pass

    def area(self):
        pass

class Circle(abstract):
    def __int__(self, radius):
        self.radius = radius 

    def perimeter(self):
        pass

    def area(self):
        pass

obj = Circle()



# ----------------------------


from abc import ABC, abstractmethod

class Animal(ABC):              #Abstract class
    @abstractmethod
    def make_sound(self):       #Abstract method
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Cat Says Meow!")


obj = Dog()

obj.make_sound()