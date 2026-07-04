# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, item in enumerate(number_list):
    if i == 2 or i == 4 or i == 6:
        print(item)
