import random

num = random.randint(1, 10)

guess = 0
tries = 0

while guess != num:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess < num:
        tries += 1
        print("Too low! Try again.")
    elif guess > num:
        tries += 1
        print("Too high! Try again.")
    else:
        tries += 1
        print("Congratulations! You guessed the correct number.")
        print(f"You made {tries} attempts to Guess the Number.")