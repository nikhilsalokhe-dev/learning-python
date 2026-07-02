string = "This is a new text file. This will be written with file write operation."

f = open("myfile.txt", "w")

f.write(string)

f.close()
