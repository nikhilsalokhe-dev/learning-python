# 5. Write a program which finds out whether a given name is present in a list or not.

name_list = ["Harry", "Nikhil", "Rohan", "Shivam"]

name = input("Enter your name: ")

if name in name_list:
    print("Your name is in the list.")

else:
    print("Your name is not in the list.")
