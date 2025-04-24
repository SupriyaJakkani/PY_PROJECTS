# Guessing Number
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 0 to {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low!")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")
    print(f"Yay, Congrats. you have guessed number {random_number} correctly!")

guess(10)