#Decorator - A decorator is just a function that modifies another function without changing its actual code.
# - Imagine you have a cake (your function). A decorator is like putting icing on the cake it doesnot change the cake itself, but makes it better, prettier, or adds some new flavour!
# For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.
#Its tough to understand with text


# --------------------------------------
def new_line():
    for i in range(25):
        print("-",end=" ")
    print("\n")
# ---------------------------------------

def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# -----------------------------

def addDecorate(func):
    def wrapper(a,b):
        print("The addition to your nums are")
        func(a,b)
        print("Thankyou.")
    return wrapper

@addDecorate
def addition(a,b):
    print(f"your total is {a+b}")

addition(12,16)



# -----------------------------

# For making the decorator with arguments it is tough for this we will move towards our next advance stuff *args, **kwargs.
# Args and Kwargs - They are special keywords in python used in function definitions to accept a flexible number of arguments.
# - Now you always donot have to use args and kwargs the main thing is *, ** you can use any names in front of them.
# - so *args are used for multiple positional arguments and **kwargs are used for multiple key word arguments
# - And the *args becomes a tuple and **kwargs becomes a dictionary.
# - The use case is great: 
#           1. you donot need to know how many inputs you will get.
#           2. Helps in building flexible functions, decorators, APIs, and more.


def fun(*args, **kwargs):
    print("Args:", args)
    print("kwargs:", kwargs)

fun(1, 2, 3, name="Arin", age=21)

# ------------------------------------

print("\n\n")

def addDecorate(func):
    def wrapper(*args,**kwargs):
        print("The addition to your nums are")
        func(*args,**kwargs)
        print("Thankyou.")
    return wrapper

@addDecorate
def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)

addition(12,16,24,54)


print("\n\n")

def info(**kwargs):
    print("Confirm Your Information:\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

info(name = "Harshit", age = 23, designation = "AI/ML")

# ----------------------------------------
new_line()
# new = [print("-",end=" ") for i in range(15)]
# ----------------------------------------

# List, Dictionary and set comphrehension
# - All of these comphrehensions are used to create list, dictionary, and set. but we donot have to use multiple lines of code for loops and if-else statements.

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]    #list comprehension
print(labels,"\n")


# new = [print("-",end=" ") for i in range(15)]                         # for new line easy and simple


evens = {x: x * x for x in range(10) if x%2 == 0}           #dictionary comprehension
print(evens)

print("\n")

unique_even_squares = {x*x for x in range(10) if x % 2 == 0}        #set comprehension
#{0, 4, 16, 36, 64}
print(unique_even_squares)


print("\n")

print_even = {x for x in range (1,21) if x % 2 == 0}
print(print_even)


new_line()

# ------------------------------------

# lambda functions - A lambda function is an anonymous, inline function defined using the lambda keyword.
# - Its often used for short, simple functions that are used only once or temporarily
# - you can have multiple arguments but there will be only one expression.


new_addition_using_lambda = lambda a,b : a+b
print("The sum of a and b is ", new_addition_using_lambda(2,4))

check_even_using_lambda = lambda a : "even" if a % 2 == 0 else "odd"
print("Your Number is :",check_even_using_lambda(42))
print("Your Number is :",check_even_using_lambda(11))



square = lambda x: x**2
print("Square of your number is: ",square(4))



new_line()

# ----------------------------

# Map filter and zip
# - Map is used for applying a function to multiple items.
# - Takes a list(or any sequences)
# - Applies the same function to every item in that list
# - Gives us back a new list(in Python 3, it gives a map object which you can convert to a list)


numbers = [1,2,3,4,5]
doubled = map(lambda x: x*2 , numbers)
print(list(doubled))

# - Use map() when you want to transform every items in a list.
# - it doesnot remove or skip items(that's what filter() does). 
# - you can use it with lambda or normal functions.

# - Filter as the name suggest is used to filter out the stuff.
# - Takes a list (or other sequences)
# - Checks each items using a function(a test)
# - keeps only the items that pass the test (i.e return True)

numbers = [1,2,3,4]
evens = filter(lambda x : x % 2 == 0, numbers)
print(list(evens))


new_line()

# -------------------------------

# Modules and packages
# - Module is just a single file containing code and we can use this file code in other file.
# - A single python file(.py)
# - Contains functions, variables, or classes
# - Used to organize and reuse code
# - python comes with lots of ready to use modules like:
#       1. math(for math operations)
#       2. random(for random generating numbers)
#       3. datetime(for date and time) 


import math
print(math.sqrt(16))


from modelss.model import self_maths_module
print("sum of your numbers is:", self_maths_module.addFromModule(4,6))
print("product of your number is:", self_maths_module.multiplicationFromModule(4,5))

# or we can also import the whole function like this
from modelss.model.self_maths_module import addFromModule                         # function imported from module
print("sum of your numbers is:", self_maths_module.addFromModule(11,54))


# Packages - a package is a folder that contains one or more modules(python files). it may also contain sub-packages.
# and you just have to use from and import keywords to use these things. you understood how these things work.
# There are third party packages as well like numpy, pandas, matplotlib etc. and we have to install all of these.


from modelss.model import hello
print(hello.hello())

from modelss.model.hello import hello
print(hello())