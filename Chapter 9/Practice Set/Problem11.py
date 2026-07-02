# 11. Write a python program to rename a file to “renamed_by_python.txt”.

with open("../Files/myfile.txt") as f:
    content = f.read()

with open("../Files/renamed_by_python.txt", "w") as f:
    f.write(content)
