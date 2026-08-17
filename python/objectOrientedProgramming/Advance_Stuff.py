#Decorator - A decorator is just a function that modifies another function without changing its actual code.
# - Imagine you have a cake (your function). A decorator is like putting icing on the cake it doesnot change the cake itself, but makes it better, prettier, or adds some new flavour!
# For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.
#Its tough to understand with text



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
