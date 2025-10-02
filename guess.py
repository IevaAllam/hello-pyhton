# guess.py
# Simple number guessing game 🎲 with replay option

import random

def play_game():
    print("\nWelcome to the Ieva Number Game! 🎉")
    print("I have a number between 1 and 10 in mind...")
    print("You have 3 tries to guess it!")

    # computer chooses random number
    secret = random.randint(1, 10)
    attempts = 3  # limit of tries

    # Loop for max attempts
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Take a guess: "))

            if guess < secret:
                print("Too low! ❄️")
            elif guess > secret:
                print("Too high! 🔥")
            else:
                print(f"🎉 Correct! The number was {secret}.")
                print(f"You guessed it in {attempt} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")
    else:
        # Only runs if loop never breaks
        print(f"😢 Game Over! The number was {secret}.")

def main():
    while True:  # loop for replay
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    main()


