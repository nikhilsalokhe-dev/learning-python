"""
Project 1 : Snake Water Gun Game

We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game
and write a python program capable of playing this game with the user.
"""

import random

print("RULES TO PLAY THE SNAKE, WATER AND GUN GAME:")
print("1. For Snake, choose s.")
print("2. For Water, choose w.")
print("3. For Gun, choose g.")

computer = random.choice([-1, 0, 1])

gameDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

user_choice = input("Enter your choice (s/w/g): ")
user_choice_num = gameDict[user_choice]

print(
    f"You chose {reverseDict[user_choice_num]}\nComputer chose {reverseDict[computer]}"
)

if computer == user_choice_num:
    print("It's a draw!")
elif computer == -1 and user_choice_num == 1:
    print("You win!")
elif computer == -1 and user_choice_num == 0:
    print("You lose!")
elif computer == 0 and user_choice_num == 1:
    print("You lose!")
elif computer == 0 and user_choice_num == -1:
    print("You win!")
elif computer == 1 and user_choice_num == 0:
    print("You win!")
elif computer == 1 and user_choice_num == -1:
    print("You lose!")
else:
    print("Something went wrong! Please enter a valid choice.")
