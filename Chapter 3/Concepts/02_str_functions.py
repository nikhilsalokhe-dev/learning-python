word = input("Enter a word: ")

print("The length of word is", len(word))
print("The word starts with S is", word.startswith("S"))
print("The word ends with y is", word.endswith("y"))
print("The letter a occurs", word.count("a"), "times in the word")
print(
    "The new word when r letters are replaced by l letters is:", word.replace("r", "l")
)
