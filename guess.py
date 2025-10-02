# guess.py
# Simple number guessing game 🎲

import random

def main():
    print("Welcome to the Guessing Game! 🎉")
    print("I'm thinking of a number between 1 and 20...")

    # computer chooses random number
    secret = random.randint(1, 20)
    guess = None
    attempts = 0

    # loop until guessed correctly
    while guess != secret:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret}.")
                print(f"You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()


