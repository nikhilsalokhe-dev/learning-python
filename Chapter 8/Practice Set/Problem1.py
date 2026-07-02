# 1. Write a program using functions to find greatest of three numbers.


def greatest(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f"{n1} is greatest.")

    elif n2 > n1 and n2 > n3:
        print(f"{n2} is greatest.")

    else:
        print(f"{n3} is greatest.")


n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
greatest(n1, n2, n3)
