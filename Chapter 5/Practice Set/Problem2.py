# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))
n5 = int(input("Enter 5th number: "))
n6 = int(input("Enter 6th number: "))
n7 = int(input("Enter 7th number: "))
n8 = int(input("Enter 8th number: "))

number_set = {n1, n2, n3, n4, n5, n6, n7, n8}

print(f"The numbers you entered are: {number_set}")
