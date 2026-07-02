# 9. Write a program to find out whether a file is identical and matches the content of another file.

with open("../Files/file.txt") as f:
    content1 = f.read()

with open("../Files/poems.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Both the files are identical.")

else:
    print("Both the files are not identical.")
