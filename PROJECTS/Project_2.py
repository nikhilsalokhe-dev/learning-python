"""
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please” .
Similarly, if the user’s guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number.

"""

import random

random_n = random.randint(1, 100)
user_n = -1
guesses = 0

while random_n != user_n:
    user_n = int(input("Guess a number from 1 to 100: "))
    if user_n < 1 or user_n > 100:
        print("Please enter a number between 1 to 100")
        continue

    guesses += 1

    if user_n > random_n:
        print("Lower number please.")

    elif user_n < random_n:
        print("Higher number please.")


print(f"You guessed the correct number {random_n} correctly in {guesses} attempts!")
