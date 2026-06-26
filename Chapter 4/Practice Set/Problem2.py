# 2. Write a program to accept marks of 6 students and display them in a sorted manner

marks = []

m1 = int(input("Enter marks of 1st student: "))
marks.append(m1)
m2 = int(input("Enter marks of 2nd student: "))
marks.append(m2)
m3 = int(input("Enter marks of 3rd student: "))
marks.append(m3)
m4 = int(input("Enter marks of 4th student: "))
marks.append(m4)
m5 = int(input("Enter marks of 5th student: "))
marks.append(m5)
m6 = int(input("Enter marks of 6th student: "))
marks.append(m6)

marks.sort()

print(f"The marks of the students are: {marks}")
