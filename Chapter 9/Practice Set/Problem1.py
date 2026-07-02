# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it
# contains the word ‘twinkle’

with open("poems.txt") as f:
    poem = f.read()
    if "twinkle" in poem:
        print("The word 'twinkle' is present in the given file.")
    else:
        print("The word 'twinkle' is not present in the given file.")
