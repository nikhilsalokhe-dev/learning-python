# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Your grade is\nGRADE: Ex")

elif marks >= 80:
    print("Your grade is\nGRADE: A")

elif marks >= 70:
    print("Your grade is\nGRADE: B")

elif marks >= 60:
    print("Your grade is\nGRADE: C")

elif marks >= 50:
    print("Your grade is\nGRADE: D")

else:
    print("Your grade is\nGRADE: F")
