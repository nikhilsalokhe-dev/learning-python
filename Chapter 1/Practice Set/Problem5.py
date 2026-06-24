# 5. Label the program written in problem 4 with comments.

# Import the os module to work with directories and files
import os

# Specify the directory path
# "." represents the current directory
path = "/"

# Get a list of all files and folders in the directory
contents = os.listdir(path)

# Print a heading
print("Contents of the directory:")

# print the contents of the directory
print(contents)
