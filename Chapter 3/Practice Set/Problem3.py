# 3. Write a program to detect double space in a string

sentence = input("Enter a sentence: ")

double_space = sentence.find("  ")

print(f"Double space is present at {double_space}th spot.")
