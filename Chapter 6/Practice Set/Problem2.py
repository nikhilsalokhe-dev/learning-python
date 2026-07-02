# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and
# at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

m1 = int(input("Enter marks of Subject 1 out of 100: "))
m2 = int(input("Enter marks of Subject 2 out of 100: "))
m3 = int(input("Enter marks of Subject 3 out of 100: "))

total = float((m1 + m2 + m3) / 3)

if m1 >= 33 and m2 >= 33 and m3 >= 33 and total >= 40:
    print("Congratulations! You are passed!")
    print(f"RESULT: PASS ({total}%)")

elif total < 40:
    print("Unfortunately, you are failed as your total is below 40%.")
    print("RESULT: FAIL")

elif m1 < 33 or m2 < 33 or m3 < 33:
    print(
        "Unfortunately, you are failed due to getting below 33% in one or more subjects."
    )
    print("RESULT: FAIL")
