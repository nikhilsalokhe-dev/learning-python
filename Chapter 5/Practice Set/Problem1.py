# 1. Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide user with an option to look it up!

words = {
    "Aam": "Mango",
    "Kela": "Banana",
    "Hoshiyaar": "Intelligent",
    "Pariksha": "Exam",
}

word = input("Enter the word whose translation you want to know: ")

print(words[word])
