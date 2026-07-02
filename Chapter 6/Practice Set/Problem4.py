# 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")

if len(username) < 10:
    print(
        "Your username has less than 10 characters. Please enter a valid username with more than 10 characters."
    )
else:
    print("Your username has more than 10 characters. It is a valid username.")
