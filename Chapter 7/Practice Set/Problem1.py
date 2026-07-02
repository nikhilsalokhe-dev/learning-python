# 1. Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter a number: "))

print(f"The multiplication table of {number} is: ")
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
