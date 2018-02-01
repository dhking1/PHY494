# guessinggame.py
import random

number = random.randint(1, 1000)   # secret number
guess = None

while guess != number:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("correct")
    elif guess < number:
        print("too low")
    elif guess > number:
        print("too high")
