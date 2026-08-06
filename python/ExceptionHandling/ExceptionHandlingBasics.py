#Exception Handling in Python
#Exception handling is a mechanism in Python that allows you to handle runtime errors gracefully, preventing the program from crashing. It involves using try and except blocks to catch and handle exceptions that may occur during the execution of a program.
#The basic syntax of exception handling in Python is as follows:

try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  # This line may raise a ZeroDivisionError if num2 is zero
    print(f"The result of division is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    
else:
    print("Division was successful.")  # This block executes if no exception occurs
finally:
    print("Execution of the try-except block is complete.")  # This block always executes, regardless of whether an exception occurred or not


print("\n")

age = int(input("Enter your age: "))
if age < 10 or age > 18:
    raise ValueError("Age must be between 10 and 18.")  # Raising a ValueError if the age is not within the specified range
else:
    print("Welcome! You are eligible to participate in the Club.")  # Printing a welcome message if the age is within the specified range

