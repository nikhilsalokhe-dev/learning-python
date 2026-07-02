# 6. Write a python function which converts inches to cms.


def inch_to_cm(inch):
    return inch * 2.54


inch = int(input("Enter a value in inches: "))

print(f"The value in cms is: {inch_to_cm(inch)}")
