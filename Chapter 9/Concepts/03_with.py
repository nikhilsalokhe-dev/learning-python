f = open("../Files/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:

with open("../Files/file.txt") as f:
    print(f.read())

# Here, closing the file is not needed.
